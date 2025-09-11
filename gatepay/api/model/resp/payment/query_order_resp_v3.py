

from dataclasses import dataclass, field
from typing import Optional, List

from gatepay.api.model.resp.payment.query_order_resp import QueryOrderResp


@dataclass
class ConfirmItem:
    amount: str = ""
    confirm: int = 0

@dataclass
class ChainTransactionInfo:
    done_amount: str = ""
    confirming_list: List[ConfirmItem] = field(default_factory=list)

@dataclass
class WhiteBrandInfo:
    logo_url: str = ""
    brand: str = ""
    pay_ways: List[str] = field(default_factory=list)

class QueryOrderRespV3(QueryOrderResp):
    """
    支付查询订单响应
    """

    def __init__(self):
        """
        初始化QueryOrderResp对象
        """
        super().__init__()

        self.total_fee = None
        self.return_url = 0
        self.merchant_name = None
        self.location = None
        self.scheme = None
        self.white_brand_info: Optional[WhiteBrandInfo] = None
        self.qr_code: str = ""
        self.tx_hash: str = ""
        self.address: str = ""
        self.chain: str = ""
        self.full_curr_type: str = ""
        self.from_address: str = ""
        self.show_chain_name_en: str = ""
        self.transaction_info: Optional[ChainTransactionInfo] = None

    # QueryOrderRespV3 getters and setters
    def get_total_fee(self):
        return self.total_fee

    def set_total_fee(self, total_fee):
        self.total_fee = total_fee

    def get_return_url(self) -> int:
        return self.return_url

    def set_return_url(self, return_url: int):
        self.return_url = return_url

    def get_merchant_name(self):
        return self.merchant_name

    def set_merchant_name(self, merchant_name):
        self.merchant_name = merchant_name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_scheme(self):
        return self.scheme

    def set_scheme(self, scheme):
        self.scheme = scheme

    def get_white_brand_info(self) -> Optional[WhiteBrandInfo]:
        return self.white_brand_info

    def set_white_brand_info(self, white_brand_info: Optional[WhiteBrandInfo]):
        self.white_brand_info = white_brand_info

    def get_qr_code(self) -> str:
        return self.qr_code

    def set_qr_code(self, qr_code: str):
        self.qr_code = qr_code

    def get_tx_hash(self) -> str:
        return self.tx_hash

    def set_tx_hash(self, tx_hash: str):
        self.tx_hash = tx_hash

    def get_address(self) -> str:
        return self.address

    def set_address(self, address: str):
        self.address = address

    def get_chain(self) -> str:
        return self.chain

    def set_chain(self, chain: str):
        self.chain = chain

    def get_full_curr_type(self) -> str:
        return self.full_curr_type

    def set_full_curr_type(self, full_curr_type: str):
        self.full_curr_type = full_curr_type

    def get_from_address(self) -> str:
        return self.from_address

    def set_from_address(self, from_address: str):
        self.from_address = from_address

    def get_show_chain_name_en(self) -> str:
        return self.show_chain_name_en

    def set_show_chain_name_en(self, show_chain_name_en: str):
        self.show_chain_name_en = show_chain_name_en

    def get_transaction_info(self) -> Optional[ChainTransactionInfo]:
        return self.transaction_info

    def set_transaction_info(self, transaction_info: Optional[ChainTransactionInfo]):
        self.transaction_info = transaction_info