from typing import Optional
from dataclasses import dataclass

from src.gatepay.base_response import BaseResponse


@dataclass
class QueryChainsResp(BaseResponse['QueryChainsResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 区块链网络名称（如ERC20、TRC20、BEP20等）
    chain: Optional[str] = None

    # 区块链网络中文名称（如以太坊、波场等）
    name_cn: Optional[str] = None

    # 区块链网络英文名称（如Ethereum、Tron等）
    name_en: Optional[str] = None

    # 币种智能合约地址（原生币如BTC、ETH主网币为空字符串）
    contract_address: Optional[str] = None

    # 全局禁用状态：0-启用, 1-禁用
    is_disabled: int = 0

    # 充值功能状态: 0-启用, 1-禁用
    is_deposit_disabled: int = 0

    # 提现功能状态: 0-启用, 1-禁用
    is_withdraw_disabled: int = 0

    # 提币精度（小数点位数，如BTC为"6"）
    decimal: Optional[str] = None

    def get_chain(self) -> Optional[str]:
        """
        获取区块链网络名称

        :return: 区块链网络名称
        """
        return self.chain

    def set_chain(self, chain: str) -> None:
        """
        设置区块链网络名称

        :param chain: 区块链网络名称
        """
        self.chain = chain

    def get_name_cn(self) -> Optional[str]:
        """
        获取区块链网络中文名称

        :return: 区块链网络中文名称
        """
        return self.name_cn

    def set_name_cn(self, name_cn: str) -> None:
        """
        设置区块链网络中文名称

        :param name_cn: 区块链网络中文名称
        """
        self.name_cn = name_cn

    def get_name_en(self) -> Optional[str]:
        """
        获取区块链网络英文名称

        :return: 区块链网络英文名称
        """
        return self.name_en

    def set_name_en(self, name_en: str) -> None:
        """
        设置区块链网络英文名称

        :param name_en: 区块链网络英文名称
        """
        self.name_en = name_en

    def get_contract_address(self) -> Optional[str]:
        """
        获取币种智能合约地址

        :return: 币种智能合约地址
        """
        return self.contract_address

    def set_contract_address(self, contract_address: str) -> None:
        """
        设置币种智能合约地址

        :param contract_address: 币种智能合约地址
        """
        self.contract_address = contract_address

    def get_is_disabled(self) -> int:
        """
        获取全局禁用状态

        :return: 全局禁用状态 (0-启用, 1-禁用)
        """
        return self.is_disabled

    def set_is_disabled(self, is_disabled: int) -> None:
        """
        设置全局禁用状态

        :param is_disabled: 全局禁用状态 (0-启用, 1-禁用)
        """
        self.is_disabled = is_disabled

    def get_is_deposit_disabled(self) -> int:
        """
        获取充值功能状态

        :return: 充值功能状态 (0-启用, 1-禁用)
        """
        return self.is_deposit_disabled

    def set_is_deposit_disabled(self, is_deposit_disabled: int) -> None:
        """
        设置充值功能状态

        :param is_deposit_disabled: 充值功能状态 (0-启用, 1-禁用)
        """
        self.is_deposit_disabled = is_deposit_disabled

    def get_is_withdraw_disabled(self) -> int:
        """
        获取提现功能状态

        :return: 提现功能状态 (0-启用, 1-禁用)
        """
        return self.is_withdraw_disabled

    def set_is_withdraw_disabled(self, is_withdraw_disabled: int) -> None:
        """
        设置提现功能状态

        :param is_withdraw_disabled: 提现功能状态 (0-启用, 1-禁用)
        """
        self.is_withdraw_disabled = is_withdraw_disabled

    def get_decimal(self) -> Optional[str]:
        """
        获取提币精度

        :return: 提币精度（小数点位数）
        """
        return self.decimal

    def set_decimal(self, decimal: str) -> None:
        """
        设置提币精度

        :param decimal: 提币精度（小数点位数）
        """
        self.decimal = decimal
