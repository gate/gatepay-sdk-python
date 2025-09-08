from typing import List, Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class SupportedConvertCurrenciesResp(BaseResponse['SupportedConvertCurrenciesResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 支持的闪兑币种
    currencies: Optional[List[str]] = None

    def get_currencies(self) -> Optional[List[str]]:
        """
        获取支持的闪兑币种

        :return: 闪兑币种列表
        """
        return self.currencies

    def set_currencies(self, currencies: List[str]) -> None:
        """
        设置支持的闪兑币种

        :param currencies: 闪兑币种列表
        """
        self.currencies = currencies
