from dataclasses import dataclass
from typing import Optional, Dict, Any

from src.gatepay.api.model.chain_transaction_info import ChainTransactionInfo


@dataclass
class QueryOrderResp:
    """
    订单查询响应
    """
    prepayId: Optional[str] = None  # 支付单单号
    merchantId: int = 0  # 用于申请商户账号的Gate UID
    merchantTradeNo: Optional[str] = None  # 商户系统交易号
    transactionId: Optional[str] = None  # 交易流水号
    goodsName: Optional[str] = None  # 商品名，商户创建订单时提供
    currency: Optional[str] = None  # 订单币种
    orderAmount: Optional[str] = None  # 订单金额
    surchargeAmount: Optional[str] = None
    payCurrency: Optional[str] = None  # 用户实际支付币种，非闪兑单中与订单币种一致
    payAmount: Optional[str] = None  # 用户应该支付的金额
    rate: Optional[str] = None  # 订单币种到用户支付币种的汇率，例如，1BTC换20000USDT
    status: Optional[str] = None  # 订单状态，PENDING处理中，PROCESS订单有效期内支付足够金额但链上未确认完毕，PAID订单支付成功，EXPIRED订单已过期
    createTime: int = 0  # 订单的创建时间
    expireTime: int = 0  # 订单的过期时间
    transactTime: int = 0  # 订单在Gate内部交易发生时间
    order_name: Optional[str] = None  # 订单名称
    transaction_info: Optional['ChainTransactionInfo'] = None  # 订单在链上交易情况总览
    channelId: Optional[str] = None  # 客户名称
    address: Optional[str] = None  # 收款地址
    chain: Optional[str] = None  # 网络
    fromAddress: Optional[str] = None  # 来源地址

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryOrderResp':
        return cls(**data)