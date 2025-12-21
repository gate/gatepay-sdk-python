from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class CloseOrderResp:
    """
    关闭订单响应
    """
    result: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CloseOrderResp':
        return cls(**data)
