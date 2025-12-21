from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class PreviewResp:
    sellCurrency: Optional[str] = None  # 出售币种
    buyCurrency: Optional[str] = None  # 购买币种
    sellAmount: Optional[str] = None  # 出售数量
    buyAmount: Optional[str] = None  # 购买数量
    price: Optional[str] = None  # 价格
    quoteId: Optional[str] = None  # 报价id
    rate: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PreviewResp':
        return cls(**data)