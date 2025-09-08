from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class CreateOrderResp(BaseResponse):
    """
    二维码创建订单响应
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

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateOrderResp(prepay_id={self.prepay_id}, terminal_type={self.terminal_type}, "
                f"expire_time={self.expire_time}, qr_content={self.qr_content}, location={self.location})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
