from src.gatepay.base_request import BaseRequest
from src.gatepay.api.model.req.env_req import EnvReq
from src.gatepay.api.model.req.goods_req import GoodsReq
from src.gatepay.common.enums.gatepay_api import GatePayApi

class CreateOrderReq(BaseRequest):
    """
    收银台创建订单请求
    """

    def __init__(self):
        """
        初始化CreateOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.CHECKOUT_CREATE_ORDER  # 需要根据实际GatePayApi定义调整

        self.merchant_trade_no = None
        self.env = None
        self.currency = None
        self.order_amount = None
        self.pay_currency = None
        self.merchant_user_id = 0
        self.goods = None
        self.return_url = None
        self.cancel_url = None
        self.chain = None
        self.full_curr_type = None
        self.channel_id = None

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

    def get_env(self) -> EnvReq:
        """
        获取环境信息

        Returns:
            EnvReq: 环境信息
        """
        return self.env

    def set_env(self, env: EnvReq):
        """
        设置环境信息

        Args:
            env (EnvReq): 环境信息
        """
        self.env = env

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

    def get_merchant_user_id(self) -> int:
        """
        获取商户用户ID

        Returns:
            int: 商户用户ID
        """
        return self.merchant_user_id

    def set_merchant_user_id(self, merchant_user_id: int):
        """
        设置商户用户ID

        Args:
            merchant_user_id (int): 商户用户ID
        """
        self.merchant_user_id = merchant_user_id

    def get_goods(self) -> GoodsReq:
        """
        获取商品信息

        Returns:
            GoodsReq: 商品信息
        """
        return self.goods

    def set_goods(self, goods: GoodsReq):
        """
        设置商品信息

        Args:
            goods (GoodsReq): 商品信息
        """
        self.goods = goods

    def get_return_url(self) -> str:
        """
        获取支付完成回调地址

        Returns:
            str: 支付完成回调地址
        """
        return self.return_url

    def set_return_url(self, return_url: str):
        """
        设置支付完成回调地址

        Args:
            return_url (str): 支付完成回调地址
        """
        self.return_url = return_url

    def get_cancel_url(self) -> str:
        """
        获取取消支付回调地址

        Returns:
            str: 取消支付回调地址
        """
        return self.cancel_url

    def set_cancel_url(self, cancel_url: str):
        """
        设置取消支付回调地址

        Args:
            cancel_url (str): 取消支付回调地址
        """
        self.cancel_url = cancel_url

    def get_chain(self) -> str:
        """
        获取链名称

        Returns:
            str: 链名称
        """
        return self.chain

    def set_chain(self, chain: str):
        """
        设置链名称

        Args:
            chain (str): 链名称
        """
        self.chain = chain

    def get_full_curr_type(self) -> str:
        """
        获取完整币种类型

        Returns:
            str: 完整币种类型
        """
        return self.full_curr_type

    def set_full_curr_type(self, full_curr_type: str):
        """
        设置完整币种类型

        Args:
            full_curr_type (str): 完整币种类型
        """
        self.full_curr_type = full_curr_type

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

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateOrderReq(merchant_trade_no={self.merchant_trade_no}, "
                f"env={self.env}, currency={self.currency}, order_amount={self.order_amount}, "
                f"pay_currency={self.pay_currency}, merchant_user_id={self.merchant_user_id}, "
                f"goods={self.goods}, return_url={self.return_url}, cancel_url={self.cancel_url}, "
                f"chain={self.chain}, full_curr_type={self.full_curr_type}, channel_id={self.channel_id})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
