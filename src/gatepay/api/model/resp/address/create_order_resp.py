from dataclasses import dataclass
from typing import Optional, Dict, Any

from src.gatepay.api.model.chain import Chain


@dataclass
class CreateOrderResp:
    """
    创建订单响应
    """
    prepayId: Optional[str] = None  # 创建的支付单order id
    terminalType: Optional[str] = None  # 创建订单的终端类型
    expireTime: int = 0  # 过期毫秒时间戳
    chain: Optional['Chain'] = None  # 地址支付支付单绑定的链和地址

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateOrderResp':
        return cls(**data)