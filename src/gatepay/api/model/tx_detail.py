from typing import Optional
from dataclasses import dataclass

from src.gatepay.api.model.tx_detail_state_item import TxDetailStateItem


@dataclass
class TxDetail:

    done: Optional[TxDetailStateItem] = None
    wait: Optional[TxDetailStateItem] = None

    def get_done(self) -> Optional[TxDetailStateItem]:
        """
        获取已完成的交易详情状态项

        :return: 已完成的交易详情状态项
        """
        return self.done

    def set_done(self, done: TxDetailStateItem) -> None:
        """
        设置已完成的交易详情状态项

        :param done: 已完成的交易详情状态项
        """
        self.done = done

    def get_wait(self) -> Optional[TxDetailStateItem]:
        """
        获取待处理的交易详情状态项

        :return: 待处理的交易详情状态项
        """
        return self.wait

    def set_wait(self, wait: TxDetailStateItem) -> None:
        """
        设置待处理的交易详情状态项

        :param wait: 待处理的交易详情状态项
        """
        self.wait = wait
