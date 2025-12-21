from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class CreateRefundResp:
    """
    创建退款响应
    """
    refundRequestId: Optional[str] = None  # 商户退款请求id
    prepayId: Optional[str] = None  # 拟退款的订单id
    orderAmount: Optional[str] = None  # 订单金额
    refundAmount: Optional[str] = None  # 退款金额

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateRefundResp':
        return cls(**data)