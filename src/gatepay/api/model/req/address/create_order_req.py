from pydantic import BaseModel, Field
from typing import Optional

from src.gatepay.base_request import BaseRequest
from src.gatepay.api.model.req.env_req import EnvReq
from src.gatepay.api.model.req.goods_req import GoodsReq
from src.gatepay.common.enums.gatepay_api import GatePayApi


def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


class CreateOrderReqData(BaseModel):
    """
    CreateOrderReq的数据模型部分，用于处理Pydantic功能
    """
    # 商户系统中的交易号
    merchant_trade_no: Optional[str] = Field(None, alias='merchantTradeNo')

    # 订单币种
    currency: Optional[str] = None

    # 订单金额
    order_amount: Optional[str] = Field(None, alias='orderAmount')

    # 用户承担手续费 非必传
    surcharge_amount: Optional[str] = Field(None, alias='surchargeAmount')

    fiat_currency : Optional[str] = Field(None, alias='fiatCurrency')

    fiat_amount : Optional[str] = Field(None, alias='fiatAmount')

    # 非地址支付的payCurrency在实际付款时确定，地址支付的payCurrency在下单时候确定
    pay_currency: Optional[str] = Field(None, alias='payCurrency')

    # 真实币种
    actual_currency: Optional[str] = Field(None, alias='actualCurrency')

    # 交易来源，可选值：APP、WEB、WAP、MINIAPP、OTHERS
    env: Optional[EnvReq] = None

    # 商品
    goods: Optional[GoodsReq] = None

    # 商户指定订单过期时间戳，毫秒为单位
    order_expire_time: int = Field(0, alias='orderExpireTime')

    # 支付完成回调地址
    return_url: Optional[str] = Field(None, alias='returnUrl')

    # 取消支付回调地址
    cancel_url: Optional[str] = Field(None, alias='cancelUrl')

    # 支付者在商户平台注册时的唯一ID
    merchant_user_id: int = Field(0, alias='merchantUserId')

    # 所选链名字
    chain: Optional[str] = None

    # 包含链名字的币种字段，对应到具体链的具体币种
    full_curr_type: Optional[str] = Field(None, alias='fullCurrType')

    # 客户名称
    channel_id: Optional[str] = Field(None, alias='channelId')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class CreateOrderReq(BaseRequest):
    """
    创建订单请求
    """

    def __init__(self):
        """
        初始化CreateOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.ADDRESS_CREATE_ORDER  # 需要根据实际GatePayApi定义调整

        # 使用内部数据模型
        self._data = CreateOrderReqData()

        # 商户系统中的交易号
        self.merchant_trade_no = None

        self.fiat_currency = None

        self.fiat_amount = None

        # 订单币种
        self.currency = None

        # 订单金额
        self.order_amount = None

        # 用户承担手续费 非必传
        self.surcharge_amount = None

        # 非地址支付的payCurrency在实际付款时确定，地址支付的payCurrency在下单时候确定
        self.pay_currency = None

        # 真实币种
        self.actual_currency = None

        # 交易来源，可选值：APP、WEB、WAP、MINIAPP、OTHERS
        self.env = None

        # 商品
        self.goods = None

        # 商户指定订单过期时间戳，毫秒为单位
        self.order_expire_time = 0

        # 支付完成回调地址
        self.return_url = None

        # 取消支付回调地址
        self.cancel_url = None

        # 支付者在商户平台注册时的唯一ID
        self.merchant_user_id = 0

        # 所选链名字
        self.chain = None

        # 包含链名字的币种字段，对应到具体链的具体币种
        self.full_curr_type = None

        # 客户名称
        self.channel_id = None

    def get_merchant_trade_no(self) -> str:
        """
        获取商户系统中的交易号

        Returns:
            str: 商户交易号
        """
        return self.merchant_trade_no

    def set_merchant_trade_no(self, merchant_trade_no: str):
        """
        设置商户系统中的交易号

        Args:
            merchant_trade_no (str): 商户交易号
        """
        self.merchant_trade_no = merchant_trade_no
        self._data.merchant_trade_no = merchant_trade_no

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
        self._data.currency = currency

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
        self._data.order_amount = order_amount

    def get_surcharge_amount(self) -> str:
        """
        获取用户承担手续费

        Returns:
            str: 用户承担手续费
        """
        return self.surcharge_amount

    def set_surcharge_amount(self, surcharge_amount: str):
        """
        用户承担手续费

        Args:
            surcharge_amount (str): 用户承担手续费
        """
        self.surcharge_amount = surcharge_amount
        self._data.surcharge_amount = surcharge_amount

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
        self._data.pay_currency = pay_currency

    def get_actual_currency(self) -> str:
        """
        获取真实币种

        Returns:
            str: 真实币种
        """
        return self.actual_currency

    def set_actual_currency(self, actual_currency: str):
        """
        设置真实币种

        Args:
            actual_currency (str): 真实币种
        """
        self.actual_currency = actual_currency
        self._data.actual_currency = actual_currency

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
        self._data.env = env

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
        self._data.goods = goods

    def get_order_expire_time(self) -> int:
        """
        获取订单过期时间戳

        Returns:
            int: 订单过期时间戳（毫秒）
        """
        return self.order_expire_time

    def set_order_expire_time(self, order_expire_time: int):
        """
        设置订单过期时间戳

        Args:
            order_expire_time (int): 订单过期时间戳（毫秒）
        """
        self.order_expire_time = order_expire_time
        self._data.order_expire_time = order_expire_time

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
        self._data.return_url = return_url

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
        self._data.cancel_url = cancel_url

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
        self._data.merchant_user_id = merchant_user_id

    def get_chain(self) -> str:
        """
        获取所选链名字

        Returns:
            str: 所选链名字
        """
        return self.chain

    def set_chain(self, chain: str):
        """
        设置所选链名字

        Args:
            chain (str): 所选链名字
        """
        self.chain = chain
        self._data.chain = chain

    def get_full_curr_type(self) -> str:
        """
        获取包含链名字的币种字段

        Returns:
            str: 包含链名字的币种字段
        """
        return self.full_curr_type

    def set_full_curr_type(self, full_curr_type: str):
        """
        设置包含链名字的币种字段

        Args:
            full_curr_type (str): 包含链名字的币种字段
        """
        self.full_curr_type = full_curr_type
        self._data.full_curr_type = full_curr_type

    def get_channel_id(self) -> str:
        """
        获取客户名称

        Returns:
            str: 客户名称
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str):
        """
        设置客户名称

        Args:
            channel_id (str): 客户名称
        """
        self.channel_id = channel_id
        self._data.channel_id = channel_id

    def set_fiat_amount(self, fiat_amount: str):
        """

        :param fiat_amount:
        :return:
        """
        self.fiat_amount = fiat_amount
        self._data.fiat_amount = fiat_amount

    def set_fiat_currency(self, fiat_currency: str):
        """

        :param fiat_currency:
        :return:
        """
        self.fiat_currency = fiat_currency
        self._data.fiat_currency = fiat_currency

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输
        """
        # 使用Pydantic的dict方法并启用by_alias选项
        result = self._data.dict(by_alias=True, exclude_none=True, exclude_defaults=True)
        if self.env is not None:
            result['env'] = self.env.to_dict()
        if self.goods is not None:
            result['goods'] = self.goods.to_dict()

        # 添加父类字段
        result.update(self.get_dicts())

        return result

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateOrderReq(merchant_trade_no={self.merchant_trade_no}, "
                f"currency={self.currency}, order_amount={self.order_amount}, "
                f"surcharge_amount={self.surcharge_amount}, "
                f"pay_currency={self.pay_currency}, actual_currency={self.actual_currency}, "
                f"env={self.env}, goods={self.goods}, order_expire_time={self.order_expire_time}, "
                f"return_url={self.return_url}, cancel_url={self.cancel_url}, "
                f"merchant_user_id={self.merchant_user_id}, chain={self.chain}, "
                f"full_curr_type={self.full_curr_type}, channel_id={self.channel_id})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
