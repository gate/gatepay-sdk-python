

from enum import Enum


class GatePayApi(Enum):

    # 地址支付相关API
    ADDRESS_CHAINS = ("/v1/pay/address/chains", "GET")
    ADDRESS_CURRENCIES = ("/v1/pay/address/currencies", "GET")
    ADDRESS_SUPPORTED_CONVERT_CURRENCIES = ("/v1/pay/address/supportedconvertcurrencies", "GET")
    ADDRESS_CREATE_ORDER = ("/v1/pay/address/create", "POST")
    ADDRESS_QUERY_ORDER = ("/v1/pay/address/query", "GET")
    ADDRESS_CREATE_REFUND = ("/v1/pay/address/refund", "POST")
    ADDRESS_CREATE_REFUND_CONVERT = ("/v1/pay/address/refundconvert", "POST")
    ADDRESS_TRANSACTION_DETAIL = ("/v1/pay/address/transactiondetail", "GET")

    # 支付相关API
    PAYMENT_CREATE_ORDER = ("/v1/pay/order", "POST")
    PAYMENT_CLOSE_ORDER = ("/v1/pay/order/close", "POST")
    PAYMENT_QUERY_ORDER = ("/v1/pay/order/query", "POST")
    PAYMENT_CREATE_REFUND = ("/v1/pay/order/refund", "POST")
    PAYMENT_QUERY_REFUND = ("/v1/pay/order/refund/query", "POST")
    PAYMENT_CREATE_BATCH_TRANSFER = ("/v1/pay/batch/transfer", "POST")
    PAYMENT_QUERY_BATCH_TRANSFER = ("/v1/pay/batch/transfer/query", "POST")
    PAYMENT_QUERY_BALANCE = ("/v1/pay/balance", "GET")

    # 收银台相关API
    CHECKOUT_CREATE_ORDER = ("/v1/pay/checkout/order", "POST")
    CHECKOUT_CREATE_REFUND = ("/v1/pay/checkout/refund", "POST")

    # 渠道管理相关API
    CHANNEL_MANAGE_SAVE = ("/v1/pay/channelmanage/save", "POST")
    CHANNEL_MANAGE_LIST = ("/v1/pay/channelmanage/list", "GET")
    CHANNEL_MANAGE_UPDATE = ("/v1/pay/channelmanage/update", "PUT")
    CHANNEL_MANAGE_DELETE = ("/v1/pay/channelmanage/delete", "DELETE")

    # 提现相关API
    WITHDRAW_CREATE_ORDER = ("/v1/pay/withdraw", "POST")
    WITHDRAW_QUERY_ORDER = ("/v1/pay/withdraw/query", "POST")
    WITHDRAW_CURRENCY_CHAINS = ("/v1/pay/wallet/currency_chains", "GET")
    WITHDRAW_QUERY_BALANCE = ("/v1/pay/wallet/total_balance", "GET")
    WITHDRAW_QUERY_STATUS = ("/v1/pay/wallet/withdraw_status", "GET")

    # 二维码支付相关API
    QR_CODE_CREATE_ORDER = ("/v1/pay/transactions/native", "POST")

    # 礼品卡相关API
    GIFT_CREATE = ("/v1/pay/gift/create", "POST")
    GIFT_LIST_TEMPLATE = ("/v1/pay/gift/temp/list", "GET")
    GIFT_QUERY = ("/v1/pay/gift/query", "POST")

    # 闪兑相关API
    CONVERT_CURRENCY = ("/v1/pay/convert/currency", "GET")
    CONVERT_PAIR = ("/v1/pay/convert/pair", "GET")
    CONVERT_PREVIEW = ("/v1/pay/convert/preview", "POST")
    CONVERT_CREATE_ORDER = ("/v1/pay/convert", "POST")
    CONVERT_QUERY_ORDER = ("/v1/pay/convert/order", "GET")

    # 账单相关API
    BILL_QUERY_ORDERS = ("/v1/pay/bill/orderlist", "GET")

    def __init__(self, url: str, http_method: str):
        """
        初始化 GatePayApi 枚举值

        :param url: API地址
        :param http_method: HTTP方法
        """
        self.url = url
        self.http_method = http_method

    def get_url(self) -> str:
        """
        获取API地址

        :return: API地址
        """
        return self.url

    def set_url(self, url: str) -> None:
        """
        设置API地址

        :param url: API地址
        """
        self.url = url

    def get_http_method(self) -> str:
        """
        获取HTTP方法

        :return: HTTP方法
        """
        return self.http_method

    def set_http_method(self, http_method: str) -> None:
        """
        设置HTTP方法

        :param http_method: HTTP方法
        """
        self.http_method = http_method
