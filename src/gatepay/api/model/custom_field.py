from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class CustomField:
    """
    自定义字段
    """

    code: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None

    def get_code(self) -> Optional[str]:
        """
        获取字段代码

        :return: 字段代码
        """
        return self.code

    def set_code(self, code: str) -> None:
        """
        设置字段代码

        :param code: 字段代码
        """
        self.code = code

    def get_name(self) -> Optional[str]:
        """
        获取字段名称

        :return: 字段名称
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        设置字段名称

        :param name: 字段名称
        """
        self.name = name

    def get_value(self) -> Optional[str]:
        """
        获取字段值

        :return: 字段值
        """
        return self.value

    def set_value(self, value: str) -> None:
        """
        设置字段值

        :param value: 字段值
        """
        self.value = value

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CustomField':
        if not data:
            return None

        return cls(
            code=data.get('code'),
            name=data.get('name'),
            value=data.get('value')
        )
