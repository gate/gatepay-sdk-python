# chain.py
import json
from pydantic import BaseModel, Field
from typing import Optional


def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


class Chain(BaseModel):
    """
    链信息
    """

    # 链类型
    chain_type: Optional[str] = Field(None, alias='chainType')

    # 链地址
    address: Optional[str] = None

    # 链币种类型
    full_curr_type: Optional[str] = Field(None, alias='fullCurrType')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

    def get_chain_type(self) -> str:
        """
        获取链类型

        Returns:
            str: 链类型
        """
        return self.chain_type

    def set_chain_type(self, chain_type: str):
        """
        设置链类型

        Args:
            chain_type (str): 链类型
        """
        self.chain_type = chain_type

    def get_address(self) -> str:
        """
        获取链地址

        Returns:
            str: 链地址
        """
        return self.address

    def set_address(self, address: str):
        """
        设置链地址

        Args:
            address (str): 链地址
        """
        self.address = address

    def get_full_curr_type(self) -> str:
        """
        获取链币种类型

        Returns:
            str: 链币种类型
        """
        return self.full_curr_type

    def set_full_curr_type(self, full_curr_type: str):
        """
        设置链币种类型

        Args:
            full_curr_type (str): 链币种类型
        """
        self.full_curr_type = full_curr_type

    def to_dict(self) -> dict:
        """
        将对象转换为字典，用于JSON序列化

        Returns:
            dict: 包含对象属性的字典（camelCase键）
        """
        return self.dict(by_alias=True)

    @classmethod
    def from_dict(cls, data: dict):
        cls(
            chain_type=data.get('chain_type'),
            address=data.get('address'),
            full_curr_type=data.get('fullCurrType')
        )
        return cls(**data)

    def to_json(self) -> str:
        """
        将对象转换为JSON字符串

        Returns:
            str: JSON字符串
        """
        return self.json(by_alias=True)

    @classmethod
    def from_json(cls, json_str: str):
        """
        从JSON字符串创建Chain对象

        Args:
            json_str (str): JSON字符串

        Returns:
            Chain: 创建的Chain对象
        """
        # Pydantic可以直接从JSON创建对象
        return cls.parse_raw(json_str)

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return f"Chain(chain_type={self.chain_type}, address={self.address}, full_curr_type={self.full_curr_type})"

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
