

import inspect
import json
from datetime import datetime
from typing import TypeVar, Type

import httpx

from gatepay.base_request import BaseRequest
from gatepay.base_response import BaseResponse
from gatepay.common.utils.random_utils import RandomUtils
from gatepay.common.utils.string_utils import StringUtils
from gatepay.common.utils.snake_camel_utils import CamelAndSnakeUtils
from gatepay.gatepay_config import GatePayConfig
from gatepay.gatepay_http_client import GatePayHttpClient

Req = TypeVar('Req', bound=BaseRequest)
Resp = TypeVar('Resp', bound=BaseResponse)

class BaseApi:


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 BaseApi 实例

        :param gate_pay_config: GatePay配置
        """
        self.gate_pay_http_client = GatePayHttpClient(gate_pay_config)

    def _pre_process(self, req: Req) -> bool:
        """
        前置处理

        :param req: 请求对象
        :return: 处理结果
        :raises IllegalAccessException: 当必填字段为空时
        """
        # 获取请求对象的所有属性
        for name, value in inspect.getmembers(req):
            # 检查是否有GatePayParam注解且为必填项
            if self._has_gatepay_param_annotation(req, name) and self._is_required_field(req, name):
                if value is None:
                    raise RuntimeError(f"Field {name} is required!")
        return True

    def _do_process(self, req: Req) -> httpx.Response:
        """
        处理请求

        :param req: 请求对象
        :return: HTTP响应
        :raises IOException, IllegalAccessException, InterruptedException
        """
        # 生成HTTP请求
        timestamp = int(datetime.now().timestamp() * 1000)  # 模拟System.currentTimeMillis()
        nonce = RandomUtils.generate_nonce(9)  # 生成随机字符串
        http_request = self.gate_pay_http_client.generate_http_request(req, timestamp, nonce)

        # 发送HTTP请求
        response = self.gate_pay_http_client.get_http_client().send(http_request)
        return response

    def _post_process(self, to_snake_json_str: str, resp_class: Type[Resp]) -> Resp:
        """
        后置处理

        :param to_snake_json_str: JSON字符串
        :param resp_class: 响应类
        :return: 响应对象
        :raises JsonProcessingException, Exception
        """
        if StringUtils.is_empty(to_snake_json_str):
            return resp_class()

        # 检查响应类是否有GatePayRespData注解
        exist_gatepay_resp_data = False
        for name in dir(resp_class):
            if not name.startswith('_') and self._has_gatepay_resp_data_annotation(resp_class, name):
                exist_gatepay_resp_data = True
                break

        if exist_gatepay_resp_data:
            # 处理带注解的响应
            spec_resp = BaseResponse()
            spec_resp.data = resp_class()

            # 解析JSON
            json_data = json.loads(to_snake_json_str)
            return_spec_resp = BaseResponse()
            return_spec_resp.code = json_data.get('code')
            return_spec_resp.status = json_data.get('status')
            return_spec_resp.label = json_data.get('label')
            return_spec_resp.error_message = json_data.get('error_message')
            return_spec_resp.data = json_data.get('data')

            resp = resp_class()
            resp.code = return_spec_resp.code
            resp.status = return_spec_resp.status
            resp.label = return_spec_resp.label
            resp.error_message = return_spec_resp.error_message
            resp.data = return_spec_resp.data
            return resp

        # 直接解析JSON到响应类
        json_data = json.loads(to_snake_json_str)
        resp = resp_class()
        for key, value in json_data.items():
            if hasattr(resp, key):
                setattr(resp, key, value)
        return resp

    def process(self, req: Req, resp_class: Type[Resp]) -> Resp:
        """
        处理请求

        :param req: 请求对象
        :param resp_class: 响应类
        :return: 响应对象
        """
        try:
            self._pre_process(req)
            http_response = self._do_process(req)
            to_snake_str = CamelAndSnakeUtils.convert_camel_json_to_snake(http_response.text)
            print(to_snake_str)
            return self._post_process(to_snake_str, resp_class)
        except Exception as e:
            raise RuntimeError(str(e)) from e

    def _has_gatepay_param_annotation(self, obj, field_name: str) -> bool:
        """
        检查字段是否有GatePayParam注解（辅助方法）

        :param obj: 对象实例
        :param field_name: 字段名
        :return: 是否有注解
        """
        # 这里需要根据实际Python实现调整
        # 可以使用装饰器或其他方式标记字段
        return hasattr(obj, f"_{field_name}_gatepay_param")

    def _is_required_field(self, obj, field_name: str) -> bool:
        """
        检查字段是否为必填项（辅助方法）

        :param obj: 对象实例
        :param field_name: 字段名
        :return: 是否为必填项
        """
        # 这里需要根据实际Python实现调整
        # 可以使用装饰器或其他方式标记必填字段
        return hasattr(obj, f"_{field_name}_required")

    def _has_gatepay_resp_data_annotation(self, obj, field_name: str) -> bool:
        """
        检查字段是否有GatePayRespData注解（辅助方法）

        :param obj: 对象实例
        :param field_name: 字段名
        :return: 是否有注解
        """
        # 这里需要根据实际Python实现调整
        # 可以使用装饰器或其他方式标记字段
        return hasattr(obj, f"_{field_name}_gatepay_resp_data")
