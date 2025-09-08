from gatepay.base_response import BaseResponse
from gatepay.api.model.chain import Chain


class  CreateOrderResp(BaseResponse):
    """
    创建订单响应
    """

    def __init__(self):
        """
        初始化CreateOrderResp对象
        """
        super().__init__()

        # 创建的支付单order id
        self.prepay_id = None

        # 创建订单的终端类型
        self.terminal_type = None

        # 过期毫秒时间戳
        self.expire_time = 0

        # 地址支付支付单绑定的链和地址
        self.chain = None

    def get_prepay_id(self) -> str:
        """
        获取支付单order id

        Returns:
            str: 支付单order id
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str):
        """
        设置支付单order id

        Args:
            prepay_id (str): 支付单order id
        """
        self.prepay_id = prepay_id

    def get_terminal_type(self) -> str:
        """
        获取创建订单的终端类型

        Returns:
            str: 终端类型
        """
        return self.terminal_type

    def set_terminal_type(self, terminal_type: str):
        """
        设置创建订单的终端类型

        Args:
            terminal_type (str): 终端类型
        """
        self.terminal_type = terminal_type

    def get_expire_time(self) -> int:
        """
        获取过期毫秒时间戳

        Returns:
            int: 过期时间戳（毫秒）
        """
        return self.expire_time

    def set_expire_time(self, expire_time: int):
        """
        设置过期毫秒时间戳

        Args:
            expire_time (int): 过期时间戳（毫秒）
        """
        self.expire_time = expire_time

    def get_chain(self) -> Chain:
        """
        获取地址支付支付单绑定的链和地址

        Returns:
            Chain: 链和地址信息
        """
        return self.chain

    def set_chain(self, chain: Chain):
        """
        设置地址支付支付单绑定的链和地址

        Args:
            chain (Chain): 链和地址信息
        """
        self.chain = chain

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateOrderResp(prepay_id={self.prepay_id}, "
                f"terminal_type={self.terminal_type}, expire_time={self.expire_time}, "
                f"chain={self.chain})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
