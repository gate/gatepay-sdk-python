
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class WithdrawFixOnChains:
    ALGO: Optional[str] = None
    APT: Optional[str] = None
    ARBEVM: Optional[str] = None
    AVAX_C: Optional[str] = None
    BSC: Optional[str] = None
    CELO: Optional[str] = None
    DOTSM: Optional[str] = None
    EOS: Optional[str] = None
    ETH: Optional[str] = None
    GTEVM: Optional[str] = None
    KAIA: Optional[str] = None
    KAVAEVM: Optional[str] = None
    MATIC: Optional[str] = None
    NEAR: Optional[str] = None
    OPETH: Optional[str] = None
    SOL: Optional[str] = None
    TON: Optional[str] = None
    TRX: Optional[str] = None
    XPL: Optional[str] = None
    XTZ: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WithdrawFixOnChains':
        return cls(**{k: v for k, v in data.items() if hasattr(cls, k)})


@dataclass
class WithdrawPercentOnChains:
    ALGO: Optional[str] = None
    APT: Optional[str] = None
    ARBEVM: Optional[str] = None
    AVAX_C: Optional[str] = None
    BSC: Optional[str] = None
    CELO: Optional[str] = None
    DOTSM: Optional[str] = None
    EOS: Optional[str] = None
    ETH: Optional[str] = None
    GTEVM: Optional[str] = None
    KAIA: Optional[str] = None
    KAVAEVM: Optional[str] = None
    MATIC: Optional[str] = None
    NEAR: Optional[str] = None
    OPETH: Optional[str] = None
    SOL: Optional[str] = None
    TON: Optional[str] = None
    TRX: Optional[str] = None
    XPL: Optional[str] = None
    XTZ: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WithdrawPercentOnChains':
        return cls(**{k: v for k, v in data.items() if hasattr(cls, k)})


@dataclass
class QueryStatusResp:
    currency: Optional[str] = None
    name: Optional[str] = None
    name_cn: Optional[str] = None
    deposit: Optional[str] = None
    withdraw_percent: Optional[str] = None
    withdraw_fix: Optional[str] = None
    withdraw_day_limit: Optional[str] = None
    withdraw_day_limit_remain: Optional[str] = None
    withdraw_amount_mini: Optional[str] = None
    withdraw_eachtime_limit: Optional[str] = None
    withdraw_fix_on_chains: Optional[WithdrawFixOnChains] = None
    withdraw_percent_on_chains: Optional[WithdrawPercentOnChains] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'QueryStatusResp':
        # 处理嵌套对象
        withdraw_fix_on_chains = data.get('withdraw_fix_on_chains')
        if withdraw_fix_on_chains is not None:
            withdraw_fix_on_chains = WithdrawFixOnChains.from_dict(withdraw_fix_on_chains)

        withdraw_percent_on_chains = data.get('withdraw_percent_on_chains')
        if withdraw_percent_on_chains is not None:
            withdraw_percent_on_chains = WithdrawPercentOnChains.from_dict(withdraw_percent_on_chains)

        return cls(
            currency=data.get('currency'),
            name=data.get('name'),
            name_cn=data.get('name_cn'),
            deposit=data.get('deposit'),
            withdraw_percent=data.get('withdraw_percent'),
            withdraw_fix=data.get('withdraw_fix'),
            withdraw_day_limit=data.get('withdraw_day_limit'),
            withdraw_day_limit_remain=data.get('withdraw_day_limit_remain'),
            withdraw_amount_mini=data.get('withdraw_amount_mini'),
            withdraw_eachtime_limit=data.get('withdraw_eachtime_limit'),
            withdraw_fix_on_chains=withdraw_fix_on_chains,
            withdraw_percent_on_chains=withdraw_percent_on_chains
        )