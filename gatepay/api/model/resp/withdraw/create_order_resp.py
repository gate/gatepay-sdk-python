from typing import Optional
from gatepay.base_response import BaseResponse


class CreateOrderResp(BaseResponse):
    """
    创建订单响应
    """

    def __init__(self):
        super().__init__()
        self.batch_id: Optional[str] = None

    @property
    def batch_id(self) -> Optional[str]:
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value: Optional[str]):
        self._batch_id = value
