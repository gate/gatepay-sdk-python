

import json
from typing import TypeVar, Optional
from urllib.parse import urlencode

import httpx

from gatepay.base_request import BaseRequest
from gatepay.common.gatepay_constants import GatePayConstants
from gatepay.infrastructure.security.signatures import Signature
from gatepay.gatepay_config import GatePayConfig
from gatepay.common.utils.snake_camel_utils import CamelAndSnakeUtils
from gatepay.common.utils.common_utils import CommonUtils

T = TypeVar('T', bound=BaseRequest)


class GatePayHttpClient:

    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 GatePayHttpClient 实例

        :param gate_pay_config: GatePay配置
        """
        self.gate_pay_config = gate_pay_config
        # 使用 httpx 作为 HTTP 客户端，替代 Java 的 HttpClient
        self.http_client = httpx.Client(
            timeout=gate_pay_config.get_timeout().total_seconds()
        )

    def generate_http_request(self, request: T, timestamp: int, nonce: str) -> Optional[httpx.Request]:
        """
        生成http请求

        :param request: 请求对象
        :param timestamp: 时间戳
        :param nonce: 随机字符串
        :return: HTTP请求对象
        :raises: IllegalAccessException, JsonProcessingException
        """
        headers = {
            GatePayConstants.HEADER_CONTENT_TYPE: GatePayConstants.HEADER_APPLICATION_JSON,
            GatePayConstants.HEADER_GATEPAY_TIMESTAMP: str(timestamp),
            GatePayConstants.HEADER_GATEPAY_NONCE: nonce,
            GatePayConstants.HEADER_GATEPAY_CERTIFICATE_CLIENT_ID: self.gate_pay_config.get_client_id()
        }

        http_method = request.get_api().get_http_method()

        if GatePayConstants.METHOD_GET == http_method:
            return self._populate_builder_for_get_delete(request, headers, timestamp, nonce, "GET")

        if GatePayConstants.METHOD_DELETE == http_method:
            return self._populate_builder_for_get_delete(request, headers, timestamp, nonce, "DELETE")

        if GatePayConstants.METHOD_POST == http_method:
            return self._populate_builder_for_post_put(request, headers, timestamp, nonce, "POST")

        if GatePayConstants.METHOD_PUT == http_method:
            return self._populate_builder_for_post_put(request, headers, timestamp, nonce, "PUT")

        return None

    def _populate_builder_for_get_delete(self, request: T, headers: dict, timestamp: int, nonce: str,
                                         method: str) -> httpx.Request:
        """
        填充http请求builder

        :param request: 请求对象
        :param headers: 请求头字典
        :param timestamp: 时间戳
        :param nonce: 随机字符串
        :param method: HTTP方法
        :return: HTTP请求对象
        """
        # 构建查询参数
        params = {}
        for name in dir(request):
            # 过滤掉私有属性和方法
            if not name.startswith('_') and not callable(getattr(request, name)):
                # 检查是否有 GatePayParam 注解且值不为None
                if self._has_gatepay_param_annotation(request, name) and getattr(request, name) is not None:
                    #name 要换成驼峰
                    camel_name = CamelAndSnakeUtils.to_camel_case(name)
                    params[camel_name] = getattr(request, name)

        # 生成参数字符串
        param_str = ""
        if params:
            param_str = "?" + urlencode(params)

        # 添加签名头
        signature = Signature.verify_signature(
            str(timestamp),
            nonce,
            "",
            self.gate_pay_config.get_credential().get_secret_key()
        )
        headers[GatePayConstants.HEADER_GATEPAY_SIGNATURE] = signature

        # 构建完整URL
        url = self.gate_pay_config.get_end_point() + request.get_api().get_url() + param_str

        # 创建并返回请求对象

        return httpx.Request(method=method, url=url, headers=headers)

    def _populate_builder_for_post_put(self, request: T, headers: dict, timestamp: int, nonce: str,
                                       method: str) -> httpx.Request:
        """
        填充http请求builder

        :param request: 请求对象
        :param headers: 请求头字典
        :param timestamp: 时间戳
        :param nonce: 随机字符串
        :param method: HTTP方法
        :return: HTTP请求对象
        :raises: JsonProcessingException
        """
        # 序列化请求对象为JSON

        if hasattr(request, 'to_dict'):
            camel_dict = request.to_dict()
            camel_request_json = json.dumps(camel_dict, separators=(',', ':'))
        else:
            # 回退到原来的处理方式
            from gatepay.common.utils.snake_camel_utils import CamelAndSnakeUtils
            nonce_request = CommonUtils.filter_none_recursive(request)

            camel_request_json = json.dumps(CamelAndSnakeUtils.convert_dict_keys(nonce_request), separators=(',', ':'))

        # 添加请求头
        headers[GatePayConstants.HEADER_GATEPAY_API_KEY] = self.gate_pay_config.get_credential().get_api_key()
        signature = Signature.verify_signature(
            str(timestamp),
            nonce,
            camel_request_json,
            self.gate_pay_config.get_credential().get_secret_key()
        )
        headers[GatePayConstants.HEADER_GATEPAY_SIGNATURE] = signature

        # 构建完整URL
        url = self.gate_pay_config.get_end_point() + request.get_api().get_url()

        # 创建并返回请求对象
        return httpx.Request(method=method, url=url, headers=headers, content=camel_request_json)

    def _has_gatepay_param_annotation(self, obj, field_name: str) -> bool:
        """
        检查字段是否有GatePayParam注解（辅助方法）
        注意：这是模拟Java注解的Python实现

        :param obj: 对象实例
        :param field_name: 字段名
        :return: 是否有注解
        """
        # 这里需要根据实际Python实现调整
        # 可以使用装饰器或其他方式标记字段
        # 简化处理，假设所有公共属性都需要处理
        return hasattr(obj, field_name) and not field_name.startswith('_')

    def get_http_client(self) -> httpx.Client:
        """
        获取HTTP客户端

        :return: HTTP客户端实例
        """
        return self.http_client

    def set_http_client(self, http_client: httpx.Client) -> None:
        """
        设置HTTP客户端

        :param http_client: HTTP客户端实例
        """
        self.http_client = http_client



