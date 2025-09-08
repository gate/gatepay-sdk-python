

from dataclasses import dataclass
from typing import Optional

from gatepay.api.model.chain_transaction_info import ChainTransactionInfo
from gatepay.base_response import BaseResponse


@dataclass
class QueryOrderResp(BaseResponse['QueryOrderResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 支付单单号
    prepay_id: Optional[str] = None

    # 用于申请商户账号的Gate UID
    merchant_id: int = 0

    # 商户系统交易号
    merchant_trade_no: Optional[str] = None

    # 交易流水号
    transaction_id: Optional[str] = None

    # 商品名，商户创建订单时提供
    goods_name: Optional[str] = None

    # 订单币种
    currency: Optional[str] = None

    # 订单金额
    order_amount: Optional[str] = None

    # 用户实际支付币种，非闪兑单中与订单币种一致
    pay_currency: Optional[str] = None

    # 用户应该支付的金额
    pay_amount: Optional[str] = None

    # 订单币种到用户支付币种的汇率，例如，1BTC换20000USDT
    rate: Optional[str] = None

    # 订单状态，PENDING处理中，PROCESS订单有效期内支付足够金额但链上未确认完毕，PAID订单支付成功，EXPIRED订单已过期
    status: Optional[str] = None

    # 订单的创建时间
    create_time: int = 0

    # 订单的过期时间
    expire_time: int = 0

    # 订单在Gate内部交易发生时间
    transact_time: int = 0

    # 订单名称
    order_name: Optional[str] = None

    # 订单在链上交易情况总览
    transaction_info: Optional[ChainTransactionInfo] = None

    # 客户名称
    channel_id: Optional[str] = None

    # 收款地址
    address: Optional[str] = None

    # 网络
    chain: Optional[str] = None

    def get_prepay_id(self) -> Optional[str]:
        """
        获取支付单单号

        :return: 支付单单号
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str) -> None:
        """
        设置支付单单号

        :param prepay_id: 支付单单号
        """
        self.prepay_id = prepay_id

    def get_merchant_id(self) -> int:
        """
        获取商户ID

        :return: 商户ID
        """
        return self.merchant_id

    def set_merchant_id(self, merchant_id: int) -> None:
        """
        设置商户ID

        :param merchant_id: 商户ID
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
        获取商品名

        :return: 商品名
        """
        return self.goods_name

    def set_goods_name(self, goods_name: str) -> None:
        """
        设置商品名

        :param goods_name: 商品名
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

        :return: 用户实际支付币种
        """
        return self.pay_currency

    def set_pay_currency(self, pay_currency: str) -> None:
        """
        设置用户实际支付币种

        :param pay_currency: 用户实际支付币种
        """
        self.pay_currency = pay_currency

    def get_pay_amount(self) -> Optional[str]:
        """
        获取用户应该支付的金额

        :return: 用户应该支付的金额
        """
        return self.pay_amount

    def set_pay_amount(self, pay_amount: str) -> None:
        """
        设置用户应该支付的金额

        :param pay_amount: 用户应该支付的金额
        """
        self.pay_amount = pay_amount

    def get_rate(self) -> Optional[str]:
        """
        获取汇率

        :return: 汇率
        """
        return self.rate

    def set_rate(self, rate: str) -> None:
        """
        设置汇率

        :param rate: 汇率
        """
        self.rate = rate

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

    def get_create_time(self) -> int:
        """
        获取订单创建时间

        :return: 订单创建时间
        """
        return self.create_time

    def set_create_time(self, create_time: int) -> None:
        """
        设置订单创建时间

        :param create_time: 订单创建时间
        """
        self.create_time = create_time

    def get_expire_time(self) -> int:
        """
        获取订单过期时间

        :return: 订单过期时间
        """
        return self.expire_time

    def set_expire_time(self, expire_time: int) -> None:
        """
        设置订单过期时间

        :param expire_time: 订单过期时间
        """
        self.expire_time = expire_time

    def get_transact_time(self) -> int:
        """
        获取订单交易时间

        :return: 订单交易时间
        """
        return self.transact_time

    def set_transact_time(self, transact_time: int) -> None:
        """
        设置订单交易时间

        :param transact_time: 订单交易时间
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

    def get_transaction_info(self) -> Optional[ChainTransactionInfo]:
        """
        获取链上交易信息

        :return: 链上交易信息
        """
        return self.transaction_info

    def set_transaction_info(self, transaction_info: ChainTransactionInfo) -> None:
        """
        设置链上交易信息

        :param transaction_info: 链上交易信息
        """
        self.transaction_info = transaction_info

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

    def get_address(self) -> Optional[str]:
        """
        获取收款地址

        :return: 收款地址
        """
        return self.address

    def set_address(self, address: str) -> None:
        """
        设置收款地址

        :param address: 收款地址
        """
        self.address = address

    def get_chain(self) -> Optional[str]:
        """
        获取网络

        :return: 网络
        """
        return self.chain

    def set_chain(self, chain: str) -> None:
        """
        设置网络

        :param chain: 网络
        """
        self.chain = chain
