from src.gatepay.base_request import BaseRequest
from src.gatepay.api.model.req.env_req import EnvReq
from src.gatepay.api.model.req.goods_req import GoodsReq
from src.gatepay.common.enums.gatepay_api import GatePayApi

class CreateOrderReq(BaseRequest):
    """
    二维码创建订单请求
    """

    def __init__(self):
        """
        初始化CreateOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.QR_CODE_CREATE_ORDER  # 需要根据实际GatePayApi定义调整

        self.merchant_trade_no = None
        self.currency = None
        self.order_amount = None
        self.env = None
        self.goods = None
        self.return_url = None
        self.fiat_currency = None
        self.fiat_amount = None

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


    def set_fiat_amount(self, fiat_amount: str):
        """

        :param fiat_amount:
        :return:
        """
        self.fiat_amount = fiat_amount

    def set_fiat_currency(self, fiat_currency: str):
        """

        :param fiat_currency:
        :return:
        """
        self.fiat_currency = fiat_currency

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateOrderReq(merchant_trade_no={self.merchant_trade_no}, "
                f"currency={self.currency}, order_amount={self.order_amount}, "
                f"env={self.env}, goods={self.goods}, return_url={self.return_url})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
