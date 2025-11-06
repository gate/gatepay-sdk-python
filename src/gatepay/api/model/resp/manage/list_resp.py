from typing import List, Optional
from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse
from src.gatepay.api.model.merchant_channel import MerchantChannel


@dataclass
class ListResp(BaseResponse['ListResp']):
    """
    查询客户渠道列表响应
    """
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    total: int = 0
    merchant_channel_list: Optional[List[MerchantChannel]] = None

    def get_total(self) -> int:
        """
        获取总记录数

        :return: 总记录数
        """
        return self.total

    def set_total(self, total: int) -> None:
        """
        设置总记录数

        :param total: 总记录数
        """
        self.total = total

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
