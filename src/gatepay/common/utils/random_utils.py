"""
Random utilities for GatePay SDK
"""
import random
import string


class RandomUtils:
    """随机数生成器"""

    LETTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def generate_nonce(length: int) -> str:
        """
        生成指定长度的随机字符串

        Args:
            length: 随机字符串的长度

        Returns:
            生成的随机字符串

        Raises:
            ValueError: 当长度不是正数时
        """
        if length <= 0:
            raise ValueError("Length must be positive")

        return ''.join(random.choice(RandomUtils.LETTERS) for _ in range(length))
