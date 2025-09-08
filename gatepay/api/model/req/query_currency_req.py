from dataclasses import dataclass
from typing import Optional

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class QueryCurrencyReq(BaseRequest):

    side: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.CONVERT_CURRENCY

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
