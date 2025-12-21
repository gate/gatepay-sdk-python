from dataclasses import dataclass
from typing import Optional, Dict, Any

from src.gatepay.api.model.transaction_detail import TransactionDetail


@dataclass
class TransactionDetailResp:
    """
    交易详情响应
    """
    prepayId: Optional[str] = None  # 支付单id
    merchantId: int = 0  # 用于申请商户账号的Gate UID
    merchantTradeNo: Optional[str] = None  # 商户系统交易号
    transactionId: Optional[str] = None  # 交易流水号
    goodsName: Optional[str] = None  # 商品名称
    currency: Optional[str] = None  # 订单币种
    orderAmount: Optional[str] = None  # 订单金额
    payCurrency: Optional[str] = None  # 用户实际支付币种
    payAmount: Optional[str] = None  # 订单对应用户实际支付币种的金额
    status: Optional[str] = None  # 订单状态
    utcCreateTime: Optional[str] = None  # 订单创建时间的utc表达，例如2023-01-07 14:04:02
    utcExpireTime: Optional[str] = None  # 订单过期时间的utc表达，例如2023-01-07 14:04:02
    utcUpdateTime: Optional[str] = None  # 订单状态更新时间的utc表达，例如2023-01-07 14:04:02
    transactTime: int = 0  # 订单在后台完成交易的UTC毫秒时间戳
    order_name: Optional[str] = None  # 订单名称
    transactionDetail: Optional['TransactionDetail'] = None  # 链上交易详情
    channelId: Optional[str] = None  # 客户名称

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TransactionDetailResp':
        return cls(**data)