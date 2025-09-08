from typing import Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class CreateResp(BaseResponse['CreateResp']):
    """
    创建礼品卡响应
    """
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 礼品卡卡号
    card_num: Optional[str] = None

    # 礼品卡兑换码
    card_key: Optional[str] = None

    # 礼品卡金额
    amount: Optional[str] = None

    # 礼品卡币种
    currency: Optional[str] = None

    # 礼品卡状态
    # 0 未知状态
    # 1 礼品卡待支付
    # 2 未兑换
    # 3 已兑换
    # 4 冻结
    # 5 支付失败
    # 6 人工审核
    # 7 审核驳回
    # 8 审核支付失败
    status: Optional[str] = None

    # 礼品卡封面ID
    card_temp_id: Optional[str] = None

    # 礼品卡创建人名字
    creator_name: Optional[str] = None

    # 创建时间
    create_time: Optional[str] = None

    def get_amount(self) -> Optional[str]:
        """
        获取礼品卡金额

        :return: 金额
        """
        return self.amount

    def set_amount(self, amount: str) -> None:
        """
        设置礼品卡金额

        :param amount: 金额
        """
        self.amount = amount

    def get_currency(self) -> Optional[str]:
        """
        获取礼品卡币种

        :return: 币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置礼品卡币种

        :param currency: 币种
        """
        self.currency = currency

    def get_status(self) -> Optional[str]:
        """
        获取礼品卡状态

        :return: 状态
        """
        return self.status

    def set_status(self, status: str) -> None:
        """
        设置礼品卡状态

        :param status: 状态
        """
        self.status = status

    def get_card_num(self) -> Optional[str]:
        """
        获取礼品卡卡号

        :return: 卡号
        """
        return self.card_num

    def set_card_num(self, card_num: str) -> None:
        """
        设置礼品卡卡号

        :param card_num: 卡号
        """
        self.card_num = card_num

    def get_card_key(self) -> Optional[str]:
        """
        获取礼品卡兑换码

        :return: 兑换码
        """
        return self.card_key

    def set_card_key(self, card_key: str) -> None:
        """
        设置礼品卡兑换码

        :param card_key: 兑换码
        """
        self.card_key = card_key

    def get_card_temp_id(self) -> Optional[str]:
        """
        获取礼品卡封面ID

        :return: 封面ID
        """
        return self.card_temp_id

    def set_card_temp_id(self, card_temp_id: str) -> None:
        """
        设置礼品卡封面ID

        :param card_temp_id: 封面ID
        """
        self.card_temp_id = card_temp_id

    def get_creator_name(self) -> Optional[str]:
        """
        获取礼品卡创建人名字

        :return: 创建人名字
        """
        return self.creator_name

    def set_creator_name(self, creator_name: str) -> None:
        """
        设置礼品卡创建人名字

        :param creator_name: 创建人名字
        """
        self.creator_name = creator_name

    def get_create_time(self) -> Optional[str]:
        """
        获取创建时间

        :return: 创建时间
        """
        return self.create_time

    def set_create_time(self, create_time: str) -> None:
        """
        设置创建时间

        :param create_time: 创建时间
        """
        self.create_time = create_time
