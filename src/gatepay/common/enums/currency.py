

from enum import Enum


class Currency(Enum):

    USDT = "USDT"
    BTC = "BTC"
    ETH = "ETH"
    LTC = "LTC"
    BCH = "BCH"
    GT = "GT"

    def __init__(self, name: str):
        """
        初始化 Currency 枚举值

        :param name: 币种名称
        """
        self.name = name

    def get_name(self) -> str:
        """
        获取币种名称

        :return: 币种名称
        """
        return self.name
