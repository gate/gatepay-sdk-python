from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi

class QueryOrderReq(BaseRequest):
    """
    支付查询订单请求
    """

    def __init__(self):
        """
        初始化QueryOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_QUERY_ORDER  # 需要根据实际GatePayApi定义调整

        self.prepay_id = None
        self.merchant_trade_no = None

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

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return f"QueryOrderReq(prepay_id={self.prepay_id}, merchant_trade_no={self.merchant_trade_no})"

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
