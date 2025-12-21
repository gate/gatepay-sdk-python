from dataclasses import dataclass
from typing import Optional, Dict, Any
from decimal import Decimal


@dataclass
class CreateRefundConvertResp:
    """
    创建闪兑退款响应
    """
    refundRequestId: Optional[str] = None  # 商户退款请求id
    prepayId: Optional[str] = None  # 拟退款的订单id
    orderCurrency: Optional[str] = None  # 订单币种
    orderAmount: Optional[Decimal] = None  # 订单金额
    refundOrderAmount: Optional[Decimal] = None  # 对应订单币种的退款金额
    payCurrency: Optional[str] = None  # 用户支付币种
    payAmount: Optional[Decimal] = None  # 订单中用户应该支付的金额
    refundPayAmount: Optional[Decimal] = None  # 对应订单用户支付币种的退款金额

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateRefundConvertResp':
        # 处理BigDecimal字段
        order_amount = data.get('orderAmount')
        if order_amount is not None and not isinstance(order_amount, Decimal):
            order_amount = Decimal(str(order_amount))

        refund_order_amount = data.get('refundOrderAmount')
        if refund_order_amount is not None and not isinstance(refund_order_amount, Decimal):
            refund_order_amount = Decimal(str(refund_order_amount))

        pay_amount = data.get('payAmount')
        if pay_amount is not None and not isinstance(pay_amount, Decimal):
            pay_amount = Decimal(str(pay_amount))

        refund_pay_amount = data.get('refundPayAmount')
        if refund_pay_amount is not None and not isinstance(refund_pay_amount, Decimal):
            refund_pay_amount = Decimal(str(refund_pay_amount))

        return cls(
            refundRequestId=data.get('refundRequestId'),
            prepayId=data.get('prepayId'),
            orderCurrency=data.get('orderCurrency'),
            orderAmount=order_amount,
            refundOrderAmount=refund_order_amount,
            payCurrency=data.get('payCurrency'),
            payAmount=pay_amount,
            refundPayAmount=refund_pay_amount
        )