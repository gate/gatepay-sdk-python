from typing import Optional
from pydantic import BaseModel, Field

def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


class BatchOrder(BaseModel):

    user_id: Optional[int] = Field(0, alias='user_id')
    amount: Optional[str] = None

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

    def get_user_id(self) -> int:
        """
        获取用户ID

        :return: 用户ID
        """
        return self.user_id

    def set_user_id(self, user_id: int) -> None:
        """
        设置用户ID

        :param user_id: 用户ID
        """
        self.user_id = user_id

    def get_amount(self) -> Optional[str]:
        """
        获取金额

        :return: 金额
        """
        return self.amount

    def set_amount(self, amount: str) -> None:
        """
        设置金额

        :param amount: 金额
        """
        self.amount = amount

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输

        Returns:
            dict: 包含camelCase键的字典
        """
        return self.dict(by_alias=True, exclude_none=True, exclude_defaults=True)
