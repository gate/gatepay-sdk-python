from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class CreateOrderResp:
    """
    创建订单响应
    """
    prepayId: Optional[str] = None
    terminalType: Optional[str] = None
    expireTime: int = 0

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateOrderResp':
        return cls(**data)
