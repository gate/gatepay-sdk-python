from typing import Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse
from gatepay.api.model.transaction_detail import TransactionDetail


@dataclass
class TransactionDetailResp(BaseResponse['TransactionDetailResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 支付单id
    prepay_id: Optional[str] = None

    # 用于申请商户账号的Gate UID
    merchant_id: int = 0

    # 商户系统交易号
    merchant_trade_no: Optional[str] = None

    # 交易流水号
    transaction_id: Optional[str] = None

    # 商品名称
    goods_name: Optional[str] = None

    # 订单币种
    currency: Optional[str] = None

    # 订单金额
    order_amount: Optional[str] = None

    # 用户实际支付币种
    pay_currency: Optional[str] = None

    # 订单对应用户实际支付币种的金额
    pay_amount: Optional[str] = None

    # 订单状态
    status: Optional[str] = None

    # 订单创建时间的utc表达，例如2023-01-07 14:04:02
    utc_create_time: Optional[str] = None

    # 订单过期时间的utc表达，例如2023-01-07 14:04:02
    utc_expire_time: Optional[str] = None

    # 订单状态更新时间的utc表达，例如2023-01-07 14:04:02
    utc_update_time: Optional[str] = None

    # 订单在后台完成交易的UTC毫秒时间戳
    transact_time: int = 0

    # 订单名称
    order_name: Optional[str] = None

    # 链上交易详情
    transaction_detail: Optional[TransactionDetail] = None

    # 客户名称
    channel_id: Optional[str] = None

    def get_prepay_id(self) -> Optional[str]:
        """
        获取支付单id

        :return: 支付单id
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str) -> None:
        """
        设置支付单id

        :param prepay_id: 支付单id
        """
        self.prepay_id = prepay_id

    def get_merchant_id(self) -> int:
        """
        获取用于申请商户账号的Gate UID

        :return: Gate UID
        """
        return self.merchant_id

    def set_merchant_id(self, merchant_id: int) -> None:
        """
        设置用于申请商户账号的Gate UID

        :param merchant_id: Gate UID
        """
        self.merchant_id = merchant_id

    def get_merchant_trade_no(self) -> Optional[str]:
        """
        获取商户系统交易号

        :return: 商户系统交易号
        """
        return self.merchant_trade_no

    def set_merchant_trade_no(self, merchant_trade_no: str) -> None:
        """
        设置商户系统交易号

        :param merchant_trade_no: 商户系统交易号
        """
        self.merchant_trade_no = merchant_trade_no

    def get_transaction_id(self) -> Optional[str]:
        """
        获取交易流水号

        :return: 交易流水号
        """
        return self.transaction_id

    def set_transaction_id(self, transaction_id: str) -> None:
        """
        设置交易流水号

        :param transaction_id: 交易流水号
        """
        self.transaction_id = transaction_id

    def get_goods_name(self) -> Optional[str]:
        """
        获取商品名称

        :return: 商品名称
        """
        return self.goods_name

    def set_goods_name(self, goods_name: str) -> None:
        """
        设置商品名称

        :param goods_name: 商品名称
        """
        self.goods_name = goods_name

    def get_currency(self) -> Optional[str]:
        """
        获取订单币种

        :return: 订单币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置订单币种

        :param currency: 订单币种
        """
        self.currency = currency

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

    def get_pay_currency(self) -> Optional[str]:
        """
        获取用户实际支付币种

        :return: 支付币种
        """
        return self.pay_currency

    def set_pay_currency(self, pay_currency: str) -> None:
        """
        设置用户实际支付币种

        :param pay_currency: 支付币种
        """
        self.pay_currency = pay_currency

    def get_pay_amount(self) -> Optional[str]:
        """
        获取订单对应用户实际支付币种的金额

        :return: 支付金额
        """
        return self.pay_amount

    def set_pay_amount(self, pay_amount: str) -> None:
        """
        设置订单对应用户实际支付币种的金额

        :param pay_amount: 支付金额
        """
        self.pay_amount = pay_amount

    def get_status(self) -> Optional[str]:
        """
        获取订单状态

        :return: 订单状态
        """
        return self.status

    def set_status(self, status: str) -> None:
        """
        设置订单状态

        :param status: 订单状态
        """
        self.status = status

    def get_utc_create_time(self) -> Optional[str]:
        """
        获取订单创建时间的utc表达

        :return: 创建时间
        """
        return self.utc_create_time

    def set_utc_create_time(self, utc_create_time: str) -> None:
        """
        设置订单创建时间的utc表达

        :param utc_create_time: 创建时间
        """
        self.utc_create_time = utc_create_time

    def get_utc_expire_time(self) -> Optional[str]:
        """
        获取订单过期时间的utc表达

        :return: 过期时间
        """
        return self.utc_expire_time

    def set_utc_expire_time(self, utc_expire_time: str) -> None:
        """
        设置订单过期时间的utc表达

        :param utc_expire_time: 过期时间
        """
        self.utc_expire_time = utc_expire_time

    def get_utc_update_time(self) -> Optional[str]:
        """
        获取订单状态更新时间的utc表达

        :return: 更新时间
        """
        return self.utc_update_time

    def set_utc_update_time(self, utc_update_time: str) -> None:
        """
        设置订单状态更新时间的utc表达

        :param utc_update_time: 更新时间
        """
        self.utc_update_time = utc_update_time

    def get_transact_time(self) -> int:
        """
        获取订单在后台完成交易的UTC毫秒时间戳

        :return: 交易时间戳
        """
        return self.transact_time

    def set_transact_time(self, transact_time: int) -> None:
        """
        设置订单在后台完成交易的UTC毫秒时间戳

        :param transact_time: 交易时间戳
        """
        self.transact_time = transact_time

    def get_order_name(self) -> Optional[str]:
        """
        获取订单名称

        :return: 订单名称
        """
        return self.order_name

    def set_order_name(self, order_name: str) -> None:
        """
        设置订单名称

        :param order_name: 订单名称
        """
        self.order_name = order_name

    def get_transaction_detail(self) -> Optional[TransactionDetail]:
        """
        获取链上交易详情

        :return: 交易详情
        """
        return self.transaction_detail

    def set_transaction_detail(self, transaction_detail: TransactionDetail) -> None:
        """
        设置链上交易详情

        :param transaction_detail: 交易详情
        """
        self.transaction_detail = transaction_detail

    def get_channel_id(self) -> Optional[str]:
        """
        获取客户名称

        :return: 客户名称
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str) -> None:
        """
        设置客户名称

        :param channel_id: 客户名称
        """
        self.channel_id = channel_id
