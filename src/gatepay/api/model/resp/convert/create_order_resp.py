from dataclasses import dataclass
from typing import Optional, Dict, Any
from decimal import Decimal


@dataclass
class CreateOrderResp:
    """
    闪兑下单响应
    """
    order_id: Optional[str] = None  # 订单ID
    userId: int = 0  # 用户ID
    sellCurrency: Optional[str] = None  # 出售币种
    buyCurrency: Optional[str] = None  # 购买币种
    sellAmount: Optional[str] = None  # 出售数量
    buyAmount: Optional[str] = None  # 购买数量
    status: int = 0  # 状态 1 - 创建成功 3 - 成功 6 - 失败
    rate: Optional[Decimal] = None  # 价格
    quoteId: Optional[str] = None  # 报价ID
    createTime: int = 0  # 创建时间

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateOrderResp':
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
            status=data.get('status', 0),
            rate=rate,
            quoteId=data.get('quoteId'),
            createTime=data.get('createTime', 0)
        )