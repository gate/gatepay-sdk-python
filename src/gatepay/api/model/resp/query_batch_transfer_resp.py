from typing import List, Optional
from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class Order:
    """
    订单信息
    """

    receiver_id: int = 0
    amount: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    reward_id: Optional[str] = None
    transaction_id: Optional[str] = None
    create_time: int = 0
    channel_id: Optional[str] = None

    def get_receiver_id(self) -> int:
        """
        获取接收者ID

        :return: 接收者ID
        """
        return self.receiver_id

    def set_receiver_id(self, receiver_id: int) -> None:
        """
        设置接收者ID

        :param receiver_id: 接收者ID
        """
        self.receiver_id = receiver_id

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

    def get_status(self) -> Optional[str]:
        """
        获取状态

        :return: 状态
        """
        return self.status

    def set_status(self, status: str) -> None:
        """
        设置状态

        :param status: 状态
        """
        self.status = status

    def get_reward_id(self) -> Optional[str]:
        """
        获取奖励ID

        :return: 奖励ID
        """
        return self.reward_id

    def set_reward_id(self, reward_id: str) -> None:
        """
        设置奖励ID

        :param reward_id: 奖励ID
        """
        self.reward_id = reward_id

    def get_transaction_id(self) -> Optional[str]:
        """
        获取交易ID

        :return: 交易ID
        """
        return self.transaction_id

    def set_transaction_id(self, transaction_id: str) -> None:
        """
        设置交易ID

        :param transaction_id: 交易ID
        """
        self.transaction_id = transaction_id

    def get_create_time(self) -> int:
        """
        获取创建时间

        :return: 创建时间戳
        """
        return self.create_time

    def set_create_time(self, create_time: int) -> None:
        """
        设置创建时间

        :param create_time: 创建时间戳
        """
        self.create_time = create_time

    def get_channel_id(self) -> Optional[str]:
        """
        获取渠道ID

        :return: 渠道ID
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str) -> None:
        """
        设置渠道ID

        :param channel_id: 渠道ID
        """
        self.channel_id = channel_id


@dataclass
class QueryBatchTransferResp(BaseResponse['QueryBatchTransferResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    batch_id: Optional[str] = None
    merchant_id: int = 0
    merchant_batch_no: Optional[str] = None
    status: Optional[str] = None
    currency: Optional[str] = None
    channel_id: Optional[str] = None
    orders: Optional[List[Order]] = None

    def get_status(self) -> Optional[str]:
        """
        获取状态

        :return: 状态
        """
        return self.status

    def set_status(self, status: str) -> None:
        """
        设置状态

        :param status: 状态
        """
        self.status = status

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

    def get_merchant_id(self) -> int:
        """
        获取商户ID

        :return: 商户ID
        """
        return self.merchant_id

    def set_merchant_id(self, merchant_id: int) -> None:
        """
        设置商户ID

        :param merchant_id: 商户ID
        """
        self.merchant_id = merchant_id

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

    def get_channel_id(self) -> Optional[str]:
        """
        获取渠道ID

        :return: 渠道ID
        """
        return self.channel_id

    def set_channel_id(self, channel_id: str) -> None:
        """
        设置渠道ID

        :param channel_id: 渠道ID
        """
        self.channel_id = channel_id

    def get_orders(self) -> Optional[List[Order]]:
        """
        获取订单列表

        :return: 订单列表
        """
        return self.orders

    def set_orders(self, orders: List[Order]) -> None:
        """
        设置订单列表

        :param orders: 订单列表
        """
        self.orders = orders
