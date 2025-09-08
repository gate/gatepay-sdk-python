"""
Base response class for GatePay SDK
"""

from typing import TypeVar, Generic, Optional, Any

T = TypeVar('T')


class BaseResponse(Generic[T]):
    """
    基础响应类
    """

    def __init__(self):
        self.status: Optional[str] = None
        self.code: Optional[str] = None
        self.error_message: Optional[str] = None
        self.label: Optional[str] = None
        self.data: Optional[T] = None

    # Getters and setters
    def get_status(self) -> Optional[str]:
        return self.status

    def set_status(self, status: str) -> None:
        self.status = status

    def get_code(self) -> Optional[str]:
        return self.code

    def set_code(self, code: str) -> None:
        self.code = code

    def get_error_message(self) -> Optional[str]:
        return self.error_message

    def set_error_message(self, error_message: str) -> None:
        self.error_message = error_message

    def get_label(self) -> Optional[str]:
        return self.label

    def set_label(self, label: str) -> None:
        self.label = label

    def get_data(self) -> Optional[T]:
        return self.data

    def set_data(self, data: T) -> None:
        self.data = data
