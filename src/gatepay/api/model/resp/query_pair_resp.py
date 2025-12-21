from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class QueryPairResp:
    """
    查询可用币种对响应
    """
    pair: Optional[str] = None
    sellCurrency: Optional[str] = None
    sellCurrencyMax: Optional[str] = None
    sellCurrencyMin: Optional[str] = None
    buyCurrency: Optional[str] = None
    buyCurrencyMax: Optional[str] = None
    buyCurrencyMin: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryPairResp':
        return cls(**data)