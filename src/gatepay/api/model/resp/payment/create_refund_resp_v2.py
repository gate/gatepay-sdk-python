from dataclasses import dataclass
from typing import Optional

from src.gatepay.base_response import BaseResponse


@dataclass
class CreateRefundRespV2(BaseResponse):
    """
    支付创建退款响应V2
    """
    refundRequestId: Optional[str] = None
    refundGateId: Optional[str] = None
    prepayId: Optional[str] = None
    orderAmount: Optional[str] = None
    refundAmount: Optional[str] = None
    errMsg: Optional[str] = None
    orderCurrency: Optional[str] = None
    payCurrency: Optional[str] = None
    payAmount: Optional[str] = None
