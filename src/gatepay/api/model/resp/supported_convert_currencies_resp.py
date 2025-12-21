from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class SupportedConvertCurrenciesResp:
    """
    支持的闪兑币种响应
    """
    currencies: Optional[List[str]] = None  # 支持的闪兑币种

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SupportedConvertCurrenciesResp':
        return cls(
            currencies=data.get('currencies')
        )