
from typing import List, Optional
from pydantic import BaseModel, Field

from src.gatepay.api.model.base_withdraw import Withdraw
from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

class CreateOrderReqData(BaseModel):
    # 批次id
    batch_id: Optional[str] = Field(None, alias='batch_id')
    withdraws: Optional[List[Withdraw]] = Field(None, alias='withdraw_list')
    channel_id: Optional[str] = Field(None, alias='channel_id')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

class CreateOrderReq(BaseRequest):

    def __init__(self):
        super().__init__()
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.WITHDRAW_CREATE_ORDER

        # 使用内部数据模型
        self._data = CreateOrderReqData()

        # 批次id
        self.batch_id: Optional[str] = None
        self.withdraws: Optional[List[Withdraw]] = None
        self.channel_id: Optional[str] = None

    def get_batch_id(self) -> Optional[str]:
        """
        获取批次id

        :return: 批次id
        """
        return self.batch_id

    def set_batch_id(self, batch_id: str) -> None:
        """
        设置批次id

        :param batch_id: 批次id
        """
        self.batch_id = batch_id
        self._data.batch_id = batch_id

    def get_withdraws(self) -> Optional[List[Withdraw]]:
        """
        获取提现列表

        :return: 提现列表
        """
        return self.withdraws

    def set_withdraws(self, withdraws: List[Withdraw]) -> None:
        """
        设置提现列表

        :param withdraws: 提现列表
        """
        self.withdraws = withdraws
        self._data.withdraws = withdraws

    def get_channel_id(self) -> Optional[str]:
        """
        获取渠道id

        :return: 渠道id
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str) -> None:
        """
        设置渠道id

        :param channel_id: 渠道id
        """
        self.channel_id = channel_id
        self._data.channel_id = channel_id

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输
        """
        # 使用Pydantic的dict方法并启用by_alias选项
        result = self._data.dict(by_alias=True, exclude_none=True, exclude_defaults=True)

        # 手动处理withdraw_list中的withdraw对象
        if self.withdraws is not None:
            result['withdraw_list'] = [item.to_dict() for item in self.withdraws]

        # 添加父类字段
        result.update(self.get_dicts())

        return result
