from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ChainNameItem:
    chain: Optional[str] = None
    currency: Optional[str] = None
    full_curr_type: Optional[str] = None
    symbol: Optional[str] = None
    explorer_url: Optional[str] = None
    show_chain_name_en: Optional[str] = None
    hasWithdrawMemo: int = 0
    withdrawPercent: Optional[str] = None
    withdrawFix: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ChainNameItem':
        if not data:
            return None

        return cls(
            chain=data.get('chain'),
            currency=data.get('currency'),
            full_curr_type=data.get('full_curr_type'),
            symbol=data.get('symbol'),
            explorer_url=data.get('explorer_url'),
            show_chain_name_en=data.get('show_chain_name_en'),
            hasWithdrawMemo=data.get('hasWithdrawMemo', 0),
            withdrawPercent=data.get('withdrawPercent'),
            withdrawFix=data.get('withdrawFix')
        )


@dataclass
class ChainsResp:
    currency: Optional[str] = None
    chains: Optional[List[ChainNameItem]] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ChainsResp':
        if not data:
            return None

        # 处理 chains 列表
        chains_data = data.get('chains')
        chains = None
        if chains_data and isinstance(chains_data, list):
            chains = [ChainNameItem.from_dict(item) for item in chains_data if item]

        return cls(
            currency=data.get('currency'),
            chains=chains
        )