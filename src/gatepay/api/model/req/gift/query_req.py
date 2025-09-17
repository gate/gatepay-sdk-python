from typing import Optional
from dataclasses import dataclass

from src.gatepay.base_request import BaseRequest
from src.gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class QueryReq(BaseRequest):
    """
    查询礼品卡请求
    """

    card_number: Optional[str] = None
    key: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.GIFT_QUERY

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
