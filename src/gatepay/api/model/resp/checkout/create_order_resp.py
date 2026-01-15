from dataclasses import dataclass
from typing import Optional, Dict, Any

from src.gatepay.api.model.chain import Chain


@dataclass
class CreateOrderResp:
    """
    创建订单响应
    """
    prepayId: Optional[str] = None
    orderAmount: Optional[str] = None
    surchargeAmount: Optional[str] = None
    terminalType: Optional[str] = None
    expireTime: int = 0
    qrContent: Optional[str] = None
    location: Optional[str] = None
    payCurrency: Optional[str] = None
    payAmount: Optional[str] = None
    chain: Optional['Chain'] = None
    appName: Optional[str] = None
    appLogo: Optional[str] = None
    goodsName: Optional[str] = None
    inUsdt: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateOrderResp':
        return cls(**data)