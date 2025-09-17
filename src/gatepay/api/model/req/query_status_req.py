from dataclasses import dataclass
from typing import Optional

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class QueryStatusReq(BaseRequest):


    # 币种
    currency: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.WITHDRAW_QUERY_STATUS

    def get_currency(self) -> Optional[str]:
        """
        获取币种

        :return: 币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置币种

        :param currency: 币种
        """
        self.currency = currency
