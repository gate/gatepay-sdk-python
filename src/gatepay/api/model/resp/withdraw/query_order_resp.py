from dataclasses import dataclass
from typing import List
from typing import Optional

from src.gatepay.api.model.base_withdraw import Withdraw


@dataclass
class QueryOrderResp:
    """
    查询订单响应
    """
    batch_id: Optional[str] = None
    merchant_id: int = 0
    client_id: Optional[str] = None
    status: Optional[str] = None
    create_time: int = 0
    withdraw_list: Optional[List['Withdraw']] = None
    channel_id: Optional[str] = None
