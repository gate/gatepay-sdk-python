from typing import Optional
from dataclasses import dataclass

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class TransactionDetailReq(BaseRequest):

    # 地址支付预支付单id
    prepay_id: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.ADDRESS_TRANSACTION_DETAIL

    def get_prepay_id(self) -> Optional[str]:
        """
        获取地址支付预支付单id

        :return: 预支付单id
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str) -> None:
        """
        设置地址支付预支付单id

        :param prepay_id: 预支付单id
        """
        self.prepay_id = prepay_id
