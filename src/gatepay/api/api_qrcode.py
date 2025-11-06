from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.qrcode.create_order_req import CreateOrderReq
from src.gatepay.api.model.resp.qrcode.create_order_resp import CreateOrderResp
from src.gatepay.gatepay_config import GatePayConfig


class ApiQrCode(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiQrCode 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def create_order(self, request: CreateOrderReq) -> CreateOrderResp:
        """
        创建扫码支付订单

        :param request: 创建订单请求参数
        :return: 创建订单响应结果
        """
        return super().process(request, CreateOrderResp)
