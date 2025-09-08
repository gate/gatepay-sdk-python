from typing import Optional
from pydantic import BaseModel, Field

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi

def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

class QueryOrderReqData(BaseModel):
    # 批次id
    batch_id: Optional[str] = Field(None, alias='batch_id')
    detail_status: Optional[str] = Field(None, alias='detail_status')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

class QueryOrderReq(BaseRequest):
    def __init__(self):
        super().__init__()
        self.api = GatePayApi.WITHDRAW_QUERY_ORDER
        self._data = QueryOrderReqData()
        self.batch_id: Optional[str] = None
        self.detail_status: Optional[str] = None

    def get_batch_id(self) -> Optional[str]:
        """
        获取批次ID

        Returns:
            Optional[str]: 批次ID
        """
        return self.batch_id

    def set_batch_id(self, batch_id: Optional[str]) -> None:
        """
        设置批次ID

        Args:
            batch_id (Optional[str]): 批次ID
        """
        self.batch_id = batch_id
        self._data.batch_id = batch_id

    def get_detail_status(self) -> Optional[str]:
        """
        获取详细状态

        Returns:
            Optional[str]: 详细状态
        """
        return self.detail_status

    def set_detail_status(self, detail_status: Optional[str]) -> None:
        """
        设置详细状态

        Args:
            detail_status (Optional[str]): 详细状态
        """
        self.detail_status = detail_status
        self._data.detail_status = detail_status

    def to_dict(self):
        """
                转换为字典，使用驼峰命名以供HTTP传输
                """
        # 使用Pydantic的dict方法并启用by_alias选项
        result = self._data.dict(by_alias=True, exclude_none=True, exclude_defaults=True)

        # 添加父类字段
        result.update(self.get_dicts())

        return result