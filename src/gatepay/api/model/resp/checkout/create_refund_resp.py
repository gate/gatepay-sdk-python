from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class CreateRefundResp:
    """
    创建退款响应
    """
    refundRequestId: Optional[str] = None  # 商户退款请求id
    prepayId: Optional[str] = None  # 拟退款的订单id
    orderCurrency: Optional[str] = None  # 订单币种
    orderAmount: Optional[str] = None  # 订单金额
    refundOrderAmount: Optional[str] = None  # 退款商户已收到的用户支付的全部金额
    payCurrency: Optional[str] = None  # 用户支付币种
    payAmount: Optional[str] = None  # 订单中用户应该支付的金额
    refundPayAmount: Optional[str] = None  # 用户支付后，退款残留于链上的金额。商户没有收到这部分资金（闪兑场景）

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateRefundResp':
        return cls(**data)