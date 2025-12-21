from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateBatchTransferResp:
    batch_id: Optional[str] = None
    merchant_batch_no: Optional[str] = None
