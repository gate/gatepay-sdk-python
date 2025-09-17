from typing import List, Optional
from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class ChainNameItem:

    # Gate链
    chain: Optional[str] = None

    # 拟支付的币种
    currency: Optional[str] = None

    # 含网络信息的币种符号，下单重要参数
    full_curr_type: Optional[str] = None

    # 链上交易符号
    symbol: Optional[str] = None

    # 浏览链接，explorer + token_address
    explorer_url: Optional[str] = None

    # 链显示名称（英文）
    show_chain_name_en: Optional[str] = None

    # 是否有提现记录
    has_withdraw_memo: int = 0

    # 提现百分比
    withdraw_percent:Optional[str] = None

    # 提现百分比
    withdraw_fix:Optional[str] = None

    def get_chain(self) -> Optional[str]:
        """
        获取Gate链

        :return: Gate链
        """
        return self.chain

    def set_chain(self, chain: str) -> None:
        """
        设置Gate链

        :param chain: Gate链
        """
        self.chain = chain

    def get_currency(self) -> Optional[str]:
        """
        获取拟支付的币种

        :return: 币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置拟支付的币种

        :param currency: 币种
        """
        self.currency = currency

    def get_symbol(self) -> Optional[str]:
        """
        获取链上交易符号

        :return: 交易符号
        """
        return self.symbol

    def set_symbol(self, symbol: str) -> None:
        """
        设置链上交易符号

        :param symbol: 交易符号
        """
        self.symbol = symbol

    def get_full_curr_type(self) -> Optional[str]:
        """
        获取含网络信息的币种符号

        :return: 币种符号
        """
        return self.full_curr_type

    def set_full_curr_type(self, full_curr_type: str) -> None:
        """
        设置含网络信息的币种符号

        :param full_curr_type: 币种符号
        """
        self.full_curr_type = full_curr_type

    def get_explorer_url(self) -> Optional[str]:
        """
        获取浏览链接

        :return: 浏览链接
        """
        return self.explorer_url

    def set_explorer_url(self, explorer_url: str) -> None:
        """
        设置浏览链接

        :param explorer_url: 浏览链接
        """
        self.explorer_url = explorer_url

    def get_show_chain_name_en(self) -> Optional[str]:
        """
        获取链显示名称（英文）

        :return: 链显示名称
        """
        return self.show_chain_name_en

    def set_show_chain_name_en(self, show_chain_name_en: str) -> None:
        """
        设置链显示名称（英文）

        :param show_chain_name_en: 链显示名称
        """
        self.show_chain_name_en = show_chain_name_en

    def get_has_withdraw_memo(self) -> int:
        """
        获取是否有提现记录

        :return: 是否有提现记录
        """
        return self.has_withdraw_memo

    def set_has_withdraw_memo(self, has_withdraw_memo: int) -> None:
        """
        设置是否有提现记录

        :param has_withdraw_memo: 是否有提现记录
        """
        self.has_withdraw_memo = has_withdraw_memo

    def get_withdraw_percent(self) -> str:
        return self.withdraw_percent

    def set_withdraw_percent(self, withdraw_percent: str) -> None:
        self.withdraw_percent = withdraw_percent


    def get_withdraw_fix(self) -> str:
        return self.withdraw_fix

    def set_withdraw_fix(self, withdraw_fix: str) -> None:
        self.withdraw_fix = withdraw_fix


@dataclass
class ChainsResp(BaseResponse['ChainsResp']):

    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化


    # 币种
    currency: Optional[str] = None

    # 支持的链列表
    chains: Optional[List[ChainNameItem]] = None

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

    def get_chains(self) -> Optional[List[ChainNameItem]]:
        """
        获取支持的链列表

        :return: 链列表
        """
        return self.chains

    def set_chains(self, chains: List[ChainNameItem]) -> None:
        """
        设置支持的链列表

        :param chains: 链列表
        """
        self.chains = chains
