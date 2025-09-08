from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class CreateRefundConvertReq(BaseRequest):

    # 商户请求退款编号
    refund_request_id: Optional[str] = None

    # 对应支付单订单id
    prepay_id: Optional[str] = None

    # 退款订单币种
    refund_order_currency: Optional[str] = None

    # 退款订单币种对应退款金额
    refund_order_amount: Optional[str] = None

    # 退款订单支付币种
    refund_pay_currency: Optional[str] = None

    # 退款订单支付币种对应退款金额
    refund_pay_amount: Optional[str] = None

    # 退款原因
    refund_reason: Optional[str] = None

    # 地址支付退款接收人在gate系统的user_id
    receiver_id: int = 0

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.ADDRESS_CREATE_REFUND_CONVERT

    def get_refund_request_id(self) -> Optional[str]:
        """
        获取商户请求退款编号

        :return: 商户请求退款编号
        """
        return self.refund_request_id

    def set_refund_request_id(self, refund_request_id: str) -> None:
        """
        设置商户请求退款编号

        :param refund_request_id: 商户请求退款编号
        """
        self.refund_request_id = refund_request_id

    def get_prepay_id(self) -> Optional[str]:
        """
        获取对应支付单订单id

        :return: 支付单订单id
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str) -> None:
        """
        设置对应支付单订单id

        :param prepay_id: 支付单订单id
        """
        self.prepay_id = prepay_id

    def get_refund_order_currency(self) -> Optional[str]:
        """
        获取退款订单币种

        :return: 退款订单币种
        """
        return self.refund_order_currency

    def set_refund_order_currency(self, refund_order_currency: str) -> None:
        """
        设置退款订单币种

        :param refund_order_currency: 退款订单币种
        """
        self.refund_order_currency = refund_order_currency

    def get_refund_order_amount(self) -> Optional[str]:
        """
        获取退款订单币种对应退款金额

        :return: 退款订单币种对应退款金额
        """
        return self.refund_order_amount

    def set_refund_order_amount(self, refund_order_amount: str) -> None:
        """
        设置退款订单币种对应退款金额

        :param refund_order_amount: 退款订单币种对应退款金额
        """
        self.refund_order_amount = refund_order_amount

    def get_refund_pay_currency(self) -> Optional[str]:
        """
        获取退款订单支付币种

        :return: 退款订单支付币种
        """
        return self.refund_pay_currency

    def set_refund_pay_currency(self, refund_pay_currency: str) -> None:
        """
        设置退款订单支付币种

        :param refund_pay_currency: 退款订单支付币种
        """
        self.refund_pay_currency = refund_pay_currency

    def get_refund_pay_amount(self) -> Optional[str]:
        """
        获取退款订单支付币种对应退款金额

        :return: 退款订单支付币种对应退款金额
        """
        return self.refund_pay_amount

    def set_refund_pay_amount(self, refund_pay_amount: str) -> None:
        """
        设置退款订单支付币种对应退款金额

        :param refund_pay_amount: 退款订单支付币种对应退款金额
        """
        self.refund_pay_amount = refund_pay_amount

    def get_refund_reason(self) -> Optional[str]:
        """
        获取退款原因

        :return: 退款原因
        """
        return self.refund_reason

    def set_refund_reason(self, refund_reason: str) -> None:
        """
        设置退款原因

        :param refund_reason: 退款原因
        """
        self.refund_reason = refund_reason

    def get_receiver_id(self) -> int:
        """
        获取地址支付退款接收人在gate系统的user_id

        :return: 接收人user_id
        """
        return self.receiver_id

    def set_receiver_id(self, receiver_id: int) -> None:
        """
        设置地址支付退款接收人在gate系统的user_id

        :param receiver_id: 接收人user_id
        """
        self.receiver_id = receiver_id
