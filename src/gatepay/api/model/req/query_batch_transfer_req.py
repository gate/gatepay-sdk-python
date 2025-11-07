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


class QueryBatchTransferReqData(BaseModel):
    """
    CreateOrderReq的数据模型部分，用于处理Pydantic功能
    """
    # 商户系统中的交易号
    batch_id: Optional[str] = Field(None, alias='batch_id')

    # 订单币种
    merchant_batch_no: Optional[str] = Field(None, alias='merchant_batch_no')

    # 订单金额
    detail_status: Optional[str] = Field(None, alias='detail_status')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True



class QueryBatchTransferReq(BaseRequest):

    def __init__(self):
        """
        初始化后处理，设置API信息
        """
        super().__init__()
        self.api = GatePayApi.PAYMENT_QUERY_BATCH_TRANSFER

        self._data = QueryBatchTransferReqData()

        self.batch_id = None
        self.merchant_batch_no = None
        self.detail_status = None

    def get_batch_id(self) -> Optional[str]:
        """
        获取批次ID

        :return: 批次ID
        """
        return self.batch_id

    def set_batch_id(self, batch_id: str) -> None:
        """
        设置批次ID

        :param batch_id: 批次ID
        """
        self.batch_id = batch_id
        self._data.batch_id = batch_id

    def get_merchant_batch_no(self) -> Optional[str]:
        """
        获取商户批次号

        :return: 商户批次号
        """
        return self.merchant_batch_no

    def set_merchant_batch_no(self, merchant_batch_no: str) -> None:
        """
        设置商户批次号

        :param merchant_batch_no: 商户批次号
        """
        self.merchant_batch_no = merchant_batch_no
        self._data.merchant_batch_no = merchant_batch_no

    def get_detail_status(self) -> Optional[str]:
        """
        获取详细状态

        :return: 详细状态
        """
        return self.detail_status

    def set_detail_status(self, detail_status: str) -> None:
        """
        设置详细状态

        :param detail_status: 详细状态
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

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
