from typing import Optional
from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class QueryPairResp(BaseResponse['QueryPairResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    pair: Optional[str] = None
    sell_currency: Optional[str] = None
    sell_currency_max: Optional[str] = None
    sell_currency_min: Optional[str] = None
    buy_currency: Optional[str] = None
    buy_currency_max: Optional[str] = None
    buy_currency_min: Optional[str] = None

    def get_pair(self) -> Optional[str]:
        """
        获取币种对

        :return: 币种对
        """
        return self.pair

    def set_pair(self, pair: str) -> None:
        """
        设置币种对

        :param pair: 币种对
        """
        self.pair = pair

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

    def get_sell_currency_max(self) -> Optional[str]:
        """
        获取卖出币种最大值

        :return: 卖出币种最大值
        """
        return self.sell_currency_max

    def set_sell_currency_max(self, sell_currency_max: str) -> None:
        """
        设置卖出币种最大值

        :param sell_currency_max: 卖出币种最大值
        """
        self.sell_currency_max = sell_currency_max

    def get_sell_currency_min(self) -> Optional[str]:
        """
        获取卖出币种最小值

        :return: 卖出币种最小值
        """
        return self.sell_currency_min

    def set_sell_currency_min(self, sell_currency_min: str) -> None:
        """
        设置卖出币种最小值

        :param sell_currency_min: 卖出币种最小值
        """
        self.sell_currency_min = sell_currency_min

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

    def get_buy_currency_max(self) -> Optional[str]:
        """
        获取买入币种最大值

        :return: 买入币种最大值
        """
        return self.buy_currency_max

    def set_buy_currency_max(self, buy_currency_max: str) -> None:
        """
        设置买入币种最大值

        :param buy_currency_max: 买入币种最大值
        """
        self.buy_currency_max = buy_currency_max

    def get_buy_currency_min(self) -> Optional[str]:
        """
        获取买入币种最小值

        :return: 买入币种最小值
        """
        return self.buy_currency_min

    def set_buy_currency_min(self, buy_currency_min: str) -> None:
        """
        设置买入币种最小值

        :param buy_currency_min: 买入币种最小值
        """
        self.buy_currency_min = buy_currency_min
