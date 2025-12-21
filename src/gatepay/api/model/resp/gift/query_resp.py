from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class QueryResp:
    """
    查询响应
    """
    card_num: Optional[str] = None  # 礼品卡卡号
    amount: Optional[str] = None  # 礼品卡金额
    currency: Optional[str] = None  # 礼品卡币种
    status: Optional[str] = None  # 礼品卡状态
    card_temp_id: Optional[str] = None  # 礼品卡封面ID
    creator_name: Optional[str] = None  # 礼品卡创建人名字
    create_time: Optional[str] = None  # 创建时间
    exchange_uid: int = 0  # 兑换人
    key: Optional[str] = None  # 兑换码
    title: Optional[str] = None  # 主题
    exchange_time: int = 0  # 兑换时间 标准时间戳 单位为毫秒

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueryResp':
        """
        从字典创建QueryResp实例

        Args:
            data: 包含查询响应信息的字典

        Returns:
            QueryResp实例
        """
        return cls(**data)