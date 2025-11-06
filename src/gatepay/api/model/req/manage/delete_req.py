from typing import Optional
from dataclasses import dataclass

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class DeleteReq(BaseRequest):
    """
    删除客户渠道请求
    """

    channel_id: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.CHANNEL_MANAGE_DELETE

    def get_channel_id(self) -> Optional[str]:
        """
        获取渠道ID

        :return: 渠道ID
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str) -> None:
        """
        设置渠道ID

        :param channel_id: 渠道ID
        """
        self.channel_id = channel_id
