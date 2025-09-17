from typing import List, Optional
from pydantic import BaseModel, Field

from src.gatepay.api.model.batch_order import BatchOrder
from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


class CreateBatchTransferReqData(BaseModel):
    """
    CreateOrderReq的数据模型部分，用于处理Pydantic功能
    """
    # 商户系统中的交易号
    batch_id: Optional[str] = Field(None, alias='batchId')
    merchant_batch_no: Optional[str] =Field(None, alias='merchant_batch_no')
    biz_scene: Optional[str] = Field(None, alias='bizscene')
    merchant_id: Optional[str] = Field(None, alias='merchant_id')
    client_id: Optional[str] = Field(None, alias='clientId')
    currency: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    batch_order_list: Optional[List[BatchOrder]] = Field(None, alias='batchorderList')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class CreateBatchTransferReq(BaseRequest):
    """
    创建批量转账请求
    """

    def __init__(self):

        super().__init__()
        """
         初始化后处理，设置API信息
         """
        self.api = GatePayApi.PAYMENT_CREATE_BATCH_TRANSFER

        # 使用内部数据模型
        self._data = CreateBatchTransferReqData()

        self.batch_id = None
        self.merchant_batch_no = None
        # DIRECT_TRANSFER ,REWARDS,REIMBURSEMENT,MERCHANTPAYMENT,OTHERSPAYMENT,BATCHGIFTCARD,GIFTEXCHANGE,CONVERT
        self.biz_scene = None
        self.merchant_id = None
        self.client_id = None
        self.currency = None
        self.name = None
        self.description = None
        self.batch_order_list = None

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

    def get_biz_scene(self) -> Optional[str]:
        """
        获取业务场景

        :return: 业务场景
        """
        return self.biz_scene

    def set_biz_scene(self, biz_scene: str) -> None:
        """
        设置业务场景

        :param biz_scene: 业务场景
        """
        self.biz_scene = biz_scene
        self._data.biz_scene = biz_scene

    def get_merchant_id(self) -> Optional[str]:
        """
        获取商户ID

        :return: 商户ID
        """
        return self.merchant_id

    def set_merchant_id(self, merchant_id: str) -> None:
        """
        设置商户ID

        :param merchant_id: 商户ID
        """
        self.merchant_id = merchant_id
        self._data.merchant_id = merchant_id

    def get_client_id(self) -> Optional[str]:
        """
        获取客户端ID

        :return: 客户端ID
        """
        return self.client_id

    def set_client_id(self, client_id: str) -> None:
        """
        设置客户端ID

        :param client_id: 客户端ID
        """
        self.client_id = client_id
        self._data.client_id = client_id

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
        self._data.currency = currency

    def get_name(self) -> Optional[str]:
        """
        获取名称

        :return: 名称
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        设置名称

        :param name: 名称
        """
        self.name = name
        self._data.name = name

    def get_description(self) -> Optional[str]:
        """
        获取描述

        :return: 描述
        """
        return self.description

    def set_description(self, description: str) -> None:
        """
        设置描述

        :param description: 描述
        """
        self.description = description
        self._data.description = description

    def get_batch_order_list(self) -> Optional[List[BatchOrder]]:
        """
        获取批量订单列表

        :return: 批量订单列表
        """
        return self.batch_order_list

    def set_batch_order_list(self, batch_order_list: List[BatchOrder]) -> None:
        """
        设置批量订单列表

        :param batch_order_list: 批量订单列表
        """
        self.batch_order_list = batch_order_list
        self._data.batch_order_list = batch_order_list

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输
        """
        # 使用Pydantic的dict方法并启用by_alias选项
        result = self._data.dict(by_alias=True, exclude_none=True, exclude_defaults=True)

        # 手动处理batch_order_list中的BatchOrder对象
        if self.batch_order_list is not None:
            result['batchorderList'] = [order.to_dict() for order in self.batch_order_list]

        # 添加父类字段
        result.update(self.get_dicts())

        return result
