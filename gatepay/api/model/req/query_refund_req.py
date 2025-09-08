from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class QueryRefundReq(BaseRequest):

    # 退款请求ID
    refund_request_id: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.PAYMENT_QUERY_REFUND

    def get_refund_request_id(self) -> Optional[str]:
        """
        获取退款请求ID

        :return: 退款请求ID
        """
        return self.refund_request_id

    def set_refund_request_id(self, refund_request_id: str) -> None:
        """
        设置退款请求ID

        :param refund_request_id: 退款请求ID
        """
        self.refund_request_id = refund_request_id
