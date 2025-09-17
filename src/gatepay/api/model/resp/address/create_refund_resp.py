from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class CreateRefundResp(BaseResponse):
    """
    地址支付创建退款响应
    """

    def __init__(self):
        """
        初始化CreateRefundResp对象
        """
        super().__init__()

        # 商户退款请求id
        self.refund_request_id = None

        # 拟退款的订单id
        self.prepay_id = None

        # 订单金额
        self.order_amount = None

        # 退款金额
        self.refund_amount = None

    def get_refund_request_id(self) -> str:
        """
        获取商户退款请求ID

        Returns:
            str: 商户退款请求ID
        """
        return self.refund_request_id

    def set_refund_request_id(self, refund_request_id: str):
        """
        设置商户退款请求ID

        Args:
            refund_request_id (str): 商户退款请求ID
        """
        self.refund_request_id = refund_request_id

    def get_prepay_id(self) -> str:
        """
        获取拟退款的订单ID

        Returns:
            str: 拟退款的订单ID
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str):
        """
        设置拟退款的订单ID

        Args:
            prepay_id (str): 拟退款的订单ID
        """
        self.prepay_id = prepay_id

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

    def get_refund_amount(self) -> str:
        """
        获取退款金额

        Returns:
            str: 退款金额
        """
        return self.refund_amount

    def set_refund_amount(self, refund_amount: str):
        """
        设置退款金额

        Args:
            refund_amount (str): 退款金额
        """
        self.refund_amount = refund_amount

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateRefundResp(refund_request_id={self.refund_request_id}, prepay_id={self.prepay_id}, "
                f"order_amount={self.order_amount}, refund_amount={self.refund_amount})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
