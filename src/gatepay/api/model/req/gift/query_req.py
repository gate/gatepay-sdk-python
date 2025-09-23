from typing import Optional

from pydantic import BaseModel, Field

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi



def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

class QueryReqData(BaseModel):
    card_number: Optional[str] = Field(None, alias='card_number')

    key: Optional[str] = None

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

class QueryReq(BaseRequest):
    """
    查询礼品卡请求
    """

    def __init__(self):
        """
        初始化后处理，设置API信息
        """
        super().__init__()
        self.api = GatePayApi.GIFT_QUERY

        # 使用内部数据模型
        self._data = QueryReqData()

        self.card_number=  None
        self.key= None

    def get_card_number(self) -> Optional[str]:
        """
        获取卡号

        :return: 卡号
        """
        return self.card_number

    def set_card_number(self, card_number: str) -> None:
        """
        设置卡号

        :param card_number: 卡号
        """
        self.card_number = card_number
        self._data.card_number = card_number


    def get_key(self) -> Optional[str]:
        """
        获取密钥

        :return: 密钥
        """
        return self.key

    def set_key(self, key: str) -> None:
        """
        设置密钥

        :param key: 密钥
        """
        self.key = key
        self._data.key = key

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输
        """
        # 使用Pydantic的dict方法并启用by_alias选项
        result = self._data.dict(by_alias=True, exclude_none=True, exclude_defaults=True)

        # 添加父类字段
        result.update(self.get_dicts())

        return result
