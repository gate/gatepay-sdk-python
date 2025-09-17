from typing import Optional
from dataclasses import dataclass


@dataclass
class TxItem:

    chain: Optional[str] = None
    address: Optional[str] = None
    full_curr_type: Optional[str] = None
    amount: Optional[str] = None
    tx_id: Optional[str] = None
    utc_create_time: Optional[str] = None
    utc_update_time: Optional[str] = None

    def get_chain(self) -> Optional[str]:
        """
        获取链

        :return: 链
        """
        return self.chain

    def set_chain(self, chain: str) -> None:
        """
        设置链

        :param chain: 链
        """
        self.chain = chain

    def get_address(self) -> Optional[str]:
        """
        获取地址

        :return: 地址
        """
        return self.address

    def set_address(self, address: str) -> None:
        """
        设置地址

        :param address: 地址
        """
        self.address = address

    def get_full_curr_type(self) -> Optional[str]:
        """
        获取完整币种类型

        :return: 完整币种类型
        """
        return self.full_curr_type

    def set_full_curr_type(self, full_curr_type: str) -> None:
        """
        设置完整币种类型

        :param full_curr_type: 完整币种类型
        """
        self.full_curr_type = full_curr_type

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

    def get_tx_id(self) -> Optional[str]:
        """
        获取交易ID

        :return: 交易ID
        """
        return self.tx_id

    def set_tx_id(self, tx_id: str) -> None:
        """
        设置交易ID

        :param tx_id: 交易ID
        """
        self.tx_id = tx_id

    def get_utc_create_time(self) -> Optional[str]:
        """
        获取创建时间的UTC表达

        :return: 创建时间
        """
        return self.utc_create_time

    def set_utc_create_time(self, utc_create_time: str) -> None:
        """
        设置创建时间的UTC表达

        :param utc_create_time: 创建时间
        """
        self.utc_create_time = utc_create_time

    def get_utc_update_time(self) -> Optional[str]:
        """
        获取更新时间的UTC表达

        :return: 更新时间
        """
        return self.utc_update_time

    def set_utc_update_time(self, utc_update_time: str) -> None:
        """
        设置更新时间的UTC表达

        :param utc_update_time: 更新时间
        """
        self.utc_update_time = utc_update_time
