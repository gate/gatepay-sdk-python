from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi

class CreateRefundReq(BaseRequest):
    """
    支付创建退款请求
    """

    def __init__(self):
        """
        初始化CreateRefundReq对象
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_CREATE_REFUND  # 需要根据实际GatePayApi定义调整

        self.refund_request_id = None
        self.prepay_id = None
        self.refund_amount = None
        self.refund_reason = None

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

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateRefundReq(refund_request_id={self.refund_request_id}, prepay_id={self.prepay_id}, "
                f"refund_amount={self.refund_amount}, refund_reason={self.refund_reason})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
