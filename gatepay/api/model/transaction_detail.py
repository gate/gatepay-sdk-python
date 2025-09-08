from typing import Optional
from dataclasses import dataclass

from gatepay.api.model.tx_detail import TxDetail


@dataclass
class TransactionDetail:

    in_term: Optional[TxDetail] = None
    out_of_term: Optional[TxDetail] = None

    def get_in_term(self) -> Optional[TxDetail]:
        """
        获取入账详情

        :return: 入账详情
        """
        return self.in_term

    def set_in_term(self, in_term: TxDetail) -> None:
        """
        设置入账详情

        :param in_term: 入账详情
        """
        self.in_term = in_term

    def get_out_of_term(self) -> Optional[TxDetail]:
        """
        获取出账详情

        :return: 出账详情
        """
        return self.out_of_term

    def set_out_of_term(self, out_of_term: TxDetail) -> None:
        """
        设置出账详情

        :param out_of_term: 出账详情
        """
        self.out_of_term = out_of_term
