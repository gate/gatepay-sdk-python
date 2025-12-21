from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class QueryRefundResp:
    """
    查询退款响应
    """
    refundRequestId: Optional[str] = None  # 商户退款单id，有商户后端生成保证唯一
    prepayId: Optional[str] = None  # 订单id，GatePay后端生成
    orderAmount: Optional[str] = None  # 订单金额
    refundAmount: Optional[str] = None  # 退款金额
    refundStatus: Optional[str] = None  # 退款单状态 SUCCESS:退款成功 FAIL:退款失败
    channelId: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryRefundResp':
        """
        从字典创建QueryRefundResp实例

        Args:
            data: 包含退款响应信息的字典

        Returns:
            QueryRefundResp实例
        """
        return cls(
            refundRequestId=data.get('refundRequestId'),
            prepayId=data.get('prepayId'),
            orderAmount=data.get('orderAmount'),
            refundAmount=data.get('refundAmount'),
            refundStatus=data.get('refundStatus'),
            channelId=data.get('channelId')
        )