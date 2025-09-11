from typing import Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class QueryRefundResp(BaseResponse['QueryRefundResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 商户退款单id，有商户后端生成保证唯一
    refund_request_id: Optional[str] = None

    # 订单id，GatePay后端生成
    prepay_id: Optional[str] = None

    # 订单金额
    order_amount: Optional[str] = None

    # 退款金额
    refund_amount: Optional[str] = None

    # 退款单状态 SUCCESS:退款成功 FAIL:退款失败
    refund_status: Optional[str] = None

    channel_id: Optional[str] = None

    def get_refund_request_id(self) -> Optional[str]:
        """
        获取商户退款单id

        :return: 商户退款单id
        """
        return self.refund_request_id

    def set_refund_request_id(self, refund_request_id: str) -> None:
        """
        设置商户退款单id

        :param refund_request_id: 商户退款单id
        """
        self.refund_request_id = refund_request_id

    def get_prepay_id(self) -> Optional[str]:
        """
        获取订单id

        :return: 订单id
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str) -> None:
        """
        设置订单id

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

    def get_refund_status(self) -> Optional[str]:
        """
        获取退款单状态
        SUCCESS:退款成功 FAIL:退款失败

        :return: 退款单状态
        """
        return self.refund_status

    def set_refund_status(self, refund_status: str) -> None:
        """
        设置退款单状态
        SUCCESS:退款成功 FAIL:退款失败

        :param refund_status: 退款单状态
        """
        self.refund_status = refund_status

    def get_channel_id(self) -> Optional[str]:
        """
        获取渠道ID

        :return: 渠道ID
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str) -> None:
        """
        设置渠道ID

        :param channel_id: 渠道ID
        """
        self.channel_id = channel_id
