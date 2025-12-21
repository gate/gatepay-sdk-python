from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.checkout.create_order_req import CreateOrderReq
from src.gatepay.api.model.req.checkout.create_refund_req import CreateRefundReq
from src.gatepay.api.model.resp.checkout.create_order_resp import CreateOrderResp
from src.gatepay.api.model.resp.checkout.create_refund_resp import CreateRefundResp
from src.gatepay.base_response import BaseResponse
from src.gatepay.gatepay_config import GatePayConfig


class ApiCheckout(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiCheckout 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def create_order(self, request: CreateOrderReq) -> 'BaseResponse[CreateOrderResp]':
        """
        创建收银台订单

        :param request: 创建订单请求参数
        :return: 创建订单响应结果
        """
        return super().process_non_base_response(request, CreateOrderResp)

    def create_refund(self, request: CreateRefundReq) -> 'BaseResponse[CreateRefundResp]':
        """
        创建退款

        :param request: 创建退款请求参数
        :return: 创建退款响应结果
        """
        return super().process_non_base_response(request, CreateRefundResp)
