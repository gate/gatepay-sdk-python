import re
import json

from typing import Any

from camel_converter import to_camel
from camel_converter import to_snake



class CamelAndSnakeUtils:
    """
    JSON下划线命名转驼峰命名工具类
    """

    @staticmethod
    def encode(obj: Any) -> str:
        if isinstance(obj, dict):
            obj = CamelAndSnakeUtils.convert_dict_keys(obj)
        return CamelAndSnakeUtils.encode(obj)

    def convert_dict_keys(data: dict) -> dict:
        """递归转换字典键名"""
        result = {}
        for key, value in data.items():
            # 转换键名为驼峰
            camel_key = to_camel(key) if '_' in key else key

            # 递归处理嵌套结构
            if isinstance(value, dict):
                result[camel_key] = CamelAndSnakeUtils.convert_dict_keys(value)
            elif isinstance(value, list):
                result[camel_key] = [
                    CamelAndSnakeUtils.convert_dict_keys(item) if isinstance(item, dict) else item
                    for item in value
                ]
            else:
                result[camel_key] = value
        return result

    @staticmethod
    def to_camel_case(snake_str: str) -> str:
        """
        将下划线命名转换为驼峰命名

        Args:
            snake_str: 下划线命名字符串

        Returns:
            驼峰命名字符串
        """
        if not snake_str or '_' not in snake_str:
            return snake_str

        components = snake_str.split('_')
        # 第一个组件保持小写，后续组件首字母大写
        return components[0] + ''.join(x.title() for x in components[1:])

    @staticmethod
    def convert_camel_json_to_snake(json_str: str) -> Any:
        """转换驼峰JSON字符串为下划线格式"""

        # 使用正则表达式处理键名
        def camel_to_snake_repl(match):
            key = match.group(1)
            # 处理连续大写字母的情况（如HTTPRequest -> http_request）
            key = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', key)
            # 处理正常驼峰
            snake_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key).lower()
            return f'"{snake_key}":'

        # 匹配JSON键名（确保不会匹配到值中的内容）
        pattern = r'"([a-z][a-zA-Z0-9]*)":'
        return re.sub(pattern, camel_to_snake_repl, json_str)