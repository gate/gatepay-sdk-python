from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.close_order_req import CloseOrderReq
from src.gatepay.api.model.req.create_batch_transfer_req import CreateBatchTransferReq
from src.gatepay.api.model.req.payment.create_order_req import CreateOrderReq
from src.gatepay.api.model.req.payment.create_refund_req import CreateRefundReq
from src.gatepay.api.model.req.payment.create_refund_req_v3 import CreateRefundReqV3
from src.gatepay.api.model.req.payment.query_balance_req import QueryBalanceReq
from src.gatepay.api.model.req.payment.query_order_req import QueryOrderReq
from src.gatepay.api.model.req.payment.query_order_req_v3 import QueryOrderReqV3
from src.gatepay.api.model.req.payment.query_refund_req_v3 import QueryRefundReqV3
from src.gatepay.api.model.req.payment.query_refund_support_chains_req import QueryRefundSupportChainsReqV3
from src.gatepay.api.model.req.query_batch_transfer_req import QueryBatchTransferReq
from src.gatepay.api.model.req.payment.query_refund_req import QueryRefundReq
from src.gatepay.api.model.resp.close_order_resp import CloseOrderResp
from src.gatepay.api.model.resp.create_batch_transfer_resp import CreateBatchTransferResp
from src.gatepay.api.model.resp.create_refund_resp import CreateRefundResp
from src.gatepay.api.model.resp.payment.create_order_resp import CreateOrderResp
from src.gatepay.api.model.resp.payment.create_refund_resp_v3 import CreateRefundRespV3
from src.gatepay.api.model.resp.payment.query_balance_resp import QueryBalanceResp
from src.gatepay.api.model.resp.payment.query_order_resp import QueryOrderResp
from src.gatepay.api.model.resp.payment.query_order_resp_v3 import QueryOrderRespV3
from src.gatepay.api.model.resp.payment.query_refund_resp_v3 import QueryRefundRespV3
from src.gatepay.api.model.resp.query_batch_transfer_resp import QueryBatchTransferResp
from src.gatepay.api.model.resp.payment.query_refund_resp import QueryRefundResp
from src.gatepay.gatepay_config import GatePayConfig

from src.gatepay.api.model.resp.chains_resp import ChainsResp


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

    def query_order_v3(self, request: QueryOrderReqV3) -> QueryOrderRespV3:
        """
        查询订单V3

        :param request: 查询订单请求参数
        :return: 查询订单响应结果
        """
        return super().process(request, QueryOrderRespV3)

    def query_refund_support_chain(self, request: QueryRefundSupportChainsReqV3) -> ChainsResp:
        """
        退款到 Web3 支持的网络和费率查询

        :param request: 查询退款请求参数
        :return: 查询退款到链上响应结果
        """
        return super().process(request, ChainsResp)

    def create_refund_v3(self, request: CreateRefundReqV3) -> CreateRefundRespV3:
        """
        创建退款订单V3

        :param request: 创建退款请求参数
        :return: 创建退款响应结果
        """
        return super().process(request, CreateRefundRespV3)

    def query_refund_v3(self, request: QueryRefundReqV3) -> QueryRefundRespV3:
        """
        查询退款订单V3

        :param request: 查询退款请求参数
        :return: 查询退款响应结果
        """
        return super().process(request, QueryRefundRespV3)
