
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class Detail:
    amount: Optional[str] = None  # 账户总额数字
    currency: Optional[str] = None  # 目标币种
    borrowed: Optional[str] = None  # 杠杆借贷总和（仅margin/cross_margin账户出现）
    unrealised_pnl: Optional[str] = None  # 未实现盈亏总和（仅futures/options/delivery/total账户出现）

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Detail':
        return cls(
            amount=data.get('amount'),
            currency=data.get('currency'),
            borrowed=data.get('borrowed'),
            unrealised_pnl=data.get('unrealised_pnl')
        )

@dataclass
class Details:
    cross_margin: Optional[Detail] = None
    spot: Optional[Detail] = None
    finance: Optional[Detail] = None
    margin: Optional[Detail] = None
    quant: Optional[Detail] = None
    futures: Optional[Detail] = None
    delivery: Optional[Detail] = None
    warrant: Optional[Detail] = None
    cbbc: Optional[Detail] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Details':
        cross_margin_data = data.get('cross_margin')
        spot_data = data.get('spot')
        finance_data = data.get('finance')
        margin_data = data.get('margin')
        quant_data = data.get('quant')
        futures_data = data.get('futures')
        delivery_data = data.get('delivery')
        warrant_data = data.get('warrant')
        cbbc_data = data.get('cbbc')

        return cls(
            cross_margin=Detail.from_dict(cross_margin_data) if cross_margin_data else None,
            spot=Detail.from_dict(spot_data) if spot_data else None,
            finance=Detail.from_dict(finance_data) if finance_data else None,
            margin=Detail.from_dict(margin_data) if margin_data else None,
            quant=Detail.from_dict(quant_data) if quant_data else None,
            futures=Detail.from_dict(futures_data) if futures_data else None,
            delivery=Detail.from_dict(delivery_data) if delivery_data else None,
            warrant=Detail.from_dict(warrant_data) if warrant_data else None,
            cbbc=Detail.from_dict(cbbc_data) if cbbc_data else None
        )

@dataclass
class Total:
    currency: Optional[str] = None
    amount: Optional[str] = None
    unrealised_pnl: Optional[str] = None
    borrowed: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Total':
        return cls(
            currency=data.get('currency'),
            amount=data.get('amount'),
            unrealised_pnl=data.get('unrealised_pnl'),
            borrowed=data.get('borrowed')
        )

@dataclass
class QueryBalanceResp:
    """
    查询余额响应
    """
    details: Optional[Details] = None
    total: Optional[Total] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryBalanceResp':
        details_data = data.get('details')
        total_data = data.get('total')

        return cls(
            details=Details.from_dict(details_data) if details_data else None,
            total=Total.from_dict(total_data) if total_data else None
        )