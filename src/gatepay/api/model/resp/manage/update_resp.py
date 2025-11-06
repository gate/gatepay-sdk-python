from dataclasses import dataclass
from src.gatepay.base_response import BaseResponse

@dataclass
class UpdateResp(BaseResponse['UpdateResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    pass
