from dataclasses import dataclass
from typing import Optional, List, Dict, Any

from src.gatepay.api.model.confirm_item import ConfirmItem
from src.gatepay.api.model.tx_item import TxItem


@dataclass
class ChainTransactionInfo:
    """
    链上交易信息
    """
    done_amount: Optional[str] = None
    done_amount_total: Optional[str] = None
    confirming_list: Optional[List['ConfirmItem']] = None
    done_tx_item_list: Optional[List['TxItem']] = None
    confirming_tx_item_list: Optional[List['TxItem']] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ChainTransactionInfo':
        # 处理列表字段
        confirming_list = None
        if 'confirming_list' in data and data['confirming_list']:
            confirming_list = [ConfirmItem.from_dict(item) for item in data['confirming_list']]

        done_tx_item_list = None
        if 'done_tx_item_list' in data and data['done_tx_item_list']:
            done_tx_item_list = [TxItem.from_dict(item) for item in data['done_tx_item_list']]

        confirming_tx_item_list = None
        if 'confirming_tx_item_list' in data and data['confirming_tx_item_list']:
            confirming_tx_item_list = [TxItem.from_dict(item) for item in data['confirming_tx_item_list']]

        return cls(
            done_amount=data.get('done_amount'),
            done_amount_total=data.get('done_amount_total'),
            confirming_list=confirming_list,
            done_tx_item_list=done_tx_item_list,
            confirming_tx_item_list=confirming_tx_item_list
        )