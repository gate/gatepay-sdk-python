from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class BalanceHistoryItem:
    """
    余额历史记录项
    """
    transactId: Optional[str] = None  # 支付流水单号
    transactTime: int = 0  # 入账时间，毫秒时间戳
    orderId: Optional[str] = None  # GatePay订单号
    merchantTradeNo: Optional[str] = None  # 商户订单号
    financialType: Optional[str] = None  # 财务类型
    payAmount: Optional[str] = None  # 收支金额
    currency: Optional[str] = None  # 收支币种
    balance: Optional[str] = None  # 账户余额
    balanceCurrency: Optional[str] = None  # 账户余额币种
    status: Optional[str] = None  # PAID表示成功
    payer: int = 0  # Gate支付付款用户UID
    buyer: Optional[str] = None  # 对方信息: Web3支付该值为付款地址，非Web3支付为付款人UID
    refund_gate_id: Optional[str] = None  # 退款订单ID
    payChannel: Optional[str] = None  # 支付方式: Web3 支付, Gate 支付
    fullChain: Optional[str] = None  # 支付网络全称
    address: Optional[str] = None  # 商家收款地址
    hash: Optional[str] = None  # 交易hash

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BalanceHistoryItem':
        return cls(**data)


@dataclass
class QueryOrdersResp:
    """
    查询订单响应
    """
    merchant_id: int = 0
    total: int = 0
    hasNext: bool = False
    nextPage: int = 0
    balance_history_item_list: Optional[List[BalanceHistoryItem]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryOrdersResp':
        balance_items = None
        if 'balance_history_item_list' in data and data['balance_history_item_list']:
            balance_items = [BalanceHistoryItem.from_dict(item_data) for item_data in data['balance_history_item_list']]

        return cls(
            merchant_id=data.get('merchant_id', 0),
            total=data.get('total', 0),
            hasNext=data.get('hasNext', False),
            nextPage=data.get('nextPage', 0),
            balance_history_item_list=balance_items
        )