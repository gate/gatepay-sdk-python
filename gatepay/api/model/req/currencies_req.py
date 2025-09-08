from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class CurrenciesReq(BaseRequest):

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.ADDRESS_CURRENCIES
