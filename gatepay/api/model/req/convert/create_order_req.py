from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi

class CreateOrderReq(BaseRequest):
    """
    闪兑创建订单请求
    """

    def __init__(self):
        """
        初始化CreateOrderReq对象
        """
        super().__init__()
        self.api = GatePayApi.CONVERT_CREATE_ORDER  # 需要根据实际GatePayApi定义调整

        self.client_req_id = None
        self.quote_id = None
        self.sell_currency = None
        self.sell_amount = None
        self.buy_currency = None
        self.buy_amount = None
        self.price = None

    def get_client_req_id(self) -> str:
        """
        获取客户端请求ID

        Returns:
            str: 客户端请求ID
        """
        return self.client_req_id

    def set_client_req_id(self, client_req_id: str):
        """
        设置客户端请求ID

        Args:
            client_req_id (str): 客户端请求ID
        """
        self.client_req_id = client_req_id

    def get_quote_id(self) -> str:
        """
        获取报价ID

        Returns:
            str: 报价ID
        """
        return self.quote_id

    def set_quote_id(self, quote_id: str):
        """
        设置报价ID

        Args:
            quote_id (str): 报价ID
        """
        self.quote_id = quote_id

    def get_sell_currency(self) -> str:
        """
        获取卖出币种

        Returns:
            str: 卖出币种
        """
        return self.sell_currency

    def set_sell_currency(self, sell_currency: str):
        """
        设置卖出币种

        Args:
            sell_currency (str): 卖出币种
        """
        self.sell_currency = sell_currency

    def get_sell_amount(self) -> str:
        """
        获取卖出金额

        Returns:
            str: 卖出金额
        """
        return self.sell_amount

    def set_sell_amount(self, sell_amount: str):
        """
        设置卖出金额

        Args:
            sell_amount (str): 卖出金额
        """
        self.sell_amount = sell_amount

    def get_buy_currency(self) -> str:
        """
        获取买入币种

        Returns:
            str: 买入币种
        """
        return self.buy_currency

    def set_buy_currency(self, buy_currency: str):
        """
        设置买入币种

        Args:
            buy_currency (str): 买入币种
        """
        self.buy_currency = buy_currency

    def get_buy_amount(self) -> str:
        """
        获取买入金额

        Returns:
            str: 买入金额
        """
        return self.buy_amount

    def set_buy_amount(self, buy_amount: str):
        """
        设置买入金额

        Args:
            buy_amount (str): 买入金额
        """
        self.buy_amount = buy_amount

    def get_price(self) -> str:
        """
        获取价格

        Returns:
            str: 价格
        """
        return self.price

    def set_price(self, price: str):
        """
        设置价格

        Args:
            price (str): 价格
        """
        self.price = price

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"CreateOrderReq(client_req_id={self.client_req_id}, quote_id={self.quote_id}, "
                f"sell_currency={self.sell_currency}, sell_amount={self.sell_amount}, "
                f"buy_currency={self.buy_currency}, buy_amount={self.buy_amount}, price={self.price})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
