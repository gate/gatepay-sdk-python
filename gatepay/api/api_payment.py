from gatepay.api.base_api import BaseApi
from gatepay.api.model.req.close_order_req import CloseOrderReq
from gatepay.api.model.req.create_batch_transfer_req import CreateBatchTransferReq
from gatepay.api.model.req.payment.create_order_req import CreateOrderReq
from gatepay.api.model.req.payment.create_refund_req import CreateRefundReq
from gatepay.api.model.req.payment.query_order_req import QueryOrderReq
from gatepay.api.model.req.payment.query_balance_req import QueryBalanceReq
from gatepay.api.model.req.query_batch_transfer_req import QueryBatchTransferReq
from gatepay.api.model.req.query_refund_req import QueryRefundReq
from gatepay.api.model.resp.close_order_resp import CloseOrderResp
from gatepay.api.model.resp.create_batch_transfer_resp import CreateBatchTransferResp
from gatepay.api.model.resp.create_refund_resp import CreateRefundResp
from gatepay.api.model.resp.payment.create_order_resp import CreateOrderResp
from gatepay.api.model.resp.payment.query_balance_resp import QueryBalanceResp
from gatepay.api.model.resp.query_batch_transfer_resp import QueryBatchTransferResp
from gatepay.api.model.resp.payment.query_order_resp import QueryOrderResp
from gatepay.api.model.resp.query_refund_resp import QueryRefundResp
from gatepay.gatepay_config import GatePayConfig


class ApiPayment(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiPayment 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def create_order(self, request: CreateOrderReq) -> CreateOrderResp:
        """
        创建订单

        :param request: 创建订单请求参数
        :return: 创建订单响应结果
        """
        return super().process(request, CreateOrderResp)

    def query_order(self, request: QueryOrderReq) -> QueryOrderResp:
        """
        查询订单

        :param request: 查询订单请求参数
        :return: 查询订单响应结果
        """
        return super().process(request, QueryOrderResp)

    def close_order(self, request: CloseOrderReq) -> CloseOrderResp:
        """
        关闭订单

        :param request: 关闭订单请求参数
        :return: 关闭订单响应结果
        """
        return super().process(request, CloseOrderResp)

    def create_refund(self, request: CreateRefundReq) -> CreateRefundResp:
        """
        创建退款订单

        :param request: 创建退款请求参数
        :return: 创建退款响应结果
        """
        return super().process(request, CreateRefundResp)

    def query_refund(self, request: QueryRefundReq) -> QueryRefundResp:
        """
        查询退款订单

        :param request: 查询退款请求参数
        :return: 查询退款响应结果
        """
        return super().process(request, QueryRefundResp)

    def create_batch_transfer(self, request: CreateBatchTransferReq) -> CreateBatchTransferResp:
        """
        创建批量转账

        :param request: 创建批量转账请求参数
        :return: 创建批量转账响应结果
        """
        return super().process(request, CreateBatchTransferResp)

    def query_batch_transfer(self, request: QueryBatchTransferReq) -> QueryBatchTransferResp:
        """
        查询批量转账

        :param request: 查询批量转账请求参数
        :return: 查询批量转账响应结果
        """
        return super().process(request, QueryBatchTransferResp)

    def query_balance(self, request: QueryBalanceReq) -> QueryBalanceResp:
        """
        查询余额

        :param request: 查询余额请求参数
        :return: 查询余额响应结果
        """
        return super().process(request, QueryBalanceResp)
