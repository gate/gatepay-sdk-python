from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi

class QueryRefundSupportChainsReqV3(BaseRequest):
    def __init__(self):
        """
        初始化QueryRefundSupportChainsReqV3对象
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_QUERY_REFUND_SUPPORT_CHAINS_V3  # 需要根据实际GatePayApi定义调整

        self.currency = None

    def get_currency(self) -> str:
        return self.currency

    def set_currency(self, currency: str):
        self.currency = currency
