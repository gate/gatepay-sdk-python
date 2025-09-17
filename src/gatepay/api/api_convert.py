

from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.query_currency_req import QueryCurrencyReq
from src.gatepay.api.model.req.query_pair_req import QueryPairReq
from src.gatepay.api.model.req.preview_req import PreviewReq
from src.gatepay.api.model.req.convert.create_order_req import CreateOrderReq
from src.gatepay.api.model.req.convert.query_order_req import QueryOrderReq
from src.gatepay.api.model.resp.query_currency_resp import QueryCurrencyResp
from src.gatepay.api.model.resp.query_pair_resp import QueryPairResp
from src.gatepay.api.model.resp.preview_resp import PreviewResp
from src.gatepay.api.model.resp.convert.create_order_resp import CreateOrderResp
from src.gatepay.api.model.resp.convert.query_order_resp import QueryOrderResp
from src.gatepay.gatepay_config import GatePayConfig


class ApiConvert(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiConvert 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def query_currency(self, request: QueryCurrencyReq) -> QueryCurrencyResp:
        """
        查询可用闪兑币种

        :param request: 查询币种请求参数
        :return: 查询币种响应结果
        """
        return super().process(request, QueryCurrencyResp)

    def query_pair(self, request: QueryPairReq) -> QueryPairResp:
        """
        查询可用币种对

        :param request: 查询币种对请求参数
        :return: 查询币种对响应结果
        """
        return super().process(request, QueryPairResp)

    def preview(self, request: PreviewReq) -> PreviewResp:
        """
        预览报价

        :param request: 预览请求参数
        :return: 预览响应结果
        """
        return super().process(request, PreviewResp)

    def create_order(self, request: CreateOrderReq) -> CreateOrderResp:
        """
        闪兑下单

        :param request: 创建订单请求参数
        :return: 创建订单响应结果
        """
        return super().process(request, CreateOrderResp)

    def query_order(self, request: QueryOrderReq) -> QueryOrderResp:
        """
        查询闪兑订单

        :param request: 查询订单请求参数
        :return: 查询订单响应结果
        """
        return super().process(request, QueryOrderResp)
