
from typing import TypeVar, Generic, Optional
from src.gatepay.base_response import BaseResponse

Resp = TypeVar('Resp', bound=BaseResponse)


class GatePayResp(BaseResponse, Generic[Resp]):

    def __init__(self, resp: Resp):
        """
        初始化 GatePayResp 实例

        :param resp: 响应对象
        """
        super().__init__()
        self.set_status(resp.status)
        self.set_code(resp.code)
        self.set_error_message(resp.error_message)
        self.set_label(resp.label)
        self.set_data(resp.data)

    def get_status(self) -> Resp:
        """
        获取响应对象

        :return: 响应对象
        """
        return self.status

    def get_data(self) -> Resp:
        """
        获取响应对象

        :return: 响应对象
        """
        return self.data

    def get_code(self) -> Optional[str]:
        """
        获取响应码

        :return: 响应码
        """
        return self.code

    def get_error_message(self) -> Optional[str]:
        """
        获取错误信息

        :return: 错误信息
        """
        return self.error_message

    def get_label(self) -> Optional[str]:
        """
        获取响应标签

        :return: 响应标签
        """
        return self.label