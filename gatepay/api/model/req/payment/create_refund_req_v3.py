from typing import Optional

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


class CreateRefundReqV3(BaseRequest):
    """
    支付创建退款请求
    """

    def __init__(self):
        """
        初始化CreateRefundReq对象
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_CREATE_REFUND_V3  # 需要根据实际GatePayApi定义调整

        self.merchant_id: Optional[str] = None
        self.client_id: Optional[str] = None
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

    # merchant_id getter and setter
    def get_merchant_id(self):
        return self.merchant_id

    def set_merchant_id(self, value):
        self.merchant_id = value

    # client_id getter and setter
    def get_client_id(self):
        return self.client_id

    def set_client_id(self, value):
        self.client_id = value

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

    # refund_gate_id getter and setter
    def get_refund_gate_id(self):
        return self.refund_gate_id

    def set_refund_gate_id(self, value):
        self.refund_gate_id = value

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

    # refund_amount_type_full getter and setter
    def get_refund_amount_type_full(self):
        return self.refund_amount_type_full

    def set_refund_amount_type_full(self, value):
        self.refund_amount_type_full = value

    # email_code getter and setter
    def get_email_code(self):
        return self.email_code

    def set_email_code(self, value):
        self.email_code = value

    # fund_pass getter and setter
    def get_fund_pass(self):
        return self.fund_pass

    def set_fund_pass(self, value):
        self.fund_pass = value

    # sms_code getter and setter
    def get_sms_code(self):
        return self.sms_code

    def set_sms_code(self, value):
        self.sms_code = value

    # totp_code getter and setter
    def get_totp_code(self):
        return self.totp_code

    def set_totp_code(self, value):
        self.totp_code = value

    # m_id getter and setter
    def get_m_id(self):
        return self.m_id

    def set_m_id(self, value):
        self.m_id = value

    # need_notify getter and setter
    def get_need_notify(self):
        return self.need_notify

    def set_need_notify(self, value):
        self.need_notify = value

    # refund_limit getter and setter
    def get_refund_limit(self):
        return self.refund_limit

    def set_refund_limit(self, value):
        self.refund_limit = value

    # refund_currency getter and setter
    def get_refund_currency(self):
        return self.refund_currency

    def set_refund_currency(self, value):
        self.refund_currency = value

    # refund_fund_statement_id getter and setter
    def get_refund_fund_statement_id(self):
        return self.refund_fund_statement_id

    def set_refund_fund_statement_id(self, value):
        self.refund_fund_statement_id = value

    # refund_source getter and setter
    def get_refund_source(self):
        return self.refund_source

    def set_refund_source(self, value):
        self.refund_source = value

    # getMId method
    def get_m_id_converted(self):
        """
        获取商户ID（转换为Long类型）
        """
        return int(self.merchant_id) if self.merchant_id else 0