

from dataclasses import dataclass
from typing import List, Optional

from src.gatepay.api.model.merchant_channel import MerchantChannel
from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class SaveReq(BaseRequest):
    """
    保存客户渠道请求
    """

    merchant_channel_list: Optional[List[MerchantChannel]] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.CHANNEL_MANAGE_SAVE

    def get_merchant_channel_list(self) -> Optional[List[MerchantChannel]]:
        """
        获取商户渠道列表

        :return: 商户渠道列表
        """
        return self.merchant_channel_list

    def set_merchant_channel_list(self, merchant_channel_list: List[MerchantChannel]) -> None:
        """
        设置商户渠道列表

        :param merchant_channel_list: 商户渠道列表
        """
        self.merchant_channel_list = merchant_channel_list
