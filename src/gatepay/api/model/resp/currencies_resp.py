from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class CurrenciesResp:
    currencies: Optional[List[str]] = None  # 支持的闪兑币种

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CurrenciesResp':
        return cls(
            currencies=data.get('currencies')
        )
