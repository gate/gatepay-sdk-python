from typing import Optional
from dataclasses import dataclass
from decimal import Decimal

from gatepay.base_response import BaseResponse


@dataclass
class CreateRefundConvertResp(BaseResponse):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 商户退款请求id
    refund_request_id: Optional[str] = None

    # 拟退款的订单id
    prepay_id: Optional[str] = None

    # 订单币种
    order_currency: Optional[str] = None

    # 订单金额
    order_amount: Optional[Decimal] = None

    # 对应订单币种的退款金额
    refund_order_amount: Optional[Decimal] = None

    # 用户支付币种
    pay_currency: Optional[str] = None

    # 订单中用户应该支付的金额
    pay_amount: Optional[Decimal] = None

    # 对应订单用户支付币种的退款金额
    refund_pay_amount: Optional[Decimal] = None

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

    def get_order_currency(self) -> Optional[str]:
        """
        获取订单币种

        :return: 订单币种
        """
        return self.order_currency

    def set_order_currency(self, order_currency: str) -> None:
        """
        设置订单币种

        :param order_currency: 订单币种
        """
        self.order_currency = order_currency

    def get_order_amount(self) -> Optional[Decimal]:
        """
        获取订单金额

        :return: 订单金额
        """
        return self.order_amount

    def set_order_amount(self, order_amount: Decimal) -> None:
        """
        设置订单金额

        :param order_amount: 订单金额
        """
        self.order_amount = order_amount

    def get_refund_order_amount(self) -> Optional[Decimal]:
        """
        获取对应订单币种的退款金额

        :return: 退款金额
        """
        return self.refund_order_amount

    def set_refund_order_amount(self, refund_order_amount: Decimal) -> None:
        """
        设置对应订单币种的退款金额

        :param refund_order_amount: 退款金额
        """
        self.refund_order_amount = refund_order_amount

    def get_pay_currency(self) -> Optional[str]:
        """
        获取用户支付币种

        :return: 支付币种
        """
        return self.pay_currency

    def set_pay_currency(self, pay_currency: str) -> None:
        """
        设置用户支付币种

        :param pay_currency: 支付币种
        """
        self.pay_currency = pay_currency

    def get_pay_amount(self) -> Optional[Decimal]:
        """
        获取订单中用户应该支付的金额

        :return: 支付金额
        """
        return self.pay_amount

    def set_pay_amount(self, pay_amount: Decimal) -> None:
        """
        设置订单中用户应该支付的金额

        :param pay_amount: 支付金额
        """
        self.pay_amount = pay_amount

    def get_refund_pay_amount(self) -> Optional[Decimal]:
        """
        获取对应订单用户支付币种的退款金额

        :return: 退款金额
        """
        return self.refund_pay_amount

    def set_refund_pay_amount(self, refund_pay_amount: Decimal) -> None:
        """
        设置对应订单用户支付币种的退款金额

        :param refund_pay_amount: 退款金额
        """
        self.refund_pay_amount = refund_pay_amount
