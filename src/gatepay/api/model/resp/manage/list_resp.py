from dataclasses import dataclass
from typing import Optional, List, Dict, Any

from src.gatepay.api.model.merchant_channel import MerchantChannel


@dataclass
class ListResp:
    """
    渠道管理列表响应
    """
    total: int = 0
    merchantChannelList: Optional[List['MerchantChannel']] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ListResp':
        merchant_channels = None
        if 'merchantChannelList' in data and data['merchantChannelList']:
            merchant_channels = [MerchantChannel.from_dict(channel_data) for channel_data in
                                 data['merchantChannelList']]

        return cls(
            total=data.get('total', 0),
            merchantChannelList=merchant_channels
        )