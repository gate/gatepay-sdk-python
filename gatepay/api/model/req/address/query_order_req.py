from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi

class QueryOrderReq(BaseRequest):
    """
    查询支付单请求
    """

    def __init__(self):
        """
        初始化QueryOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.ADDRESS_QUERY_ORDER  # 需要根据实际GatePayApi定义调整

        # 地址支付预支付单id
        self.prepay_id = None

        # 商户系统交易号
        self.merchant_trade_no = None

    def get_prepay_id(self) -> str:
        """
        获取地址支付预支付单id

        Returns:
            str: 预支付单id
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str):
        """
        设置地址支付预支付单id

        Args:
            prepay_id (str): 预支付单id
        """
        self.prepay_id = prepay_id

    def get_merchant_trade_no(self) -> str:
        """
        获取商户系统交易号

        Returns:
            str: 商户系统交易号
        """
        return self.merchant_trade_no

    def set_merchant_trade_no(self, merchant_trade_no: str):
        """
        设置商户系统交易号

        Args:
            merchant_trade_no (str): 商户系统交易号
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
