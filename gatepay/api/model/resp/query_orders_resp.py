from typing import List, Optional
from dataclasses import dataclass

from gatepay.base_response import BaseResponse


@dataclass
class BalanceHistoryItem:

    # 支付流水单号
    transact_id: Optional[str] = None

    # 入账时间，毫秒时间戳
    transact_time: int = 0

    # GatePay订单号
    order_id: Optional[str] = None

    # 商户订单号
    merchant_trade_no: Optional[str] = None

    # 财务类型
    financial_type: Optional[str] = None

    # 收支金额
    pay_amount: Optional[str] = None

    # 收支币种
    currency: Optional[str] = None

    # 账户余额
    balance: Optional[str] = None

    # 账户余额币种
    balance_currency: Optional[str] = None

    # PAID表示成功
    status: Optional[str] = None

    # Gate支付付款用户UID
    payer: int = 0

    # 对方信息: Web3支付该值为付款地址，非Web3支付为付款人UID
    buyer: Optional[str] = None

    # 退款订单ID
    refund_gate_id: Optional[str] = None

    # 支付方式: Web3 支付, Gate 支付
    pay_channel: Optional[str] = None

    # 支付网络全称
    full_chain: Optional[str] = None

    # 商家收款地址
    address: Optional[str] = None

    # 交易hash
    hash: Optional[str] = None

    def get_transact_id(self) -> Optional[str]:
        """
        获取支付流水单号

        :return: 支付流水单号
        """
        return self.transact_id

    def set_transact_id(self, transact_id: str) -> None:
        """
        设置支付流水单号

        :param transact_id: 支付流水单号
        """
        self.transact_id = transact_id

    def get_transact_time(self) -> int:
        """
        获取入账时间

        :return: 入账时间戳(毫秒)
        """
        return self.transact_time

    def set_transact_time(self, transact_time: int) -> None:
        """
        设置入账时间

        :param transact_time: 入账时间戳(毫秒)
        """
        self.transact_time = transact_time

    def get_order_id(self) -> Optional[str]:
        """
        获取GatePay订单号

        :return: GatePay订单号
        """
        return self.order_id

    def set_order_id(self, order_id: str) -> None:
        """
        设置GatePay订单号

        :param order_id: GatePay订单号
        """
        self.order_id = order_id

    def get_merchant_trade_no(self) -> Optional[str]:
        """
        获取商户订单号

        :return: 商户订单号
        """
        return self.merchant_trade_no

    def set_merchant_trade_no(self, merchant_trade_no: str) -> None:
        """
        设置商户订单号

        :param merchant_trade_no: 商户订单号
        """
        self.merchant_trade_no = merchant_trade_no

    def get_financial_type(self) -> Optional[str]:
        """
        获取财务类型

        :return: 财务类型
        """
        return self.financial_type

    def set_financial_type(self, financial_type: str) -> None:
        """
        设置财务类型

        :param financial_type: 财务类型
        """
        self.financial_type = financial_type

    def get_pay_amount(self) -> Optional[str]:
        """
        获取收支金额

        :return: 收支金额
        """
        return self.pay_amount

    def set_pay_amount(self, pay_amount: str) -> None:
        """
        设置收支金额

        :param pay_amount: 收支金额
        """
        self.pay_amount = pay_amount

    def get_currency(self) -> Optional[str]:
        """
        获取收支币种

        :return: 收支币种
        """
        return self.currency

    def set_currency(self, currency: str) -> None:
        """
        设置收支币种

        :param currency: 收支币种
        """
        self.currency = currency

    def get_balance(self) -> Optional[str]:
        """
        获取账户余额

        :return: 账户余额
        """
        return self.balance

    def set_balance(self, balance: str) -> None:
        """
        设置账户余额

        :param balance: 账户余额
        """
        self.balance = balance

    def get_balance_currency(self) -> Optional[str]:
        """
        获取账户余额币种

        :return: 账户余额币种
        """
        return self.balance_currency

    def set_balance_currency(self, balance_currency: str) -> None:
        """
        设置账户余额币种

        :param balance_currency: 账户余额币种
        """
        self.balance_currency = balance_currency

    def get_status(self) -> Optional[str]:
        """
        获取状态

        :return: 状态
        """
        return self.status

    def set_status(self, status: str) -> None:
        """
        设置状态

        :param status: 状态
        """
        self.status = status

    def get_payer(self) -> int:
        """
        获取Gate支付付款用户UID

        :return: 付款用户UID
        """
        return self.payer

    def set_payer(self, payer: int) -> None:
        """
        设置Gate支付付款用户UID

        :param payer: 付款用户UID
        """
        self.payer = payer

    def get_buyer(self) -> Optional[str]:
        """
        获取对方信息

        :return: 对方信息
        """
        return self.buyer

    def set_buyer(self, buyer: str) -> None:
        """
        设置对方信息

        :param buyer: 对方信息
        """
        self.buyer = buyer

    def get_refund_gate_id(self) -> Optional[str]:
        """
        获取退款订单ID

        :return: 退款订单ID
        """
        return self.refund_gate_id

    def set_refund_gate_id(self, refund_gate_id: str) -> None:
        """
        设置退款订单ID

        :param refund_gate_id: 退款订单ID
        """
        self.refund_gate_id = refund_gate_id

    def get_pay_channel(self) -> Optional[str]:
        """
        获取支付方式

        :return: 支付方式
        """
        return self.pay_channel

    def set_pay_channel(self, pay_channel: str) -> None:
        """
        设置支付方式

        :param pay_channel: 支付方式
        """
        self.pay_channel = pay_channel

    def get_full_chain(self) -> Optional[str]:
        """
        获取支付网络全称

        :return: 支付网络全称
        """
        return self.full_chain

    def set_full_chain(self, full_chain: str) -> None:
        """
        设置支付网络全称

        :param full_chain: 支付网络全称
        """
        self.full_chain = full_chain

    def get_address(self) -> Optional[str]:
        """
        获取商家收款地址

        :return: 商家收款地址
        """
        return self.address

    def set_address(self, address: str) -> None:
        """
        设置商家收款地址

        :param address: 商家收款地址
        """
        self.address = address

    def get_hash(self) -> Optional[str]:
        """
        获取交易hash

        :return: 交易hash
        """
        return self.hash

    def set_hash(self, hash: str) -> None:
        """
        设置交易hash

        :param hash: 交易hash
        """
        self.hash = hash


@dataclass
class QueryOrdersResp(BaseResponse['QueryOrdersResp']):
    """
    查询订单响应
    """
    def __init__(self):
        super().__init__()
        # 确保所有属性都被初始化

    merchant_id: int = 0
    total: int = 0
    has_next: bool = False
    next_page: int = 0
    balance_history_item_list: Optional[List[BalanceHistoryItem]] = None

    def get_total(self) -> int:
        """
        获取总记录数

        :return: 总记录数
        """
        return self.total

    def set_total(self, total: int) -> None:
        """
        设置总记录数

        :param total: 总记录数
        """
        self.total = total

    def is_has_next(self) -> bool:
        """
        是否有下一页

        :return: 是否有下一页
        """
        return self.has_next

    def set_has_next(self, has_next: bool) -> None:
        """
        设置是否有下一页

        :param has_next: 是否有下一页
        """
        self.has_next = has_next

    def get_next_page(self) -> int:
        """
        获取下一页页码

        :return: 下一页页码
        """
        return self.next_page

    def set_next_page(self, next_page: int) -> None:
        """
        设置下一页页码

        :param next_page: 下一页页码
        """
        self.next_page = next_page

    def get_merchant_id(self) -> int:
        """
        获取商户ID

        :return: 商户ID
        """
        return self.merchant_id

    def set_merchant_id(self, merchant_id: int) -> None:
        """
        设置商户ID

        :param merchant_id: 商户ID
        """
        self.merchant_id = merchant_id

    def get_balance_history_item_list(self) -> Optional[List[BalanceHistoryItem]]:
        """
        获取余额历史记录列表

        :return: 余额历史记录列表
        """
        return self.balance_history_item_list

    def set_balance_history_item_list(self, balance_history_item_list: List[BalanceHistoryItem]) -> None:
        """
        设置余额历史记录列表

        :param balance_history_item_list: 余额历史记录列表
        """
        self.balance_history_item_list = balance_history_item_list
