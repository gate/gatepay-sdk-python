from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class QueryPairReq(BaseRequest):

    currency: Optional[str] = None
    side: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.CONVERT_PAIR

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

    def get_side(self) -> Optional[str]:
        """
        获取方向

        :return: 方向
        """
        return self.side

    def set_side(self, side: str) -> None:
        """
        设置方向

        :param side: 方向
        """
        self.side = side
