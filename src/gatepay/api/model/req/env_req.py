# env_req.py
from pydantic import BaseModel, Field
from typing import Optional


def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


class EnvReq(BaseModel):
    """
    环境请求
    """

    # 终端类型
    terminal_type: Optional[str] = Field(None, alias='terminalType')

    # 场景
    scene: Optional[str] = None

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

    def get_terminal_type(self) -> str:
        """
        获取终端类型

        Returns:
            str: 终端类型
        """
        return self.terminal_type

    def set_terminal_type(self, terminal_type: str):
        """
        设置终端类型

        Args:
            terminal_type (str): 终端类型
        """
        self.terminal_type = terminal_type

    def get_scene(self) -> str:
        """
        获取场景

        Returns:
            str: 场景
        """
        return self.scene

    def set_scene(self, scene: str):
        """
        设置场景

        Args:
            scene (str): 场景
        """
        self.scene = scene

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输

        Returns:
            dict: 包含camelCase键的字典
        """
        return self.dict(by_alias=True,exclude_none=True, exclude_defaults=True)

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return f"EnvReq(terminal_type={self.terminal_type}, scene={self.scene})"

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
