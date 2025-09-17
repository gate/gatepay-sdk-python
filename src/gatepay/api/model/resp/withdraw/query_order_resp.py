from typing import List
from typing import Optional

from src.gatepay.api.model.base_withdraw import Withdraw
from src.gatepay.base_response import BaseResponse


class QueryOrderResp(BaseResponse):
    """
    查询订单响应
    """

    def __init__(self):
        super().__init__()
        self._batch_id: Optional[str] = None
        self._merchant_id: Optional[int] = None
        self._client_id: Optional[int] = None
        self._status: Optional[str] = None
        self._create_time: Optional[int] = None
        self._withdraw_list: Optional[List[Withdraw]] = None
        self._channel_id: Optional[str] = None

    @property
    def batch_id(self) -> Optional[str]:
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value: Optional[str]):
        self._batch_id = value

    @property
    def merchant_id(self) -> Optional[int]:
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value: Optional[int]):
        self._merchant_id = value

    @property
    def client_id(self) -> Optional[int]:
        return self._client_id

    @client_id.setter
    def client_id(self, value: Optional[int]):
        self._client_id = value

    @property
    def status(self) -> Optional[str]:
        return self._status

    @status.setter
    def status(self, value: Optional[str]):
        self._status = value

    @property
    def create_time(self) -> Optional[int]:
        return self._create_time

    @create_time.setter
    def create_time(self, value: Optional[int]):
        self._create_time = value

    @property
    def withdraw_list(self) -> Optional[List[Withdraw]]:
        return self._withdraw_list

    @withdraw_list.setter
    def withdraw_list(self, value: Optional[List[Withdraw]]):
        self._withdraw_list = value

    @property
    def channel_id(self) -> Optional[str]:
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value: Optional[str]):
        self._channel_id = value
