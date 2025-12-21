from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi

class QueryRefundSupportChainsReqV2(BaseRequest):
    def __init__(self):
        """
        初始化QueryRefundSupportChainsReqV2对象
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_QUERY_REFUND_SUPPORT_CHAINS_V2  # 需要根据实际GatePayApi定义调整

        self.currency = None

    def get_currency(self) -> str:
        return self.currency

    def set_currency(self, currency: str):
        self.currency = currency
