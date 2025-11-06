
from typing import TypeVar, Generic
from src.gatepay.base_response import BaseResponse

Resp = TypeVar('Resp', bound=BaseResponse)


class GatePayResp(BaseResponse, Generic[Resp]):

    def __init__(self, resp: Resp):
        """
        初始化 GatePayResp 实例

        :param resp: 响应对象
        """
        super().__init__()
        self.set_status(resp.get_status())
        self.set_code(resp.get_code())
        self.set_error_message(resp.get_error_message())
        self.set_label(resp.get_label())
        self.set_data(resp.get_data())
