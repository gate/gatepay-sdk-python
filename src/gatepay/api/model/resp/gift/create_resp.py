from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class CreateResp:
    """
    创建礼品卡响应
    """
    card_num: Optional[str] = None  # 礼品卡卡号
    card_key: Optional[str] = None  # 礼品卡兑换码
    amount: Optional[str] = None  # 礼品卡金额
    currency: Optional[str] = None  # 礼品卡币种
    status: int = 0  # 礼品卡状态
    card_temp_id: Optional[str] = None  # 礼品卡封面ID
    creator: int = 0  # 创建人
    creator_name: Optional[str] = None  # 礼品卡创建人名字
    exchange_uid: int = 0
    owner: int = 0
    give_count: int = 0
    last_give_time: int = 0
    create_time: int = 0  # 创建时间
    batchId: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CreateResp':
        return cls(**data)