

from dataclasses import dataclass
from typing import Optional

from gatepay.api.model.chain_transaction_info import ChainTransactionInfo
from gatepay.base_response import BaseResponse


@dataclass
class QueryOrderResp(BaseResponse):
    """
    支付查询订单响应
    """

    def __init__(self):
        """
        初始化QueryOrderResp对象
        """
        super().__init__()

        self.prepay_id = None
        self.merchant_id = 0
        self.merchant_trade_no = None
        self.transaction_id = None
        self.goods_name = None
        self.currency = None
        self.order_amount = None
        self.status = None
        self.create_time = 0
        self.expire_time = 0
        self.transact_time = 0
        self.expect_currency = None
        self.actual_currency = None
        self.actual_amount = None
        self.rate = None
        self.app_name = None
        self.app_logo = None
        self.in_usdt = None
        self.channel_id = None
        self.order_name = None
        self.pay_currency = None
        self.pay_amount = None
        self.channel_type = None
        self.pay_account = None

    def get_prepay_id(self) -> str:
        """
        获取预支付ID

        Returns:
            str: 预支付ID
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str):
        """
        设置预支付ID

        Args:
            prepay_id (str): 预支付ID
        """
        self.prepay_id = prepay_id

    def get_merchant_id(self) -> int:
        """
        获取商户ID

        Returns:
            int: 商户ID
        """
        return self.merchant_id

    def set_merchant_id(self, merchant_id: int):
        """
        设置商户ID

        Args:
            merchant_id (int): 商户ID
        """
        self.merchant_id = merchant_id

    def get_merchant_trade_no(self) -> str:
        """
        获取商户交易号

        Returns:
            str: 商户交易号
        """
        return self.merchant_trade_no

    def set_merchant_trade_no(self, merchant_trade_no: str):
        """
        设置商户交易号

        Args:
            merchant_trade_no (str): 商户交易号
        """
        self.merchant_trade_no = merchant_trade_no

    def get_transaction_id(self) -> str:
        """
        获取交易ID

        Returns:
            str: 交易ID
        """
        return self.transaction_id

    def set_transaction_id(self, transaction_id: str):
        """
        设置交易ID

        Args:
            transaction_id (str): 交易ID
        """
        self.transaction_id = transaction_id

    def get_goods_name(self) -> str:
        """
        获取商品名称

        Returns:
            str: 商品名称
        """
        return self.goods_name

    def set_goods_name(self, goods_name: str):
        """
        设置商品名称

        Args:
            goods_name (str): 商品名称
        """
        self.goods_name = goods_name

    def get_currency(self) -> str:
        """
        获取订单币种

        Returns:
            str: 订单币种
        """
        return self.currency

    def set_currency(self, currency: str):
        """
        设置订单币种

        Args:
            currency (str): 订单币种
        """
        self.currency = currency

    def get_order_amount(self) -> str:
        """
        获取订单金额

        Returns:
            str: 订单金额
        """
        return self.order_amount

    def set_order_amount(self, order_amount: str):
        """
        设置订单金额

        Args:
            order_amount (str): 订单金额
        """
        self.order_amount = order_amount

    def get_status(self) -> str:
        """
        获取订单状态

        Returns:
            str: 订单状态
        """
        return self.status

    def set_status(self, status: str):
        """
        设置订单状态

        Args:
            status (str): 订单状态
        """
        self.status = status

    def get_create_time(self) -> int:
        """
        获取创建时间

        Returns:
            int: 创建时间（毫秒时间戳）
        """
        return self.create_time

    def set_create_time(self, create_time: int):
        """
        设置创建时间

        Args:
            create_time (int): 创建时间（毫秒时间戳）
        """
        self.create_time = create_time

    def get_expire_time(self) -> int:
        """
        获取过期时间

        Returns:
            int: 过期时间（毫秒时间戳）
        """
        return self.expire_time

    def set_expire_time(self, expire_time: int):
        """
        设置过期时间

        Args:
            expire_time (int): 过期时间（毫秒时间戳）
        """
        self.expire_time = expire_time

    def get_transact_time(self) -> int:
        """
        获取交易时间

        Returns:
            int: 交易时间（毫秒时间戳）
        """
        return self.transact_time

    def set_transact_time(self, transact_time: int):
        """
        设置交易时间

        Args:
            transact_time (int): 交易时间（毫秒时间戳）
        """
        self.transact_time = transact_time

    def get_expect_currency(self) -> str:
        """
        获取期望币种

        Returns:
            str: 期望币种
        """
        return self.expect_currency

    def set_expect_currency(self, expect_currency: str):
        """
        设置期望币种

        Args:
            expect_currency (str): 期望币种
        """
        self.expect_currency = expect_currency

    def get_actual_currency(self) -> str:
        """
        获取实际币种

        Returns:
            str: 实际币种
        """
        return self.actual_currency

    def set_actual_currency(self, actual_currency: str):
        """
        设置实际币种

        Args:
            actual_currency (str): 实际币种
        """
        self.actual_currency = actual_currency

    def get_actual_amount(self) -> str:
        """
        获取实际金额

        Returns:
            str: 实际金额
        """
        return self.actual_amount

    def set_actual_amount(self, actual_amount: str):
        """
        设置实际金额

        Args:
            actual_amount (str): 实际金额
        """
        self.actual_amount = actual_amount

    def get_rate(self) -> str:
        """
        获取汇率

        Returns:
            str: 汇率
        """
        return self.rate

    def set_rate(self, rate: str):
        """
        设置汇率

        Args:
            rate (str): 汇率
        """
        self.rate = rate

    def get_app_name(self) -> str:
        """
        获取应用名称

        Returns:
            str: 应用名称
        """
        return self.app_name

    def set_app_name(self, app_name: str):
        """
        设置应用名称

        Args:
            app_name (str): 应用名称
        """
        self.app_name = app_name

    def get_app_logo(self) -> str:
        """
        获取应用Logo

        Returns:
            str: 应用Logo
        """
        return self.app_logo

    def set_app_logo(self, app_logo: str):
        """
        设置应用Logo

        Args:
            app_logo (str): 应用Logo
        """
        self.app_logo = app_logo

    def get_in_usdt(self) -> str:
        """
        获取以USDT计价的金额

        Returns:
            str: 以USDT计价的金额
        """
        return self.in_usdt

    def set_in_usdt(self, in_usdt: str):
        """
        设置以USDT计价的金额

        Args:
            in_usdt (str): 以USDT计价的金额
        """
        self.in_usdt = in_usdt

    def get_channel_id(self) -> str:
        """
        获取渠道ID

        Returns:
            str: 渠道ID
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str):
        """
        设置渠道ID

        Args:
            channel_id (str): 渠道ID
        """
        self.channel_id = channel_id

    def get_order_name(self) -> str:
        """
        获取订单名称

        Returns:
            str: 订单名称
        """
        return self.order_name

    def set_order_name(self, order_name: str):
        """
        设置订单名称

        Args:
            order_name (str): 订单名称
        """
        self.order_name = order_name

    def get_pay_currency(self) -> str:
        """
        获取支付币种

        Returns:
            str: 支付币种
        """
        return self.pay_currency

    def set_pay_currency(self, pay_currency: str):
        """
        设置支付币种

        Args:
            pay_currency (str): 支付币种
        """
        self.pay_currency = pay_currency

    def get_pay_amount(self) -> str:
        """
        获取支付金额

        Returns:
            str: 支付金额
        """
        return self.pay_amount

    def set_pay_amount(self, pay_amount: str):
        """
        设置支付金额

        Args:
            pay_amount (str): 支付金额
        """
        self.pay_amount = pay_amount

    def get_channel_type(self) -> str:
        """
        获取渠道类型

        Returns:
            str: 渠道类型
        """
        return self.channel_type

    def set_channel_type(self, channel_type: str):
        """
        设置渠道类型

        Args:
            channel_type (str): 渠道类型
        """
        self.channel_type = channel_type

    def get_pay_account(self) -> str:
        """
        获取支付账户

        Returns:
            str: 支付账户
        """
        return self.pay_account

    def set_pay_account(self, pay_account: str):
        """
        设置支付账户

        Args:
            pay_account (str): 支付账户
        """
        self.pay_account = pay_account

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"QueryOrderResp(prepay_id={self.prepay_id}, merchant_id={self.merchant_id}, "
                f"merchant_trade_no={self.merchant_trade_no}, transaction_id={self.transaction_id}, "
                f"goods_name={self.goods_name}, currency={self.currency}, order_amount={self.order_amount}, "
                f"status={self.status}, create_time={self.create_time}, expire_time={self.expire_time}, "
                f"transact_time={self.transact_time}, expect_currency={self.expect_currency}, "
                f"actual_currency={self.actual_currency}, actual_amount={self.actual_amount}, "
                f"rate={self.rate}, app_name={self.app_name}, app_logo={self.app_logo}, "
                f"in_usdt={self.in_usdt}, channel_id={self.channel_id}, order_name={self.order_name}, "
                f"pay_currency={self.pay_currency}, pay_amount={self.pay_amount}, "
                f"channel_type={self.channel_type}, pay_account={self.pay_account})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
