from dataclasses import dataclass
from typing import Optional, Dict, Any

from src.gatepay.api.model.tx_detail import TxDetail


@dataclass
class TransactionDetail:

    in_term: Optional[TxDetail] = None
    out_of_term: Optional[TxDetail] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TransactionDetail':
        return cls(**data)