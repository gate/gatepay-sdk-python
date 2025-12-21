from dataclasses import dataclass
from typing import Optional


@dataclass
class QueryChainsResp:
    """
    查询币种支持的链响应
    """
    chain: Optional[str] = None  # 区块链网络名称（如ERC20、TRC20、BEP20等）
    name_cn: Optional[str] = None  # 区块链网络中文名称（如以太坊、波场等）
    name_en: Optional[str] = None  # 区块链网络英文名称（如Ethereum、Tron等）
    contract_address: Optional[str] = None  # 币种智能合约地址（原生币如BTC、ETH主网币为空字符串）
    is_disabled: int = 0  # 全局禁用状态：0-启用, 1-禁用
    is_deposit_disabled: int = 0  # 充值功能状态: 0-启用, 1-禁用
    is_withdraw_disabled: int = 0  # 提现功能状态: 0-启用, 1-禁用
    decimal: Optional[str] = None