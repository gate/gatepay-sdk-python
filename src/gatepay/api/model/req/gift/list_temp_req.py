from dataclasses import dataclass

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class ListTempReq(BaseRequest):
    """
    列出礼品卡模板请求
    """

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.GIFT_LIST_TEMPLATE
