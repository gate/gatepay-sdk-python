from src.gatepay.base_response import BaseResponse
from src.gatepay.api.model.chain import Chain


class CreateOrderResp(BaseResponse):
    """
    收银台创建订单响应
    """

    def __init__(self):
        """
        初始化CreateOrderResp对象
        """
        super().__init__()

        self.prepay_id = None
        self.terminal_type = None
        self.expire_time = 0
        self.qr_content = None
        self.location = None
        self.pay_currency = None
        self.pay_amount = None
        self.chain = None
        self.app_name = None
        self.app_logo = None
        self.goods_name = None
        self.in_usdt = None

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

    def get_terminal_type(self) -> str:
        """
        获取终端类型

        Returns:
            str: 终端类型
        """
        return self.terminal_type

    def set_terminal_type(self, terminal_type: str):
        """
        设置终端类型

        Args:
            terminal_type (str): 终端类型
        """
        self.terminal_type = terminal_type

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

    def get_qr_content(self) -> str:
        """
        获取二维码内容

        Returns:
            str: 二维码内容
        """
        return self.qr_content

    def set_qr_content(self, qr_content: str):
        """
        设置二维码内容

        Args:
            qr_content (str): 二维码内容
        """
        self.qr_content = qr_content

    def get_location(self) -> str:
        """
        获取位置信息

        Returns:
            str: 位置信息
        """
        return self.location

    def set_location(self, location: str):
        """
        设置位置信息

        Args:
            location (str): 位置信息
        """
        self.location = location

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

    def get_chain(self) -> Chain:
        """
        获取链信息

        Returns:
            Chain: 链信息
        """
        return self.chain

    def set_chain(self, chain: Chain):
        """
        设置链信息

        Args:
            chain (Chain): 链信息
        """
        self.chain = chain

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

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateOrderResp(prepay_id={self.prepay_id}, terminal_type={self.terminal_type}, "
                f"expire_time={self.expire_time}, qr_content={self.qr_content}, location={self.location}, "
                f"pay_currency={self.pay_currency}, pay_amount={self.pay_amount}, chain={self.chain}, "
                f"app_name={self.app_name}, app_logo={self.app_logo}, goods_name={self.goods_name}, "
                f"in_usdt={self.in_usdt})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
