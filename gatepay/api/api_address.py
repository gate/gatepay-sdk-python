

from typing import TypeVar

from gatepay.api.base_api import BaseApi
from gatepay.api.model.req.chain_req import ChainsReq
from gatepay.api.model.req.address.create_order_req import CreateOrderReq
from gatepay.api.model.req.create_refund_convert_req import CreateRefundConvertReq
from gatepay.api.model.req.address.create_refund_req import CreateRefundReq
from gatepay.api.model.req.currencies_req import CurrenciesReq
from gatepay.api.model.req.address.query_order_req import QueryOrderReq
from gatepay.api.model.req.supported_convert_currencies_req import SupportedConvertCurrenciesReq
from gatepay.api.model.req.transaction_detail_req import TransactionDetailReq
from gatepay.api.model.resp.chains_resp import ChainsResp
from gatepay.api.model.resp.address.create_order_resp import CreateOrderResp
from gatepay.api.model.resp.create_refund_convert_resp import CreateRefundConvertResp
from gatepay.api.model.resp.create_refund_resp import CreateRefundResp
from gatepay.api.model.resp.currencies_resp import CurrenciesResp
from gatepay.api.model.resp.address.query_order_resp import QueryOrderResp
from gatepay.api.model.resp.supported_convert_currencies_resp import SupportedConvertCurrenciesResp
from gatepay.api.model.resp.transaction_detail_resp import TransactionDetailResp
from gatepay.gatepay_config import GatePayConfig

T = TypeVar('T')


class ApiAddress(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiAddress 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def get_address_chains(self, request: ChainsReq) -> ChainsResp:
        """
        查询支持链列表

        :param request: 请求参数
        :return: ChainsResp
        """
        return super().process(request, ChainsResp)

    def get_address_currencies(self) -> CurrenciesResp:
        """
        查询支持币种列表

        :return: CurrenciesResp
        """
        return super().process(CurrenciesReq(), CurrenciesResp)

    def get_supported_convert_currencies(self,
                                         request: SupportedConvertCurrenciesReq) -> SupportedConvertCurrenciesResp:
        """
        创建闪兑地址支付单之前，根据订单币种查询支持闪兑的币种，
        用户从支持闪兑的币种列表中选择实际支付币种创建闪兑支付订单

        :param request: 请求参数, currency 订单币种
        :return: SupportedConvertCurrenciesResp, currencies 支持闪兑到订单币种的币种列表
        """
        return super().process(request, SupportedConvertCurrenciesResp)

    def create_order(self, request: CreateOrderReq) -> CreateOrderResp:
        """
        创建地址支付订单/下单

        :param request: 请求参数
        :return: CreateOrderResp
        """
        return super().process(request, CreateOrderResp)

    def query_order(self, request: QueryOrderReq) -> QueryOrderResp:
        """
        查询地址支付订单详情

        :param request: 请求参数
        :return: QueryOrderResp
        """
        return super().process(request, QueryOrderResp)

    def create_refund(self, request: CreateRefundReq) -> CreateRefundResp:
        """
        创建非闪兑支付单退款

        :param request: 请求参数
        :return: CreateRefundResp
        """
        return super().process(request, CreateRefundResp)

    def create_refund_convert(self, request: CreateRefundConvertReq) -> CreateRefundConvertResp:
        """
        创建闪兑支付单退款

        :param request: 请求参数
        :return: CreateRefundConvertResp
        """
        return super().process(request, CreateRefundConvertResp)

    def transaction_detail(self, request: TransactionDetailReq) -> TransactionDetailResp:
        """
        查询链上交易详情

        :param request: 请求参数
        :return: TransactionDetailResp
        """
        return super().process(request, TransactionDetailResp)
