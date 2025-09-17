from dataclasses import dataclass
from typing import Optional

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class QueryOrdersReq(BaseRequest):

    start_time: int = 0
    end_time: int = 0
    page: int = 0
    count: int = 0
    currency: Optional[str] = None
    order_type: Optional[str] = None
    order_id_no: Optional[str] = None
    financial_type: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.BILL_QUERY_ORDERS

    def get_start_time(self) -> int:
        """
        获取开始时间

        :return: 开始时间戳
        """
        return self.start_time

    def set_start_time(self, start_time: int) -> None:
        """
        设置开始时间

        :param start_time: 开始时间戳
        """
        self.start_time = start_time

    def get_end_time(self) -> int:
        """
        获取结束时间

        :return: 结束时间戳
        """
        return self.end_time

    def set_end_time(self, end_time: int) -> None:
        """
        设置结束时间

        :param end_time: 结束时间戳
        """
        self.end_time = end_time

    def get_count(self) -> int:
        """
        获取查询数量

        :return: 查询数量
        """
        return self.count

    def set_count(self, count: int) -> None:
        """
        设置查询数量

        :param count: 查询数量
        """
        self.count = count

    def get_page(self) -> int:
        """
        获取页码

        :return: 页码
        """
        return self.page

    def set_page(self, page: int) -> None:
        """
        设置页码

        :param page: 页码
        """
        self.page = page

    def get_currency(self) -> Optional[str]:
        """
        获取币种

        :return: 币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置币种

        :param currency: 币种
        """
        self.currency = currency

    def get_order_type(self) -> Optional[str]:
        """
        获取订单类型

        :return: 订单类型
        """
        return self.order_type

    def set_order_type(self, order_type: str) -> None:
        """
        设置订单类型

        :param order_type: 订单类型
        """
        self.order_type = order_type

    def get_order_id_no(self) -> Optional[str]:
        """
        获取订单编号

        :return: 订单编号
        """
        return self.order_id_no

    def set_order_id_no(self, order_id_no: str) -> None:
        """
        设置订单编号

        :param order_id_no: 订单编号
        """
        self.order_id_no = order_id_no

    def get_financial_type(self) -> Optional[str]:
        """
        获取财务类型

        :return: 财务类型
        """
        return self.financial_type

    def set_financial_type(self, financial_type: str) -> None:
        """
        设置财务类型

        :param financial_type: 财务类型
        """
        self.financial_type = financial_type
