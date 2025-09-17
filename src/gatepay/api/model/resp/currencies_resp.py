from typing import List, Optional
from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class CurrenciesResp(BaseResponse['CurrenciesResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 可选支付币种列表
    currencies: Optional[List[str]] = None

    def get_currencies(self) -> Optional[List[str]]:
        """
        获取可选支付币种列表

        :return: 币种列表
        """
        return self.currencies

    def set_currencies(self, currencies: List[str]) -> None:
        """
        设置可选支付币种列表

        :param currencies: 币种列表
        """
        self.currencies = currencies
