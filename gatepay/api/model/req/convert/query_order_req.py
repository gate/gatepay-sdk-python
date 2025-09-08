from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi

class QueryOrderReq(BaseRequest):
    """
    闪兑查询订单请求
    """

    def __init__(self):
        """
        初始化QueryOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.CONVERT_QUERY_ORDER  # 需要根据实际GatePayApi定义调整

        # 订单id
        self.order_id = None

    def get_order_id(self) -> str:
        """
        获取订单ID

        Returns:
            str: 订单ID
        """
        return self.order_id

    def set_order_id(self, order_id: str):
        """
        设置订单ID

        Args:
            order_id (str): 订单ID
        """
        self.order_id = order_id

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return f"QueryOrderReq(order_id={self.order_id})"

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
