from dataclasses import dataclass
from typing import Optional, List, Any, Dict


@dataclass
class Order:
    receiver_id: int = 0
    amount: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    reward_id: Optional[str] = None
    transaction_id: Optional[str] = None
    create_time: int = 0
    channel_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Order':
        """
        从字典创建Order实例

        Args:
            data: 包含订单信息的字典

        Returns:
            Order实例
        """
        return cls(
            receiver_id=data.get('receiver_id', 0),
            amount=data.get('amount'),
            currency=data.get('currency'),
            status=data.get('status'),
            reward_id=data.get('reward_id'),
            transaction_id=data.get('transaction_id'),
            create_time=data.get('create_time', 0),
            channel_id=data.get('channel_id')
        )


@dataclass
class QueryBatchTransferResp:
    bizCode: Optional[str] = None
    bizMessage: Optional[str] = None
    bizData: Optional[Any] = None
    batch_id: Optional[str] = None
    merchant_id: int = 0
    merchant_batch_no: Optional[str] = None
    status: Optional[str] = None
    currency: Optional[str] = None
    channel_id: Optional[str] = None
    orders_list: Optional[List[Order]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryBatchTransferResp':
        """
        从字典创建QueryBatchTransferResp实例

        Args:
            data: 包含批量转账响应信息的字典

        Returns:
            QueryBatchTransferResp实例
        """
        orders = None
        if 'orders_list' in data and data['orders_list']:
            orders = [Order.from_dict(order_data) for order_data in data['orders_list']]

        return cls(
            bizCode=data.get('bizCode'),
            bizMessage=data.get('bizMessage'),
            bizData=data.get('bizData'),
            batch_id=data.get('batch_id'),
            merchant_id=data.get('merchant_id', 0),
            merchant_batch_no=data.get('merchant_batch_no'),
            status=data.get('status'),
            currency=data.get('currency'),
            channel_id=data.get('channel_id'),
            orders_list=orders
        )