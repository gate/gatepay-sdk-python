from typing import Optional
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ConfirmItem:
    """
    确认项类，用于表示链上交易的确认信息
    """

    amount: Optional[Decimal] = None
    confirm: int = 0

    def get_amount(self) -> Optional[Decimal]:
        """
        获取金额

        :return: 金额
        """
        return self.amount

    def set_amount(self, amount: Decimal) -> None:
        """
        设置金额

        :param amount: 金额
        """
        self.amount = amount

    def get_confirm(self) -> int:
        """
        获取确认数

        :return: 确认数
        """
        return self.confirm

    def set_confirm(self, confirm: int) -> None:
        """
        设置确认数

        :param confirm: 确认数
        """
        self.confirm = confirm
