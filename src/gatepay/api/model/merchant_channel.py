from typing import List, Optional
from dataclasses import dataclass

from src.gatepay.api.model.custom_field import CustomField


@dataclass
class MerchantChannel:

    channel_id: Optional[str] = None
    desc: Optional[str] = None

    # 0: 个人，1：企业
    channel_type: Optional[str] = None

    chain: Optional[str] = None
    currency: Optional[str] = None
    address: Optional[str] = None
    custom_fields: Optional[List[CustomField]] = None
    result: Optional[str] = None

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
        0: 个人，1：企业

        :return: 渠道类型
        """
        return self.channel_type

    def set_channel_type(self, channel_type: str) -> None:
        """
        设置渠道类型
        0: 个人，1：企业

        :param channel_type: 渠道类型
        """
        self.channel_type = channel_type

    def get_chain(self) -> Optional[str]:
        """
        获取链

        :return: 链
        """
        return self.chain

    def set_chain(self, chain: str) -> None:
        """
        设置链

        :param chain: 链
        """
        self.chain = chain

    def get_address(self) -> Optional[str]:
        """
        获取地址

        :return: 地址
        """
        return self.address

    def set_address(self, address: str) -> None:
        """
        设置地址

        :param address: 地址
        """
        self.address = address

    def get_custom_fields(self) -> Optional[List[CustomField]]:
        """
        获取自定义字段列表

        :return: 自定义字段列表
        """
        return self.custom_fields

    def set_custom_fields(self, custom_fields: List[CustomField]) -> None:
        """
        设置自定义字段列表

        :param custom_fields: 自定义字段列表
        """
        self.custom_fields = custom_fields

    def get_currency(self) -> Optional[str]:
        """
        获取币种

        :return: 币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置币种

        :param currency: 币种
        """
        self.currency = currency

    def get_result(self) -> Optional[str]:
        """
        获取结果

        :return: 结果
        """
        return self.result

    def set_result(self, result: str) -> None:
        """
        设置结果

        :param result: 结果
        """
        self.result = result
