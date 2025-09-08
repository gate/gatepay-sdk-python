from typing import Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class CloseOrderResp(BaseResponse['CloseOrderResp']):

    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    result: Optional[str] = None

    def get_result(self) -> Optional[str]:
        """
        获取结果

        :return: 结果
        """
        return self.result

    def set_result(self, result: str) -> None:
        """
        设置结果

        :param result: 结果
        """
        self.result = result
