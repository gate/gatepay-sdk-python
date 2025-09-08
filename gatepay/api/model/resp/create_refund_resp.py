from typing import Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class CreateRefundResp(BaseResponse['CreateRefundResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 商户退款请求id
    refund_request_id: Optional[str] = None

    # 拟退款的订单id
    prepay_id: Optional[str] = None

    # 订单金额
    order_amount: Optional[str] = None

    # 退款金额
    refund_amount: Optional[str] = None

    def get_refund_request_id(self) -> Optional[str]:
        """
        获取商户退款请求id

        :return: 商户退款请求id
        """
        return self.refund_request_id

    def set_refund_request_id(self, refund_request_id: str) -> None:
        """
        设置商户退款请求id

        :param refund_request_id: 商户退款请求id
        """
        self.refund_request_id = refund_request_id

    def get_prepay_id(self) -> Optional[str]:
        """
        获取拟退款的订单id

        :return: 订单id
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str) -> None:
        """
        设置拟退款的订单id

        :param prepay_id: 订单id
        """
        self.prepay_id = prepay_id

    def get_order_amount(self) -> Optional[str]:
        """
        获取订单金额

        :return: 订单金额
        """
        return self.order_amount

    def set_order_amount(self, order_amount: str) -> None:
        """
        设置订单金额

        :param order_amount: 订单金额
        """
        self.order_amount = order_amount

    def get_refund_amount(self) -> Optional[str]:
        """
        获取退款金额

        :return: 退款金额
        """
        return self.refund_amount

    def set_refund_amount(self, refund_amount: str) -> None:
        """
        设置退款金额

        :param refund_amount: 退款金额
        """
        self.refund_amount = refund_amount
