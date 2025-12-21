from enum import Enum

class Code(Enum):
    """
    返回码枚举
    """
    SUCCESS = ("000000", "成功")
    FAIL = ("400000", "失败")

    def __init__(self, code, desc):
        self.code = code
        self.desc = desc