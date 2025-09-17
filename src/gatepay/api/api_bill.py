from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.query_orders_req import QueryOrdersReq
from src.gatepay.api.model.resp.query_orders_resp import QueryOrdersResp
from src.gatepay.gatepay_config import GatePayConfig


class ApiBill(BaseApi):

    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiBill 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def query_orders(self, request: QueryOrdersReq) -> QueryOrdersResp:
        """
        查询账单

        :param request: 查询请求参数
        :return: 查询响应结果
        """
        return super().process(request, QueryOrdersResp)
