

from datetime import timedelta

from gatepay.common.gatepay_constants import GatePayConstants
from gatepay.infrastructure.credential import Credential


class GatePayConfig:

    def __init__(self, end_point: str, timeout_in_seconds: int, client_id: str, credential: Credential):
        """
        初始化 GatePayConfig 实例

        :param end_point: 端点地址
        :param timeout_in_seconds: 超时时间（秒）
        :param client_id: 客户端ID
        :param credential: 凭证信息
        """
        self.scheme = GatePayConstants.SCHEME_HTTPS
        self.end_point = end_point
        self.timeout = timedelta(seconds=timeout_in_seconds)
        self.client_id = client_id
        self.credential = credential

    def __init__(self, end_point: str, timeout_in_seconds: int, client_id: str,client_type: str, credential: Credential):
        """
        初始化 GatePayConfig 实例

        :param end_point: 端点地址
        :param timeout_in_seconds: 超时时间（秒）
        :param client_id: 客户端ID
        :param client_type: 客户端类型
        :param credential: 凭证信息
        """
        self.scheme = GatePayConstants.SCHEME_HTTPS
        self.end_point = end_point
        self.timeout = timedelta(seconds=timeout_in_seconds)
        self.client_id = client_id
        self.client_type = client_type
        self.credential = credential

    def get_scheme(self) -> str:
        """
        获取协议方案

        :return: 协议方案 (如: https)
        """
        return self.scheme

    def set_scheme(self, scheme: str) -> None:
        """
        设置协议方案

        :param scheme: 协议方案
        """
        self.scheme = scheme

    def get_end_point(self) -> str:
        """
        获取端点地址

        :return: 端点地址
        """
        return self.end_point

    def set_end_point(self, end_point: str) -> None:
        """
        设置端点地址

        :param end_point: 端点地址
        """
        self.end_point = end_point

    def get_timeout(self) -> timedelta:
        """
        获取超时时间

        :return: 超时时间
        """
        return self.timeout

    def set_timeout(self, timeout: timedelta) -> None:
        """
        设置超时时间

        :param timeout: 超时时间
        """
        self.timeout = timeout

    def get_client_id(self) -> str:
        """
        获取客户端ID

        :return: 客户端ID
        """
        return self.client_id

    def set_client_id(self, client_id: str) -> None:
        """
        设置客户端ID

        :param client_id: 客户端ID
        """
        self.client_id = client_id

    def get_client_type(self) -> str:
        """
        获取客户端类型

        :return: 客户端类型
        """
        return self.client_type

    def set_client_type(self, client_type: str) -> None:
        """
        设置客户端ID

        :param client_type: 客户端类型
        """
        self.client_type = client_type

    def get_credential(self) -> Credential:
        """
        获取凭证信息

        :return: 凭证信息
        """
        return self.credential

    def set_credential(self, credential: Credential) -> None:
        """
        设置凭证信息

        :param credential: 凭证信息
        """
        self.credential = credential
