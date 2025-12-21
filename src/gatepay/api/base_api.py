

import inspect
import json
from datetime import datetime
from typing import TypeVar, Type, Optional

import httpx

from src.gatepay.api.model.req.query_chains_req import QueryChainsReq
from src.gatepay.api.model.req.withdraw.query_balance_req import QueryBalanceReq
from src.gatepay.api.model.req.query_status_req import QueryStatusReq
from src.gatepay.api.model.resp.query_chains_resp import QueryChainsResp
from src.gatepay.api.model.resp.withdraw.query_status_resp import QueryStatusResp
from src.gatepay.api.model.resp.withdraw.query_balance_resp import QueryBalanceResp
from src.gatepay.api.processor import Processor
from src.gatepay.base_request import BaseRequest
from src.gatepay.base_response import BaseResponse, T
from src.gatepay.common.enums.code import Code
from src.gatepay.common.enums.status import Status
from src.gatepay.common.utils.random_utils import RandomUtils
from src.gatepay.common.utils.snake_camel_utils import CamelAndSnakeUtils
from src.gatepay.common.utils.string_utils import StringUtils
from src.gatepay.gatepay_config import GatePayConfig
from src.gatepay.gatepay_http_client import GatePayHttpClient

Req = TypeVar('Req', bound=BaseRequest)
Resp = TypeVar('Resp', bound=BaseResponse)

class BaseApi:


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 BaseApi 实例

        :param gate_pay_config: GatePay配置
        """
        self.gate_pay_http_client = GatePayHttpClient(gate_pay_config)
        self.processor = Processor()

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

    def process_non_base_response(self, req: Req, resp_class: Type[T]) -> 'BaseResponse[T]':
        """
        处理非基础响应的请求

        Args:
            req: 请求对象
            resp_class: 响应数据类

        Returns:
            BaseResponse: 处理后的基础响应对象

        Raises:
            RuntimeException: 当处理过程中出现异常时抛出
        """
        try:
            # 前置处理
            self._pre_process(req)

            # 执行请求处理
            http_response = self._do_process(req)

            # 使用PROCESSOR处理响应
            return self.processor.post_process_response(http_response.text, resp_class)

        except Exception as e:
            raise RuntimeError(str(e))