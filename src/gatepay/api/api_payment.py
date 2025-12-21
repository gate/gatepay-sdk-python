from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.payment.create_order_req import CreateOrderReq
from src.gatepay.api.model.req.payment.query_order_req import QueryOrderReq
from src.gatepay.api.model.resp.chains_resp import ChainsResp
from src.gatepay.api.model.resp.close_order_resp import CloseOrderResp
from src.gatepay.api.model.resp.create_batch_transfer_resp import CreateBatchTransferResp
from src.gatepay.api.model.resp.create_refund_resp import CreateRefundResp
from src.gatepay.api.model.resp.payment.create_order_resp import CreateOrderResp
from src.gatepay.api.model.resp.payment.create_refund_resp_v2 import CreateRefundRespV2
from src.gatepay.api.model.resp.payment.query_balance_resp import QueryBalanceResp
from src.gatepay.api.model.resp.payment.query_order_resp import QueryOrderResp
from src.gatepay.api.model.resp.payment.query_order_resp_v2 import QueryOrderRespV2
from src.gatepay.api.model.resp.payment.query_refund_resp import QueryRefundResp
from src.gatepay.api.model.resp.payment.query_refund_resp_v2 import QueryRefundRespV2
from src.gatepay.api.model.resp.query_batch_transfer_resp import QueryBatchTransferResp
from src.gatepay.base_response import BaseResponse
from src.gatepay.gatepay_config import GatePayConfig


class ApiPayment(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiPayment 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def create_order(self, request: CreateOrderReq) -> 'BaseResponse[CreateOrderResp]':
        """
        创建订单

        :param request: 创建订单请求参数
        :return: 创建订单响应结果
        """
        return super().process_non_base_response(request, CreateOrderResp)

    def query_order(self, request: QueryOrderReq) -> 'BaseResponse[QueryOrderResp]':
        """
        查询订单

        :param request: 查询订单请求参数
        :return: 查询订单响应结果
        """
        return super().process_non_base_response(request, QueryOrderResp)

    def close_order(self, request) -> 'BaseResponse[CloseOrderResp]':
        """
        关闭订单

        :param request: 关闭订单请求参数
        :return: 关闭订单响应结果
        """
        return super().process_non_base_response(request, CloseOrderResp)

    def create_refund(self, request) -> 'BaseResponse[CreateRefundResp]':
        """
        创建退款订单

        :param request: 创建退款请求参数
        :return: 创建退款响应结果
        """
        return super().process_non_base_response(request, CreateRefundResp)

    def query_refund(self, request) -> 'BaseResponse[QueryRefundResp]':
        """
        查询退款订单

        :param request: 查询退款请求参数
        :return: 查询退款响应结果
        """
        return super().process_non_base_response(request, QueryRefundResp)

    def create_batch_transfer(self, request) -> 'BaseResponse[CreateBatchTransferResp]':
        """
        创建批量转账

        :param request: 创建批量转账请求参数
        :return: 创建批量转账响应结果
        """
        return super().process_non_base_response(request, CreateBatchTransferResp)

    def query_batch_transfer(self, request) -> 'BaseResponse[QueryBatchTransferResp]':
        """
        查询批量转账

        :param request: 查询批量转账请求参数
        :return: 查询批量转账响应结果
        """
        return super().process_non_base_response(request, QueryBatchTransferResp)

    def query_balance(self, request) -> 'BaseResponse[QueryBalanceResp]':
        """
        查询余额

        :param request: 查询余额请求参数
        :return: 查询余额响应结果
        """
        return super().process_non_base_response(request, QueryBalanceResp)

    def query_order_v2(self, request) -> 'BaseResponse[QueryOrderRespV2]':
        """
        查询订单V2

        :param request: 查询订单请求参数
        :return: 查询订单响应结果
        """
        return super().process_non_base_response(request, QueryOrderRespV2)

    def query_refund_support_chain(self, request) -> 'BaseResponse[ChainsResp]':
        """
        退款到 Web3 支持的网络和费率查询

        :param request: 查询退款请求参数
        :return: 查询退款到链上响应结果
        """
        return super().process_non_base_response(request, ChainsResp)

    def create_refund_v2(self, request) -> 'BaseResponse[CreateRefundRespV2]':
        """
        创建退款订单V3

        :param request: 创建退款请求参数
        :return: 创建退款响应结果
        """
        return super().process_non_base_response(request, CreateRefundRespV2)

    def query_refund_v2(self, request) -> 'BaseResponse[QueryRefundRespV2]':
        """
        查询退款订单V2

        :param request: 查询退款请求参数
        :return: 查询退款响应结果
        """
        return super().process_non_base_response(request, QueryRefundRespV2)
