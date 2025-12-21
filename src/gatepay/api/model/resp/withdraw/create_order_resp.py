from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class CreateOrderResp:
    """
    创建订单响应
    """
    batch_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateOrderResp':
        return cls(**data)