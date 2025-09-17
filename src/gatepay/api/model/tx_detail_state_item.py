from typing import List, Optional
from dataclasses import dataclass

from src.gatepay.api.model.tx_item import TxItem


@dataclass
class TxDetailStateItem:
    """
    交易详情状态项
    """

    amount: Optional[str] = None
    tx_list: Optional[List[TxItem]] = None

    def get_amount(self) -> Optional[str]:
        """
        获取金额

        :return: 金额
        """
        return self.amount

    def set_amount(self, amount: str) -> None:
        """
        设置金额

        :param amount: 金额
        """
        self.amount = amount

    def get_tx_list(self) -> Optional[List[TxItem]]:
        """
        获取交易列表

        :return: 交易列表
        """
        return self.tx_list

    def set_tx_list(self, tx_list: List[TxItem]) -> None:
        """
        设置交易列表

        :param tx_list: 交易列表
        """
        self.tx_list = tx_list
