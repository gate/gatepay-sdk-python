from typing import List, Optional
from dataclasses import dataclass

from gatepay.api.model.confirm_item import ConfirmItem


@dataclass
class ChainTransactionInfo:

    done_amount: Optional[str] = None
    confirming_list: Optional[List[ConfirmItem]] = None

    def get_done_amount(self) -> Optional[str]:
        """
        获取已完成的金额

        :return: 已完成的金额
        """
        return self.done_amount

    def set_done_amount(self, done_amount: str) -> None:
        """
        设置已完成的金额

        :param done_amount: 已完成的金额
        """
        self.done_amount = done_amount

    def get_confirming_list(self) -> Optional[List[ConfirmItem]]:
        """
        获取确认中的交易列表

        :return: 确认中的交易列表
        """
        return self.confirming_list

    def set_confirming_list(self, confirming_list: List[ConfirmItem]) -> None:
        """
        设置确认中的交易列表

        :param confirming_list: 确认中的交易列表
        """
        self.confirming_list = confirming_list
