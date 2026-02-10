from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class QueryOrderResp:
    """
    查询订单响应
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
    totalFee: Optional[str] = None
    returnUrl: Optional[str] = None
    merchantName: Optional[str] = None
    location: Optional[str] = None
    scheme: Optional[str] = None
    whiteBrandInfo: Optional[Any] = None
    txHash: Optional[str] = None
    address: Optional[str] = None
    chain: Optional[str] = None
    fullCurrType: Optional[str] = None
    fromAddress: Optional[str] = None
    showChainNameEn: Optional[str] = None
    order_name: Optional[str] = None
    pay_currency: Optional[str] = None
    pay_amount: Optional[str] = None
    channel_type: Optional[str] = None
    pay_account: Optional[str] = None
    qrcode: Optional[str] = None
    transaction_info: Optional[Any] = None
    fiatCurrency: Optional[str] = None
    fiatAmount: Optional[str] = None
    fiatRate: Optional[str] = None
    toleranceAmount: Optional[str] = None
    underpaidAmount: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryOrderResp':
        """
        从字典创建QueryOrderResp实例

        Args:
            data: 包含订单响应信息的字典

        Returns:
            QueryOrderResp实例
        """
        return cls(**data)