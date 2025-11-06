
from dataclasses import dataclass

from src.gatepay.api.model.req.env_req import EnvReq
from src.gatepay.api.model.req.goods_req import GoodsReq
from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class CreateOrderReq(BaseRequest):
    """
    支付创建订单请求
    """

    def __init__(self):
        """
        初始化CreateOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_CREATE_ORDER  # 需要根据实际GatePayApi定义调整

        self.merchant_trade_no = None
        self.currency = None
        self.order_amount = None
        self.env = None
        self.goods = None
        self.extend_info = None
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

    def get_extend_info(self) -> str:
        """
        获取扩展信息

        Returns:
            str: 扩展信息
        """
        return self.extend_info

    def set_extend_info(self, extend_info: str):
        """
        设置扩展信息

        Args:
            extend_info (str): 扩展信息
        """
        self.extend_info = extend_info

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
                f"currency={self.currency}, order_amount={self.order_amount}, "
                f"env={self.env}, goods={self.goods}, extend_info={self.extend_info}, "
                f"channel_id={self.channel_id})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
