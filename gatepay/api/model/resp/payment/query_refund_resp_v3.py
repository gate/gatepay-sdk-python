from dataclasses import dataclass

from gatepay.base_response import BaseResponse


class RefundDetailItem:
    def __init__(self):
        self.transaction_id = ""
        self.transact_time = 0
        self.pay_channel = ""
        self.status = ""
        self.amount = ""
        self.currency = ""
        self.chain = ""
        self.address = ""
        self.hash = ""
        self.remark = ""
        self.bill_type = 0

    # transaction_id getter and setter
    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_id(self, value):
        self.transaction_id = value

    # transact_time getter and setter
    def get_transact_time(self):
        return self.transact_time

    def set_transact_time(self, value):
        self.transact_time = value

    # pay_channel getter and setter
    def get_pay_channel(self):
        return self.pay_channel

    def set_pay_channel(self, value):
        self.pay_channel = value

    # status getter and setter
    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    # amount getter and setter
    def get_amount(self):
        return self.amount

    def set_amount(self, value):
        self.amount = value

    # currency getter and setter
    def get_currency(self):
        return self.currency

    def set_currency(self, value):
        self.currency = value

    # chain getter and setter
    def get_chain(self):
        return self.chain

    def set_chain(self, value):
        self.chain = value

    # address getter and setter
    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value

    # hash getter and setter
    def get_hash(self):
        return self.hash

    def set_hash(self, value):
        self.hash = value

    # remark getter and setter
    def get_remark(self):
        return self.remark

    def set_remark(self, value):
        self.remark = value

    # bill_type getter and setter
    def get_bill_type(self):
        return self.bill_type

    def set_bill_type(self, value):
        self.bill_type = value


class QueryRefundRespV3(BaseResponse):
    def __init__(self):
        super().__init__()
        self.refund_request_id = ""
        self.gate_refund_id = ""
        self.refund_id = ""
        self.order_id = ""
        self.merchant_trade_no = ""
        self.create_time = 0
        self.transact_time = 0
        self.transaction_id = ""
        self.tx_hash = ""
        self.order_amount = ""
        self.order_currency = ""
        self.request_amount = ""
        self.request_currency = ""
        self.amount = ""
        self.currency = ""
        self.status = ""
        self.remark = ""
        self.refund_style = 0
        self.refund_pay_channel = 0
        self.refund_address = ""
        self.refund_chain = ""
        self.refund_bear_type = 0
        self.refund_amount_type = 0
        self.refund_account_type = 0
        self.refund_gas_amount = ""
        self.refund_fail_reason = ""
        self.refund_to_gate_uid = 0
        self.channel_id = ""
        self.nick_name = ""
        self.payer_id = 0
        self.from_address = ""
        self.refund_details = []
        self.pay_channel = ""
        self.bill_type = 0
        self.goods_name = ""
        self.total_request_amount = ""
        self.total_request_currency = ""
        self.total_receive_amount = ""
        self.total_receive_currency = ""

    # refund_request_id getter and setter
    def get_refund_request_id(self):
        return self.refund_request_id

    def set_refund_request_id(self, value):
        self.refund_request_id = value

    # gate_refund_id getter and setter
    def get_gate_refund_id(self):
        return self.gate_refund_id

    def set_gate_refund_id(self, value):
        self.gate_refund_id = value

    # refund_id getter and setter
    def get_refund_id(self):
        return self.refund_id

    def set_refund_id(self, value):
        self.refund_id = value

    # order_id getter and setter
    def get_order_id(self):
        return self.order_id

    def set_order_id(self, value):
        self.order_id = value

    # merchant_trade_no getter and setter
    def get_merchant_trade_no(self):
        return self.merchant_trade_no

    def set_merchant_trade_no(self, value):
        self.merchant_trade_no = value

    # create_time getter and setter
    def get_create_time(self):
        return self.create_time

    def set_create_time(self, value):
        self.create_time = value

    # transact_time getter and setter
    def get_transact_time(self):
        return self.transact_time

    def set_transact_time(self, value):
        self.transact_time = value

    # transaction_id getter and setter
    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_id(self, value):
        self.transaction_id = value

    # tx_hash getter and setter
    def get_tx_hash(self):
        return self.tx_hash

    def set_tx_hash(self, value):
        self.tx_hash = value

    # order_amount getter and setter
    def get_order_amount(self):
        return self.order_amount

    def set_order_amount(self, value):
        self.order_amount = value

    # order_currency getter and setter
    def get_order_currency(self):
        return self.order_currency

    def set_order_currency(self, value):
        self.order_currency = value

    # request_amount getter and setter
    def get_request_amount(self):
        return self.request_amount

    def set_request_amount(self, value):
        self.request_amount = value

    # request_currency getter and setter
    def get_request_currency(self):
        return self.request_currency

    def set_request_currency(self, value):
        self.request_currency = value

    # amount getter and setter
    def get_amount(self):
        return self.amount

    def set_amount(self, value):
        self.amount = value

    # currency getter and setter
    def get_currency(self):
        return self.currency

    def set_currency(self, value):
        self.currency = value

    # status getter and setter
    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    # remark getter and setter
    def get_remark(self):
        return self.remark

    def set_remark(self, value):
        self.remark = value

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

    # refund_amount_type getter and setter
    def get_refund_amount_type(self):
        return self.refund_amount_type

    def set_refund_amount_type(self, value):
        self.refund_amount_type = value

    # refund_account_type getter and setter
    def get_refund_account_type(self):
        return self.refund_account_type

    def set_refund_account_type(self, value):
        self.refund_account_type = value

    # refund_gas_amount getter and setter
    def get_refund_gas_amount(self):
        return self.refund_gas_amount

    def set_refund_gas_amount(self, value):
        self.refund_gas_amount = value

    # refund_fail_reason getter and setter
    def get_refund_fail_reason(self):
        return self.refund_fail_reason

    def set_refund_fail_reason(self, value):
        self.refund_fail_reason = value

    # refund_to_gate_uid getter and setter
    def get_refund_to_gate_uid(self):
        return self.refund_to_gate_uid

    def set_refund_to_gate_uid(self, value):
        self.refund_to_gate_uid = value

    # channel_id getter and setter
    def get_channel_id(self):
        return self.channel_id

    def set_channel_id(self, value):
        self.channel_id = value

    # nick_name getter and setter
    def get_nick_name(self):
        return self.nick_name

    def set_nick_name(self, value):
        self.nick_name = value

    # payer_id getter and setter
    def get_payer_id(self):
        return self.payer_id

    def set_payer_id(self, value):
        self.payer_id = value

    # from_address getter and setter
    def get_from_address(self):
        return self.from_address

    def set_from_address(self, value):
        self.from_address = value

    # refund_details getter and setter
    def get_refund_details(self):
        return self.refund_details

    def set_refund_details(self, value):
        self.refund_details = value

    # pay_channel getter and setter
    def get_pay_channel(self):
        return self.pay_channel

    def set_pay_channel(self, value):
        self.pay_channel = value

    # bill_type getter and setter
    def get_bill_type(self):
        return self.bill_type

    def set_bill_type(self, value):
        self.bill_type = value

    # goods_name getter and setter
    def get_goods_name(self):
        return self.goods_name

    def set_goods_name(self, value):
        self.goods_name = value

    # total_request_amount getter and setter
    def get_total_request_amount(self):
        return self.total_request_amount

    def set_total_request_amount(self, value):
        self.total_request_amount = value

    # total_request_currency getter and setter
    def get_total_request_currency(self):
        return self.total_request_currency

    def set_total_request_currency(self, value):
        self.total_request_currency = value

    # total_receive_amount getter and setter
    def get_total_receive_amount(self):
        return self.total_receive_amount

    def set_total_receive_amount(self, value):
        self.total_receive_amount = value

    # total_receive_currency getter and setter
    def get_total_receive_currency(self):
        return self.total_receive_currency

    def set_total_receive_currency(self, value):
        self.total_receive_currency = value

