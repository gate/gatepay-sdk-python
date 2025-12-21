from dataclasses import dataclass
from typing import Optional


@dataclass
class QueryRefundRespV2:
    """
    退款查询响应 V2
    """
    # 商户退款订单号
    refundRequestId: Optional[str] = None

    # Gate退款订单号
    gateRefundId: Optional[str] = None

    # 商家退款订单号（发起退款的 refundRequestId）
    refundId: Optional[str] = None

    # GatePay支付订单号（原始正向订单的 orderId）
    orderId: Optional[str] = None

    # 商户订单号（原始正向订单的 merchantTradeNo）
    merchantTradeNo: Optional[str] = None

    # 退款单创建时间
    createTime: int = 0

    # 支付时间
    transactTime: int = 0

    # 支付流水订单号
    transactionId: Optional[str] = None

    # 交易hash
    txHash: str = ""

    # 订单金额
    orderAmount: Optional[str] = None

    # 订单币种
    orderCurrency: Optional[str] = None

    # 申请退款金额
    requestAmount: Optional[str] = None

    # 申请退款币种
    requestCurrency: Optional[str] = None

    # 退款金额
    amount: Optional[str] = None

    # 退款币种
    currency: Optional[str] = None

    # 退款状态
    status: Optional[str] = None

    # 退款订单备注
    remark: Optional[str] = None

    # 退款方式 1:原路退 2:指定退
    refund_style: int = 0

    # 退款支付方式 1:gate 2:web3
    refund_pay_channel: int = 0

    # 退款地址
    refund_address: Optional[str] = None

    # 退款网络
    refund_chain: Optional[str] = None

    # 退款承担类型 1:需商家承担，2:需用户承担
    refund_bear_type: int = 0

    # 退款金额类型 1:全部退 2:部分退
    refund_amount_type: int = 0

    # 退款扣款账户类型，1:支付账户 2:现货账户
    refund_account_type: int = 0

    # 退款手续费，只有退到web3有
    refund_gas_amount: Optional[str] = None

    # 退款失败原因
    refund_fail_reason: Optional[str] = None

    # 退款至gate用户uid
    refund_to_gate_uid: int = 0

    # 客户渠道名称
    channelId: Optional[str] = None

    # 用户昵称
    nickName: Optional[str] = None

    # 用户UID
    payerId: int = 0

    # 付款地址
    fromAddress: Optional[str] = None

    # 商品名称
    goodsName: Optional[str] = None

    # 订单维度-申请退款金额
    totalRequestAmount: Optional[str] = None

    # 订单维度-申请退款币种
    totalRequestCurrency: Optional[str] = None

    # 订单维度-实际到账订单金额
    totalReceiveAmount: Optional[str] = None

    # 订单维度-实际到账订单币种
    totalReceiveCurrency: Optional[str] = None
