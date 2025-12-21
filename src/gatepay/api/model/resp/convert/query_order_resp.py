from dataclasses import dataclass
from typing import Optional, Dict, Any
from decimal import Decimal


@dataclass
class QueryOrderResp:
    """
    查询闪兑订单
    """
    order_id: Optional[str] = None
    userId: int = 0
    sellCurrency: Optional[str] = None
    buyCurrency: Optional[str] = None
    sellAmount: Optional[str] = None
    buyAmount: Optional[str] = None
    status_: int = 0  # 注意：这里是status_而不是status，因为Java中有getStatus_()方法
    rate: Optional[Decimal] = None
    quoteId: Optional[str] = None
    createTime: int = 0

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryOrderResp':
        # 处理rate字段，可能是字符串或数字
        rate = data.get('rate')
        if rate is not None and not isinstance(rate, Decimal):
            rate = Decimal(str(rate))

        return cls(
            order_id=data.get('order_id'),
            userId=data.get('userId', 0),
            sellCurrency=data.get('sellCurrency'),
            buyCurrency=data.get('buyCurrency'),
            sellAmount=data.get('sellAmount'),
            buyAmount=data.get('buyAmount'),
            status_=data.get('status', 0),
            rate=rate,
            quoteId=data.get('quoteId'),
            createTime=data.get('createTime', 0)
        )