

from typing import Dict, Optional
from gatepay.common.enums.gatepay_api import GatePayApi


class BaseRequest:


    def __init__(self, version: Optional[str] = None):
        """
        初始化 BaseRequest 实例

        :param version: 版本号
        """
        self.api: Optional[GatePayApi] = None
        self.headers: Dict[str, str] = {}
        self.version: Optional[str] = version

    def get_api(self) -> Optional[GatePayApi]:
        """
        获取API信息

        :return: GatePayApi对象
        """
        return self.api

    def set_api(self, api: GatePayApi) -> None:
        """
        设置API信息

        :param api: GatePayApi对象
        """
        self.api = api

    def set_headers(self, headers: Dict[str, str]) -> None:
        """
        设置请求头

        :param headers: 请求头字典
        """
        self.headers = headers

    def get_version(self) -> Optional[str]:
        """
        获取版本号

        :return: 版本号
        """
        return self.version

    def set_version(self, version: str) -> None:
        """
        设置版本号

        :param version: 版本号
        """
        self.version = version

    def get_headers(self) -> Dict[str, str]:
        """
        获取请求头

        :return: 请求头字典
        """
        return self.headers

    def add_header(self, key: str, value: str) -> None:
        """
        添加请求头

        :param key: 请求头键
        :param value: 请求头值
        """
        if self.headers is None:
            self.headers = {}
        self.headers[key] = value
