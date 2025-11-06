from dataclasses import dataclass
from src.gatepay.base_response import BaseResponse

@dataclass
class CreateBatchTransferResp(BaseResponse):
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    pass
