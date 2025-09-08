from dataclasses import dataclass

from gatepay.base_response import BaseResponse

@dataclass
class CreateRefundResp(BaseResponse):
    """
    收银台创建退款响应
    """

    def __init__(self):
        """
        初始化CreateRefundResp对象
        """
        super().__init__()

        self.refund_request_id = None  # 商户退款请求id
        self.prepay_id = None  # 拟退款的订单id
        self.order_currency = None  # 订单币种
        self.order_amount = None  # 订单金额
        self.refund_order_amount = None  # 退款商户已收到的用户支付的全部金额
        self.pay_currency = None  # 用户支付币种
        self.pay_amount = None  # 订单中用户应该支付的金额
        self.refund_pay_amount = None  # 用户支付后，退款残留于链上的金额。商户没有收到这部分资金（闪兑场景）

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

    def get_order_currency(self) -> str:
        """
        获取订单币种

        Returns:
            str: 订单币种
        """
        return self.order_currency

    def set_order_currency(self, order_currency: str):
        """
        设置订单币种

        Args:
            order_currency (str): 订单币种
        """
        self.order_currency = order_currency

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

    def get_refund_order_amount(self) -> str:
        """
        获取退款商户已收到的用户支付的全部金额

        Returns:
            str: 退款商户已收到的用户支付的全部金额
        """
        return self.refund_order_amount

    def set_refund_order_amount(self, refund_order_amount: str):
        """
        设置退款商户已收到的用户支付的全部金额

        Args:
            refund_order_amount (str): 退款商户已收到的用户支付的全部金额
        """
        self.refund_order_amount = refund_order_amount

    def get_pay_currency(self) -> str:
        """
        获取用户支付币种

        Returns:
            str: 用户支付币种
        """
        return self.pay_currency

    def set_pay_currency(self, pay_currency: str):
        """
        设置用户支付币种

        Args:
            pay_currency (str): 用户支付币种
        """
        self.pay_currency = pay_currency

    def get_pay_amount(self) -> str:
        """
        获取订单中用户应该支付的金额

        Returns:
            str: 订单中用户应该支付的金额
        """
        return self.pay_amount

    def set_pay_amount(self, pay_amount: str):
        """
        设置订单中用户应该支付的金额

        Args:
            pay_amount (str): 订单中用户应该支付的金额
        """
        self.pay_amount = pay_amount

    def get_refund_pay_amount(self) -> str:
        """
        获取用户支付后，退款残留于链上的金额。商户没有收到这部分资金（闪兑场景）

        Returns:
            str: 用户支付后，退款残留于链上的金额
        """
        return self.refund_pay_amount

    def set_refund_pay_amount(self, refund_pay_amount: str):
        """
        设置用户支付后，退款残留于链上的金额。商户没有收到这部分资金（闪兑场景）

        Args:
            refund_pay_amount (str): 用户支付后，退款残留于链上的金额
        """
        self.refund_pay_amount = refund_pay_amount

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateRefundResp(refund_request_id={self.refund_request_id}, prepay_id={self.prepay_id}, "
                f"order_currency={self.order_currency}, order_amount={self.order_amount}, "
                f"refund_order_amount={self.refund_order_amount}, pay_currency={self.pay_currency}, "
                f"pay_amount={self.pay_amount}, refund_pay_amount={self.refund_pay_amount})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
