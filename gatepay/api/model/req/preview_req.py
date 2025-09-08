from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class PreviewReq(BaseRequest):

    buy_currency: Optional[str] = None
    buy_amount: Optional[str] = None
    sell_currency: Optional[str] = None
    sell_amount: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.CONVERT_PREVIEW

    def get_buy_currency(self) -> Optional[str]:
        """
        获取买入币种

        :return: 买入币种
        """
        return self.buy_currency

    def set_buy_currency(self, buy_currency: str) -> None:
        """
        设置买入币种

        :param buy_currency: 买入币种
        """
        self.buy_currency = buy_currency

    def get_buy_amount(self) -> Optional[str]:
        """
        获取买入金额

        :return: 买入金额
        """
        return self.buy_amount

    def set_buy_amount(self, buy_amount: str) -> None:
        """
        设置买入金额

        :param buy_amount: 买入金额
        """
        self.buy_amount = buy_amount

    def get_sell_currency(self) -> Optional[str]:
        """
        获取卖出币种

        :return: 卖出币种
        """
        return self.sell_currency

    def set_sell_currency(self, sell_currency: str) -> None:
        """
        设置卖出币种

        :param sell_currency: 卖出币种
        """
        self.sell_currency = sell_currency

    def get_sell_amount(self) -> Optional[str]:
        """
        获取卖出金额

        :return: 卖出金额
        """
        return self.sell_amount

    def set_sell_amount(self, sell_amount: str) -> None:
        """
        设置卖出金额

        :param sell_amount: 卖出金额
        """
        self.sell_amount = sell_amount
