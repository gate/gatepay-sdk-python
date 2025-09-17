from pydantic import BaseModel, Field
from typing import Optional


def to_camel(string: str) -> str:
    """Convert snake_case to camelCase"""
    if '_' not in string:
        return string
    components = string.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


class GoodsReq(BaseModel):
    """
    商品请求
    """

    # 商品类型
    goods_type: Optional[str] = Field(None, alias='goodsType')

    # 商品名称
    goods_name: Optional[str] = Field(None, alias='goodsName')

    # 商品详情
    goods_detail: Optional[str] = Field(None, alias='goodsDetail')

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

    def get_goods_type(self) -> str:
        """
        获取商品类型

        Returns:
            str: 商品类型
        """
        return self.goods_type

    def set_goods_type(self, goods_type: str):
        """
        设置商品类型

        Args:
            goods_type (str): 商品类型
        """
        self.goods_type = goods_type

    def get_goods_name(self) -> str:
        """
        获取商品名称

        Returns:
            str: 商品名称
        """
        return self.goods_name

    def set_goods_name(self, goods_name: str):
        """
        设置商品名称

        Args:
            goods_name (str): 商品名称
        """
        self.goods_name = goods_name

    def get_goods_detail(self) -> str:
        """
        获取商品详情

        Returns:
            str: 商品详情
        """
        return self.goods_detail

    def set_goods_detail(self, goods_detail: str):
        """
        设置商品详情

        Args:
            goods_detail (str): 商品详情
        """
        self.goods_detail = goods_detail

    def to_dict(self):
        """
        转换为字典，使用驼峰命名以供HTTP传输

        Returns:
            dict: 包含camelCase键的字典
        """
        return self.dict(by_alias=True, exclude_none=True, exclude_defaults=True)

    def __str__(self) -> str:
        """
        返回对象的字符串表示

        Returns:
            str: 对象的字符串表示
        """
        return f"GoodsReq(goods_type={self.goods_type}, goods_name={self.goods_name}, goods_detail={self.goods_detail})"

    def __repr__(self) -> str:
        """
        返回对象的详细字符串表示

        Returns:
            str: 对象的详细字符串表示
        """
        return self.__str__()
