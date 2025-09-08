from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class CloseOrderReq(BaseRequest):
    """
    关闭订单请求
    """

    merchant_trade_no: Optional[str] = None
    prepay_id: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.PAYMENT_CLOSE_ORDER

    def get_merchant_trade_no(self) -> Optional[str]:
        """
        获取商户交易号

        :return: 商户交易号
        """
        return self.merchant_trade_no

    def set_merchant_trade_no(self, merchant_trade_no: str) -> None:
        """
        设置商户交易号

        :param merchant_trade_no: 商户交易号
        """
        self.merchant_trade_no = merchant_trade_no

    def get_prepay_id(self) -> Optional[str]:
        """
        获取预支付ID

        :return: 预支付ID
        """
        return self.prepay_id

    def set_prepay_id(self, prepay_id: str) -> None:
        """
        设置预支付ID

        :param prepay_id: 预支付ID
        """
        self.prepay_id = prepay_id
