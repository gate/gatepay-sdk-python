from typing import Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class ListTempResp(BaseResponse['ListTempResp']):
    """
    列出礼品卡模板响应
    """
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    # 卡模板ID
    card_temp_id: Optional[str] = None

    # 图片URL
    image_url: Optional[str] = None

    # 英文标题
    title_en: Optional[str] = None

    # 中文标题
    title_cn: Optional[str] = None

    # 封面类型
    cover_type: Optional[str] = None

    def get_card_temp_id(self) -> Optional[str]:
        """
        获取卡模板ID

        :return: 卡模板ID
        """
        return self.card_temp_id

    def set_card_temp_id(self, card_temp_id: str) -> None:
        """
        设置卡模板ID

        :param card_temp_id: 卡模板ID
        """
        self.card_temp_id = card_temp_id

    def get_image_url(self) -> Optional[str]:
        """
        获取图片URL

        :return: 图片URL
        """
        return self.image_url

    def set_image_url(self, image_url: str) -> None:
        """
        设置图片URL

        :param image_url: 图片URL
        """
        self.image_url = image_url

    def get_title_en(self) -> Optional[str]:
        """
        获取英文标题

        :return: 英文标题
        """
        return self.title_en

    def set_title_en(self, title_en: str) -> None:
        """
        设置英文标题

        :param title_en: 英文标题
        """
        self.title_en = title_en

    def get_title_cn(self) -> Optional[str]:
        """
        获取中文标题

        :return: 中文标题
        """
        return self.title_cn

    def set_title_cn(self, title_cn: str) -> None:
        """
        设置中文标题

        :param title_cn: 中文标题
        """
        self.title_cn = title_cn

    def get_cover_type(self) -> Optional[str]:
        """
        获取封面类型

        :return: 封面类型
        """
        return self.cover_type

    def set_cover_type(self, cover_type: str) -> None:
        """
        设置封面类型

        :param cover_type: 封面类型
        """
        self.cover_type = cover_type
