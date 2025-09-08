from typing import Optional
from gatepay.base_response import BaseResponse


class QueryBalanceResp(BaseResponse):
    """
    查询余额响应
    """

    class Detail:
        """
        余额详情
        """
        def __init__(self):
            self.amount: Optional[str] = None  # 账户总额数字
            self.currency: Optional[str] = None  # 目标币种
            self.borrowed: Optional[str] = None  # 杠杆借贷总和（仅margin/cross_margin账户出现）
            self.unrealised_pnl: Optional[str] = None  # 未实现盈亏总和（仅futures/options/delivery/total账户出现）

        @classmethod
        def from_dict(cls, data: dict):
            if not data:
                return None
            detail = cls()
            detail.amount = data.get("amount")
            detail.currency = data.get("currency")
            detail.borrowed = data.get("borrowed")
            detail.unrealised_pnl = data.get("unrealised_pnl")
            return detail

        def to_dict(self):
            if not self:
                return None
            return {
                "amount": self.amount,
                "currency": self.currency,
                "borrowed": self.borrowed,
                "unrealised_pnl": self.unrealised_pnl
            }

    class Details:
        """
        各账户类型详情
        """
        def __init__(self):
            self.cross_margin: Optional['QueryBalanceResp.Detail'] = None
            self.spot: Optional['QueryBalanceResp.Detail'] = None
            self.finance: Optional['QueryBalanceResp.Detail'] = None
            self.margin: Optional['QueryBalanceResp.Detail'] = None
            self.quant: Optional['QueryBalanceResp.Detail'] = None
            self.futures: Optional['QueryBalanceResp.Detail'] = None
            self.delivery: Optional['QueryBalanceResp.Detail'] = None
            self.warrant: Optional['QueryBalanceResp.Detail'] = None
            self.cbbc: Optional['QueryBalanceResp.Detail'] = None

    class Total:
        """
        换算成目标币种的账户总额汇总
        """
        def __init__(self):
            self.currency: Optional[str] = None
            self.amount: Optional[str] = None
            self.unrealised_pnl: Optional[str] = None
            self.borrowed: Optional[str] = None

    def __init__(self):
        super().__init__()
        self.details: Optional[QueryBalanceResp.Details] = None
        self.total: Optional[QueryBalanceResp.Total] = None

    def get_details(self) -> Optional[Details]:
        """
        获取详情信息

        Returns:
            Optional[Details]: 详情信息
        """
        return self.details

    def set_details(self, details: Details) -> None:
        """
        设置详情信息

        Args:
            details (Details): 详情信息
        """
        self.details = details

    def get_total(self) -> Optional[Total]:
        """
        获取总额信息

        Returns:
            Optional[Total]: 总额信息
        """
        return self.total

    def set_total(self, total: Total) -> None:
        """
        设置总额信息

        Args:
            total (Total): 总额信息
        """
        self.total = total
