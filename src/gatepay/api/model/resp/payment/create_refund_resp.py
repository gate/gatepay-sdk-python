from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class CreateRefundResp(BaseResponse):
    """
    支付创建退款响应
    """

    def __init__(self):
        """
        初始化CreateRefundResp对象
        """
        super().__init__()

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return "CreateRefundResp()"

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
