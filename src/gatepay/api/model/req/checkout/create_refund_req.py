from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi

class CreateRefundReq(BaseRequest):
    """
    收银台创建退款请求
    """

    def __init__(self):
        """
        初始化CreateRefundReq对象
        """
        super().__init__()
        self.api = GatePayApi.CHECKOUT_CREATE_REFUND  # 需要根据实际GatePayApi定义调整

        self.refund_request_id = None
        self.prepay_id = None
        self.refund_order_currency = None
        self.refund_order_amount = None
        self.refund_pay_currency = None
        self.refund_pay_amount = None
        self.refund_reason = None
        self.receiver_id = 0

    def get_refund_request_id(self) -> str:
        """
        获取退款请求ID

        Returns:
            str: 退款请求ID
        """
        return self.refund_request_id

    def set_refund_request_id(self, refund_request_id: str):
        """
        设置退款请求ID

        Args:
            refund_request_id (str): 退款请求ID
        """
        self.refund_request_id = refund_request_id

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

    def get_refund_order_currency(self) -> str:
        """
        获取退款订单币种

        Returns:
            str: 退款订单币种
        """
        return self.refund_order_currency

    def set_refund_order_currency(self, refund_order_currency: str):
        """
        设置退款订单币种

        Args:
            refund_order_currency (str): 退款订单币种
        """
        self.refund_order_currency = refund_order_currency

    def get_refund_order_amount(self) -> str:
        """
        获取退款订单金额

        Returns:
            str: 退款订单金额
        """
        return self.refund_order_amount

    def set_refund_order_amount(self, refund_order_amount: str):
        """
        设置退款订单金额

        Args:
            refund_order_amount (str): 退款订单金额
        """
        self.refund_order_amount = refund_order_amount

    def get_refund_pay_currency(self) -> str:
        """
        获取退款支付币种

        Returns:
            str: 退款支付币种
        """
        return self.refund_pay_currency

    def set_refund_pay_currency(self, refund_pay_currency: str):
        """
        设置退款支付币种

        Args:
            refund_pay_currency (str): 退款支付币种
        """
        self.refund_pay_currency = refund_pay_currency

    def get_refund_pay_amount(self) -> str:
        """
        获取退款支付金额

        Returns:
            str: 退款支付金额
        """
        return self.refund_pay_amount

    def set_refund_pay_amount(self, refund_pay_amount: str):
        """
        设置退款支付金额

        Args:
            refund_pay_amount (str): 退款支付金额
        """
        self.refund_pay_amount = refund_pay_amount

    def get_refund_reason(self) -> str:
        """
        获取退款原因

        Returns:
            str: 退款原因
        """
        return self.refund_reason

    def set_refund_reason(self, refund_reason: str):
        """
        设置退款原因

        Args:
            refund_reason (str): 退款原因
        """
        self.refund_reason = refund_reason

    def get_receiver_id(self) -> int:
        """
        获取接收者ID

        Returns:
            int: 接收者ID
        """
        return self.receiver_id

    def set_receiver_id(self, receiver_id: int):
        """
        设置接收者ID

        Args:
            receiver_id (int): 接收者ID
        """
        self.receiver_id = receiver_id

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateRefundReq(refund_request_id={self.refund_request_id}, prepay_id={self.prepay_id}, "
                f"refund_order_currency={self.refund_order_currency}, refund_order_amount={self.refund_order_amount}, "
                f"refund_pay_currency={self.refund_pay_currency}, refund_pay_amount={self.refund_pay_amount}, "
                f"refund_reason={self.refund_reason}, receiver_id={self.receiver_id})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
