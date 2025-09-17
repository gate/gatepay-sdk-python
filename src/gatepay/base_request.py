"""
Base req class for GatePay SDK
"""

from typing import Dict, Optional
from src.gatepay.common.enums.gatepay_api import GatePayApi


class BaseRequest:
    """
    基础请求类
    """

    def __init__(self, version: Optional[str] = None):
        self.api: Optional[GatePayApi] = None
        self.headers: Dict[str, str] = {}
        self.version: Optional[str] = version

    def get_api(self) -> Optional[GatePayApi]:
        return self.api

    def set_api(self, api: GatePayApi) -> None:
        self.api = api

    def set_headers(self, headers: Dict[str, str]) -> None:
        self.headers = headers

    def get_version(self) -> Optional[str]:
        return self.version

    def set_version(self, version: str) -> None:
        self.version = version

    def get_headers(self) -> Dict[str, str]:
        return self.headers

    def add_header(self, key: str, value: str) -> None:
        self.headers[key] = value

    def get_dicts(self) -> Dict[str, str]:
        result = {}

        # 添加父类字段
        if self.api is not None:
            result['api'] = self.api.name
        if self.headers:
            result['headers'] = self.headers
        if self.version is not None:
            result['version'] = self.version
        return result
