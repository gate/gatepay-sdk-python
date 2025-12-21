from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class QueryBalanceResp:
    """
    查询余额响应
    """
    ADA: Optional[str] = None
    ALGO: Optional[str] = None
    APT: Optional[str] = None
    ARB: Optional[str] = None
    ATOM: Optional[str] = None
    AVAX: Optional[str] = None
    BCH: Optional[str] = None
    BNB: Optional[str] = None
    BTC: Optional[str] = None
    CRO: Optional[str] = None
    DAI: Optional[str] = None
    DOGE: Optional[str] = None
    DOT: Optional[str] = None
    EEG: Optional[str] = None
    ETC: Optional[str] = None
    ETH: Optional[str] = None
    FDUSD: Optional[str] = None
    FET: Optional[str] = None
    FIL: Optional[str] = None
    FROG: Optional[str] = None
    GT: Optional[str] = None
    HBAR: Optional[str] = None
    ICP: Optional[str] = None
    KAS: Optional[str] = None
    LEO: Optional[str] = None
    LINK: Optional[str] = None
    LION: Optional[str] = None
    LTC: Optional[str] = None
    MKR: Optional[str] = None
    MNT: Optional[str] = None
    NEAR: Optional[str] = None
    OKB: Optional[str] = None
    PEPE: Optional[str] = None
    POL: Optional[str] = None
    PPIE: Optional[str] = None
    RENDER: Optional[str] = None
    SEPOLIA: Optional[str] = None
    SHIB: Optional[str] = None
    SOL: Optional[str] = None
    STEPG: Optional[str] = None
    STPT: Optional[str] = None
    STX: Optional[str] = None
    SUPE: Optional[str] = None
    TAO: Optional[str] = None
    TESTNET3: Optional[str] = None
    TON: Optional[str] = None
    TRX: Optional[str] = None
    UNI: Optional[str] = None
    USDC: Optional[str] = None
    USDT: Optional[str] = None
    VET: Optional[str] = None
    XLM: Optional[str] = None
    XMR: Optional[str] = None
    XRP: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryBalanceResp':
        return cls(**data)