from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class ListReq(BaseRequest):

    channel_id: Optional[str] = None
    desc: Optional[str] = None
    channel_type: Optional[str] = None
    page: int = 0
    count: int = 0

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.CHANNEL_MANAGE_LIST

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

    def get_desc(self) -> Optional[str]:
        """
        获取描述

        :return: 描述
        """
        return self.desc

    def set_desc(self, desc: str) -> None:
        """
        设置描述

        :param desc: 描述
        """
        self.desc = desc

    def get_channel_type(self) -> Optional[str]:
        """
        获取渠道类型

        :return: 渠道类型
        """
        return self.channel_type

    def set_channel_type(self, channel_type: str) -> None:
        """
        设置渠道类型

        :param channel_type: 渠道类型
        """
        self.channel_type = channel_type

    def get_page(self) -> int:
        """
        获取页码

        :return: 页码
        """
        return self.page

    def set_page(self, page: int) -> None:
        """
        设置页码

        :param page: 页码
        """
        self.page = page

    def get_count(self) -> int:
        """
        获取数量

        :return: 数量
        """
        return self.count

    def set_count(self, count: int) -> None:
        """
        设置数量

        :param count: 数量
        """
        self.count = count
