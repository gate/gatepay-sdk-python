from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.withdraw.query_balance_req import QueryBalanceReq
from src.gatepay.api.model.req.query_chains_req import QueryChainsReq
from src.gatepay.api.model.req.query_status_req import QueryStatusReq
from src.gatepay.api.model.req.withdraw.create_order_req import CreateOrderReq
from src.gatepay.api.model.req.withdraw.query_order_req import QueryOrderReq
from src.gatepay.api.model.resp.withdraw.query_balance_resp import QueryBalanceResp
from src.gatepay.api.model.resp.query_chains_resp import QueryChainsResp
from src.gatepay.api.model.resp.withdraw.query_order_resp import QueryOrderResp
from src.gatepay.api.model.resp.query_status_resp import QueryStatusResp
from src.gatepay.api.model.resp.withdraw.create_order_resp import CreateOrderResp
from src.gatepay.gatepay_config import GatePayConfig


class ApiWithdraw(BaseApi):
    """
    提现API类
    """

    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化ApiWithdraw实例

        Args:
            gate_pay_config (GatePayConfig): GatePay配置对象
        """
        super().__init__(gate_pay_config)

    def create_order(self, request: CreateOrderReq) -> CreateOrderResp:
        """
        创建提现订单

        Args:
            request (CreateOrderReq): 创建订单请求对象

        Returns:
            CreateOrderResp: 创建订单响应对象
        """
        return super().process(request, CreateOrderResp)

    def query_order(self, request: QueryOrderReq) -> QueryOrderResp:
        """
        查询提现订单

        detail_status:
        ALL 全部子订单
        PENDING 待处理子订单
        PROCESSING 已提交提现请求，待确认子订单
        CHECK 审核中子订单
        FAIL 失败子订单
        DONE 提现成功子订单

        Args:
            request (QueryOrderReq): 查询订单请求对象

        Returns:
            QueryOrderResp: 查询订单响应对象
        """
        return super().process(request, QueryOrderResp)

    def query_chains(self, request: QueryChainsReq) -> QueryChainsResp:
        """
        查询币种支持的链

        Args:
            request (QueryChainsReq): 查询链请求对象

        Returns:
            QueryChainsResp: 查询链响应对象
        """
        return super().process(request, QueryChainsResp)

    def query_balance(self, request: QueryBalanceReq) -> QueryBalanceResp:
        """
        查询个人账户余额

        Args:
            request (QueryBalanceReq): 查询余额请求对象

        Returns:
            QueryBalanceResp: 查询余额响应对象
        """
        return super().process(request, QueryBalanceResp)

    def query_status(self, request: QueryStatusReq) -> QueryStatusResp:
        """
        查询提现状态

        Args:
            request (QueryStatusReq): 查询状态请求对象

        Returns:
            QueryStatusResp: 查询状态响应对象
        """
        return super().process(request, QueryStatusResp)
