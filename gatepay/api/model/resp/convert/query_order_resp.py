import decimal
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class QueryOrderResp(BaseResponse):
    """
    查询闪兑订单响应
    """

    def __init__(self):
        """
        初始化QueryOrderResp对象
        """
        super().__init__()

        self.order_id = None
        self.user_id = 0
        self.sell_currency = None
        self.buy_currency = None
        self.sell_amount = None
        self.buy_amount = None
        self.status = 0
        self.rate = None
        self.quote_id = None
        self.create_time = 0

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

    def get_user_id(self) -> int:
        """
        获取用户ID

        Returns:
            int: 用户ID
        """
        return self.user_id

    def set_user_id(self, user_id: int):
        """
        设置用户ID

        Args:
            user_id (int): 用户ID
        """
        self.user_id = user_id

    def get_sell_currency(self) -> str:
        """
        获取出售币种

        Returns:
            str: 出售币种
        """
        return self.sell_currency

    def set_sell_currency(self, sell_currency: str):
        """
        设置出售币种

        Args:
            sell_currency (str): 出售币种
        """
        self.sell_currency = sell_currency

    def get_buy_currency(self) -> str:
        """
        获取购买币种

        Returns:
            str: 购买币种
        """
        return self.buy_currency

    def set_buy_currency(self, buy_currency: str):
        """
        设置购买币种

        Args:
            buy_currency (str): 购买币种
        """
        self.buy_currency = buy_currency

    def get_sell_amount(self) -> str:
        """
        获取出售数量

        Returns:
            str: 出售数量
        """
        return self.sell_amount

    def set_sell_amount(self, sell_amount: str):
        """
        设置出售数量

        Args:
            sell_amount (str): 出售数量
        """
        self.sell_amount = sell_amount

    def get_buy_amount(self) -> str:
        """
        获取购买数量

        Returns:
            str: 购买数量
        """
        return self.buy_amount

    def set_buy_amount(self, buy_amount: str):
        """
        设置购买数量

        Args:
            buy_amount (str): 购买数量
        """
        self.buy_amount = buy_amount

    def get_status_(self) -> int:
        """
        获取状态

        Returns:
            int: 状态
        """
        return self.status

    def set_status(self, status: int):
        """
        设置状态

        Args:
            status (int): 状态
        """
        self.status = status

    def get_rate(self) -> decimal:
        """
        获取汇率

        Returns:
            Decimal: 汇率
        """
        return self.rate

    def set_rate(self, rate: decimal):
        """
        设置汇率

        Args:
            rate (Decimal): 汇率
        """
        self.rate = rate

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

    def get_create_time(self) -> int:
        """
        获取创建时间

        Returns:
            int: 创建时间（毫秒时间戳）
        """
        return self.create_time

    def set_create_time(self, create_time: int):
        """
        设置创建时间

        Args:
            create_time (int): 创建时间（毫秒时间戳）
        """
        self.create_time = create_time

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return (f"QueryOrderResp(order_id={self.order_id}, user_id={self.user_id}, "
                f"sell_currency={self.sell_currency}, buy_currency={self.buy_currency}, "
                f"sell_amount={self.sell_amount}, buy_amount={self.buy_amount}, "
                f"status={self.status}, rate={self.rate}, quote_id={self.quote_id}, "
                f"create_time={self.create_time})")

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
