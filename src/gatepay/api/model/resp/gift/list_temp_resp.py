from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class ListTempResp:
    """
    礼品卡模板列表响应
    """
    card_temp_id: Optional[str] = None
    image_url: Optional[str] = None
    title_en: Optional[str] = None
    title_cn: Optional[str] = None
    cover_type: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ListTempResp':
        return cls(**data)