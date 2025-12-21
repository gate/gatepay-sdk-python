from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class QueryCurrencyResp:
    """
    查询可用闪兑币种
    """
    currency: Optional[List[str]] = None  # 币种列表

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryCurrencyResp':
        return cls(
            currency=data.get('currency')
        )