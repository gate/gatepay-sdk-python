
from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class BaseResponse(Generic[T]):

    def __init__(self):
        """
        初始化 BaseResponse 实例
        """
        self.status: Optional[str] = None
        self.code: Optional[str] = None
        self.error_message: Optional[str] = None
        self.label: Optional[str] = None
        self.data: Optional[T] = None

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

    def get_code(self) -> Optional[str]:
        """
        获取编码

        :return: 编码
        """
        return self.code

    def set_code(self, code: str) -> None:
        """
        设置编码

        :param code: 编码
        """
        self.code = code

    def get_error_message(self) -> Optional[str]:
        """
        获取报错信息

        :return: 报错信息
        """
        return self.error_message

    def set_error_message(self, error_message: str) -> None:
        """
        设置报错信息

        :param error_message: 报错信息
        """
        self.error_message = error_message

    def get_label(self) -> Optional[str]:
        """
        获取标签

        :return: 标签
        """
        return self.label

    def set_label(self, label: str) -> None:
        """
        设置标签

        :param label: 标签
        """
        self.label = label

    def get_data(self) -> Optional[T]:
        """
        获取数据

        :return: 数据
        """
        return self.data

    def set_data(self, data: T) -> None:
        """
        设置数据

        :param data: 数据
        """
        self.data = data
