from typing import List, Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class QueryCurrencyResp(BaseResponse['QueryCurrencyResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 币种列表
    currency: Optional[List[str]] = None

    def get_currency(self) -> Optional[List[str]]:
        """
        获取币种列表

        :return: 币种列表
        """
        return self.currency

    def set_currency(self, currency: List[str]) -> None:
        """
        设置币种列表

        :param currency: 币种列表
        """
        self.currency = currency
