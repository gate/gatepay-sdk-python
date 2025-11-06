from typing import Optional
from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class PreviewResp(BaseResponse['PreviewResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 出售币种
    sell_currency: Optional[str] = None

    # 购买币种
    buy_currency: Optional[str] = None

    # 出售数量
    sell_amount: Optional[str] = None

    # 购买数量
    buy_amount: Optional[str] = None

    # 价格
    price: Optional[str] = None

    # 报价id
    quote_id: Optional[str] = None

    rate: Optional[str] = None

    def get_sell_currency(self) -> Optional[str]:
        """
        获取出售币种

        :return: 出售币种
        """
        return self.sell_currency

    def set_sell_currency(self, sell_currency: str) -> None:
        """
        设置出售币种

        :param sell_currency: 出售币种
        """
        self.sell_currency = sell_currency

    def get_buy_currency(self) -> Optional[str]:
        """
        获取购买币种

        :return: 购买币种
        """
        return self.buy_currency

    def set_buy_currency(self, buy_currency: str) -> None:
        """
        设置购买币种

        :param buy_currency: 购买币种
        """
        self.buy_currency = buy_currency

    def get_sell_amount(self) -> Optional[str]:
        """
        获取出售数量

        :return: 出售数量
        """
        return self.sell_amount

    def set_sell_amount(self, sell_amount: str) -> None:
        """
        设置出售数量

        :param sell_amount: 出售数量
        """
        self.sell_amount = sell_amount

    def get_buy_amount(self) -> Optional[str]:
        """
        获取购买数量

        :return: 购买数量
        """
        return self.buy_amount

    def set_buy_amount(self, buy_amount: str) -> None:
        """
        设置购买数量

        :param buy_amount: 购买数量
        """
        self.buy_amount = buy_amount

    def get_price(self) -> Optional[str]:
        """
        获取价格

        :return: 价格
        """
        return self.price

    def set_price(self, price: str) -> None:
        """
        设置价格

        :param price: 价格
        """
        self.price = price

    def get_quote_id(self) -> Optional[str]:
        """
        获取报价id

        :return: 报价id
        """
        return self.quote_id

    def set_quote_id(self, quote_id: str) -> None:
        """
        设置报价id

        :param quote_id: 报价id
        """
        self.quote_id = quote_id

    def get_rate(self) -> Optional[str]:
        """
        获取汇率

        :return: 汇率
        """
        return self.rate

    def set_rate(self, rate: str) -> None:
        """
        设置汇率

        :param rate: 汇率
        """
        self.rate = rate
