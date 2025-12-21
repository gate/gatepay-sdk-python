from typing import Optional

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


class CreateRefundReqV2(BaseRequest):
    """
    退款请求 V2
    """

    def __init__(self):
        """
        初始化CreateRefundReq对象
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_CREATE_REFUND_V2  # 需要根据实际GatePayApi定义调整

        self.refund_request_id: Optional[str] = None
        self.prepay_id: Optional[str] = None
        self.refund_amount: Optional[str] = None
        self.refund_reason: Optional[str] = None
        self.refund_gate_id: Optional[str] = None
        self.refund_style: Optional[int] = None
        self.refund_pay_channel: Optional[int] = None
        self.refund_to_gate_uid: Optional[int] = None
        self.refund_address: Optional[str] = None
        self.refund_chain: Optional[str] = None
        self.refund_bear_type: Optional[int] = None
        self.memo: Optional[str] = None
        self.refund_amount_type_full: Optional[int] = None
        self.email_code: Optional[str] = None
        self.fund_pass: Optional[str] = None
        self.sms_code: Optional[str] = None
        self.totp_code: Optional[str] = None
        self.m_id: Optional[int] = None
        self.need_notify: bool = False
        self.refund_limit: bool = False
        self.refund_currency: Optional[str] = None
        self.refund_fund_statement_id: Optional[int] = None
        self.refund_source: Optional[int] = None

    # refund_request_id getter and setter
    def get_refund_request_id(self):
        return self.refund_request_id

    def set_refund_request_id(self, value):
        self.refund_request_id = value

    # prepay_id getter and setter
    def get_prepay_id(self):
        return self.prepay_id

    def set_prepay_id(self, value):
        self.prepay_id = value

    # refund_amount getter and setter
    def get_refund_amount(self):
        return self.refund_amount

    def set_refund_amount(self, value):
        self.refund_amount = value

    # refund_reason getter and setter
    def get_refund_reason(self):
        return self.refund_reason

    def set_refund_reason(self, value):
        self.refund_reason = value

    # refund_style getter and setter
    def get_refund_style(self):
        return self.refund_style

    def set_refund_style(self, value):
        self.refund_style = value

    # refund_pay_channel getter and setter
    def get_refund_pay_channel(self):
        return self.refund_pay_channel

    def set_refund_pay_channel(self, value):
        self.refund_pay_channel = value

    # refund_to_gate_uid getter and setter
    def get_refund_to_gate_uid(self):
        return self.refund_to_gate_uid

    def set_refund_to_gate_uid(self, value):
        self.refund_to_gate_uid = value

    # refund_address getter and setter
    def get_refund_address(self):
        return self.refund_address

    def set_refund_address(self, value):
        self.refund_address = value

    # refund_chain getter and setter
    def get_refund_chain(self):
        return self.refund_chain

    def set_refund_chain(self, value):
        self.refund_chain = value

    # refund_bear_type getter and setter
    def get_refund_bear_type(self):
        return self.refund_bear_type

    def set_refund_bear_type(self, value):
        self.refund_bear_type = value

    # memo getter and setter
    def get_memo(self):
        return self.memo

    def set_memo(self, value):
        self.memo = value