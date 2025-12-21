from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class CreateOrderResp:
    prepayId: Optional[str] = None
    terminalType: Optional[str] = None
    expireTime: int = 0
    qrContent: Optional[str] = None
    location: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateOrderResp':
        return cls(**data)
