from dataclasses import dataclass
from gatepay.base_response import BaseResponse

@dataclass
class DeleteResp(BaseResponse['DeleteResp']):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    pass
