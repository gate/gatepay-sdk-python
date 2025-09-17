

from typing import List, Optional


class StringUtils:

    @staticmethod
    def join_str_sep_by_double_quot(str_list: List[str]) -> str:
        """
        将字符串列表用双引号和逗号连接

        :param str_list: 字符串列表
        :return: 连接后的字符串
        """
        if str_list is None or len(str_list) == 0:
            return '""'

        return '"' + '", "'.join(str_list) + '"'

    @staticmethod
    def is_string_in_list(string: str, strings: List[str]) -> bool:
        """
        判断字符串是否在列表中

        :param string: 要查找的字符串
        :param strings: 字符串列表
        :return: 如果字符串在列表中返回True，否则返回False
        """
        if strings is None:
            return False
        return string in strings

    @staticmethod
    def is_empty(string: Optional[str]) -> bool:
        """
        判断字符串是否为空

        :param string: 要判断的字符串
        :return: 如果字符串为None或空字符串返回True，否则返回False
        """
        return string is None or len(string) == 0
