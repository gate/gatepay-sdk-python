

from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class ConfirmItem:
    amount: str = ""
    confirm: int = 0

@dataclass
class ChainTransactionInfo:
    done_amount: str = ""
    confirming_list: List[ConfirmItem] = field(default_factory=list)

@dataclass
class QueryOrderRespV2:
    """
    支付查询订单响应
    """

    prepayId: Optional[str] = None
    merchantId: int = 0
    merchantTradeNo: Optional[str] = None
    transactionId: Optional[str] = None
    goodsName: Optional[str] = None
    currency: Optional[str] = None
    orderAmount: Optional[str] = None
    surchargeAmount: Optional[str] = None
    status: Optional[str] = None
    createTime: int = 0
    expireTime: int = 0
    transactTime: int = 0
    expectCurrency: Optional[str] = None
    actualCurrency: Optional[str] = None
    actualAmount: Optional[str] = None
    rate: Optional[str] = None
    appName: Optional[str] = None
    appLogo: Optional[str] = None
    inUsdt: Optional[str] = None
    channelId: Optional[str] = None
    order_name: Optional[str] = None
    pay_currency: Optional[str] = None
    pay_amount: Optional[str] = None
    channel_type: Optional[str] = None
    pay_account: Optional[str] = None
    txHash: str = ""
    address: str = ""
    chain: str = ""
    fromAddress: str = ""
    transaction_info: Optional[ChainTransactionInfo] = None
    fiatCurrency: Optional[str] = None
    fiatAmount: Optional[str] = None
    fiatRate: Optional[str] = None
    toleranceAmount: Optional[str] = None
    underpaidAmount: Optional[str] = None