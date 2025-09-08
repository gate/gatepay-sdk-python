from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class QueryBatchTransferReq(BaseRequest):

    batch_id: Optional[str] = None
    merchant_batch_no: Optional[str] = None
    detail_status: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.PAYMENT_QUERY_BATCH_TRANSFER

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
