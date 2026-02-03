from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class CreateRefundRespV3(BaseResponse):
    """
    支付创建退款响应V3
    """

    def __init__(self):
        super().__init__()
        self.refund_request_id = ""
        self.refund_gate_id = ""
        self.prepay_id = ""
        self.order_amount = ""
        self.refund_amount = ""
        self.err_msg = ""
        self.order_currency = ""
        self.pay_currency = ""
        self.pay_amount = ""

    # refund_request_id getter and setter
    def get_refund_request_id(self):
        return self.refund_request_id

    def set_refund_request_id(self, value):
        self.refund_request_id = value

    # refund_gate_id getter and setter
    def get_refund_gate_id(self):
        return self.refund_gate_id

    def set_refund_gate_id(self, value):
        self.refund_gate_id = value

    # prepay_id getter and setter
    def get_prepay_id(self):
        return self.prepay_id

    def set_prepay_id(self, value):
        self.prepay_id = value

    # order_amount getter and setter
    def get_order_amount(self):
        return self.order_amount

    def set_order_amount(self, value):
        self.order_amount = value

    # refund_amount getter and setter
    def get_refund_amount(self):
        return self.refund_amount

    def set_refund_amount(self, value):
        self.refund_amount = value

    # err_msg getter and setter
    def get_err_msg(self):
        return self.err_msg

    def set_err_msg(self, value):
        self.err_msg = value

    # order_currency getter and setter
    def get_order_currency(self):
        return self.order_currency

    def set_order_currency(self, value):
        self.order_currency = value

    # pay_currency getter and setter
    def get_pay_currency(self):
        return self.pay_currency

    def set_pay_currency(self, value):
        self.pay_currency = value

    # pay_amount getter and setter
    def get_pay_amount(self):
        return self.pay_amount

    def set_pay_amount(self, value):
        self.pay_amount = value