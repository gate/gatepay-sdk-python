from pydantic import BaseModel, Field
from typing import Optional

def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

class Withdraw(BaseModel):

    # 商户提现ID
    merchant_withdraw_id: Optional[str] = Field(None, alias='merchant_withdraw_id')
    currency: Optional[str] = None
    amount: Optional[str] = None
    chain: Optional[str] = None
    address: Optional[str] = None
    memo: Optional[str] = None

    # 提现手续费的收取方式：
    #    如果选择内扣，则手续费将从提现金额中收取，到账金额为提现金额扣除手续费；
    #    如果选择外收，则手续费将从账户余额中扣除，到账金额即为提现金额。
    # 存量不传默认为内扣的方式
    # 类型枚举：
    #    0-内扣
    #    1-外收
    fee_type: Optional[int] = Field(None, alias='fee_type')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

    def get_merchant_withdraw_id(self) -> Optional[str]:
        """
        获取商户提现ID

        :return: 商户提现ID
        """
        return self.merchant_withdraw_id

    def set_merchant_withdraw_id(self, merchant_withdraw_id: str) -> None:
        """
        设置商户提现ID

        :param merchant_withdraw_id: 商户提现ID
        """
        self.merchant_withdraw_id = merchant_withdraw_id

    def get_currency(self) -> Optional[str]:
        """
        获取币种

        :return: 币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置币种

        :param currency: 币种
        """
        self.currency = currency

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

    def get_chain(self) -> Optional[str]:
        """
        获取链

        :return: 链
        """
        return self.chain

    def set_chain(self, chain: str) -> None:
        """
        设置链

        :param chain: 链
        """
        self.chain = chain

    def get_address(self) -> Optional[str]:
        """
        获取地址

        :return: 地址
        """
        return self.address

    def set_address(self, address: str) -> None:
        """
        设置地址

        :param address: 地址
        """
        self.address = address

    def get_memo(self) -> Optional[str]:
        """
        获取备注

        :return: 备注
        """
        return self.memo

    def set_memo(self, memo: str) -> None:
        """
        设置备注

        :param memo: 备注
        """
        self.memo = memo

    def get_fee_type(self) -> int:
        """
        获取手续费类型

        :return: 手续费类型 (0-内扣, 1-外收)
        """
        return self.fee_type

    def set_fee_type(self, fee_type: int) -> None:
        """
        设置手续费类型

        :param fee_type: 手续费类型 (0-内扣, 1-外收)
        """
        self.fee_type = fee_type

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输

        Returns:
            dict: 包含camelCase键的字典
        """
        return self.dict(by_alias=True,exclude_none=True, exclude_defaults=True)
