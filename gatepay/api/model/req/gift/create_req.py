from typing import Optional
from dataclasses import dataclass

from gatepay.base_request import BaseRequest
from gatepay.common.enums.gatepay_api import GatePayApi


@dataclass
class CreateReq(BaseRequest):
    """
    创建礼品卡请求
    """

    title: Optional[str] = None
    template_id: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[str] = None

    def __post_init__(self):
        """
        初始化后处理，设置API信息
        """
        self.api = GatePayApi.GIFT_CREATE

    def get_title(self) -> Optional[str]:
        """
        获取标题

        :return: 标题
        """
        return self.title

    def set_title(self, title: str) -> None:
        """
        设置标题

        :param title: 标题
        """
        self.title = title

    def get_template_id(self) -> Optional[str]:
        """
        获取模板ID

        :return: 模板ID
        """
        return self.template_id

    def set_template_id(self, template_id: str) -> None:
        """
        设置模板ID

        :param template_id: 模板ID
        """
        self.template_id = template_id

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

    def get_amount(self) -> Optional[str]:
        """
        获取金额

        :return: 金额
        """
        return self.amount

    def set_amount(self, amount: str) -> None:
        """
        设置金额

        :param amount: 金额
        """
        self.amount = amount
