from src.gatepay.api.api_address import ApiAddress
from src.gatepay.api.api_bill import ApiBill
from src.gatepay.api.api_channel_manage import ApiChannelManage
from src.gatepay.api.api_checkout import ApiCheckout
from src.gatepay.api.api_convert import ApiConvert
from src.gatepay.api.api_gift import ApiGift
from src.gatepay.api.api_payment import ApiPayment
from src.gatepay.api.api_qrcode import ApiQrCode
from src.gatepay.api.api_withdraw import ApiWithdraw
from src.gatepay.api.model.req.address.create_order_req import CreateOrderReq as AddressCreateOrderReq
from src.gatepay.api.model.req.address.create_refund_req import CreateRefundReq as AddressCreateRefundReq
from src.gatepay.api.model.req.address.query_order_req import QueryOrderReq as AddressQueryOrderReq
from src.gatepay.api.model.req.chain_req import ChainsReq
from src.gatepay.api.model.req.checkout.create_order_req import CreateOrderReq as CheckoutCreateOrderReq
from src.gatepay.api.model.req.checkout.create_refund_req import CreateRefundReq as CheckoutCreateRefundReq
from src.gatepay.api.model.req.close_order_req import CloseOrderReq
from src.gatepay.api.model.req.convert.create_order_req import CreateOrderReq as ConvertCreateOrderReq
from src.gatepay.api.model.req.convert.query_order_req import QueryOrderReq as ConvertQueryOrderReq
from src.gatepay.api.model.req.create_batch_transfer_req import CreateBatchTransferReq
from src.gatepay.api.model.req.create_refund_convert_req import CreateRefundConvertReq
from src.gatepay.api.model.req.gift.create_req import CreateReq
from src.gatepay.api.model.req.gift.list_temp_req import ListTempReq
from src.gatepay.api.model.req.gift.query_req import QueryReq
from src.gatepay.api.model.req.manage.delete_req import DeleteReq
from src.gatepay.api.model.req.manage.list_req import ListReq
from src.gatepay.api.model.req.manage.save_req import SaveReq
from src.gatepay.api.model.req.manage.update_req import UpdateReq
from src.gatepay.api.model.req.payment.create_order_req import CreateOrderReq as PaymentCreateOrderReq
from src.gatepay.api.model.req.payment.create_refund_req import CreateRefundReq as PaymentCreateRefundReq
from src.gatepay.api.model.req.payment.create_refund_req_v3 import CreateRefundReqV3 as PaymentCreateRefundReqV3
from src.gatepay.api.model.req.payment.query_balance_req import QueryBalanceReq as PaymentQueryBalanceReq
from src.gatepay.api.model.req.payment.query_order_req import QueryOrderReq as PaymentQueryOrderReq
from src.gatepay.api.model.req.payment.query_order_req_v3 import QueryOrderReqV3 as PaymentQueryOrderReqV3
from src.gatepay.api.model.req.payment.query_refund_req import QueryRefundReq
from src.gatepay.api.model.req.payment.query_refund_req_v3 import QueryRefundReqV3 as PaymentQueryRefundReqV3
from src.gatepay.api.model.req.payment.query_refund_support_chains_req import QueryRefundSupportChainsReqV3
from src.gatepay.api.model.req.preview_req import PreviewReq
from src.gatepay.api.model.req.qrcode.create_order_req import CreateOrderReq as QrCodeCreateOrderReq
from src.gatepay.api.model.req.query_batch_transfer_req import QueryBatchTransferReq
from src.gatepay.api.model.req.query_chains_req import QueryChainsReq
from src.gatepay.api.model.req.query_currency_req import QueryCurrencyReq
from src.gatepay.api.model.req.query_orders_req import QueryOrdersReq
from src.gatepay.api.model.req.query_pair_req import QueryPairReq
from src.gatepay.api.model.req.query_status_req import QueryStatusReq
from src.gatepay.api.model.req.supported_convert_currencies_req import SupportedConvertCurrenciesReq
from src.gatepay.api.model.req.transaction_detail_req import TransactionDetailReq
from src.gatepay.api.model.req.withdraw.create_order_req import CreateOrderReq as WithdrawCreateOrderReq
from src.gatepay.api.model.req.withdraw.query_balance_req import QueryBalanceReq as WithdrawQueryBalanceReq
from src.gatepay.api.model.req.withdraw.query_order_req import QueryOrderReq as WithdrawQueryOrderReq
from src.gatepay.api.model.resp.address.create_order_resp import CreateOrderResp as AddressCreateOrderResp
from src.gatepay.api.model.resp.address.create_refund_resp import CreateRefundResp as AddressCreateRefundResp
from src.gatepay.api.model.resp.address.query_order_resp import QueryOrderResp as AddressQueryOrderResp
from src.gatepay.api.model.resp.chains_resp import ChainsResp
from src.gatepay.api.model.resp.checkout.create_order_resp import CreateOrderResp as CheckoutCreateOrderResp
from src.gatepay.api.model.resp.checkout.create_refund_resp import CreateRefundResp as CheckoutCreateRefundResp
from src.gatepay.api.model.resp.close_order_resp import CloseOrderResp
from src.gatepay.api.model.resp.convert.create_order_resp import CreateOrderResp as ConvertCreateOrderResp
from src.gatepay.api.model.resp.convert.query_order_resp import QueryOrderResp as ConvertQueryOrderResp
from src.gatepay.api.model.resp.create_batch_transfer_resp import CreateBatchTransferResp
from src.gatepay.api.model.resp.create_refund_convert_resp import CreateRefundConvertResp
from src.gatepay.api.model.resp.currencies_resp import CurrenciesResp
from src.gatepay.api.model.resp.gift.create_resp import CreateResp
from src.gatepay.api.model.resp.gift.list_temp_resp import ListTempResp
from src.gatepay.api.model.resp.gift.query_resp import QueryResp
from src.gatepay.api.model.resp.manage.delete_resp import DeleteResp
from src.gatepay.api.model.resp.manage.list_resp import ListResp
from src.gatepay.api.model.resp.manage.save_resp import SaveResp
from src.gatepay.api.model.resp.manage.update_resp import UpdateResp
from src.gatepay.api.model.resp.payment.create_order_resp import CreateOrderResp as PaymentCreateOrderResp
from src.gatepay.api.model.resp.payment.create_refund_resp import CreateRefundResp as PaymentCreateRefundResp
from src.gatepay.api.model.resp.payment.create_refund_resp_v3 import CreateRefundRespV3 as PaymentCreateRefundRespV3
from src.gatepay.api.model.resp.payment.query_balance_resp import QueryBalanceResp as PaymentQueryBalanceResp
from src.gatepay.api.model.resp.payment.query_order_resp import QueryOrderResp as PaymentQueryOrderResp
from src.gatepay.api.model.resp.payment.query_order_resp_v3 import QueryOrderRespV3 as PaymentQueryOrderRespV3
from src.gatepay.api.model.resp.payment.query_refund_resp import QueryRefundResp
from src.gatepay.api.model.resp.payment.query_refund_resp_v3 import QueryRefundRespV3 as PaymentQueryRefundRespV3
from src.gatepay.api.model.resp.preview_resp import PreviewResp
from src.gatepay.api.model.resp.qrcode.create_order_resp import CreateOrderResp as QrCodeCreateOrderResp
from src.gatepay.api.model.resp.query_batch_transfer_resp import QueryBatchTransferResp
from src.gatepay.api.model.resp.query_chains_resp import QueryChainsResp
from src.gatepay.api.model.resp.query_currency_resp import QueryCurrencyResp
from src.gatepay.api.model.resp.query_orders_resp import QueryOrdersResp
from src.gatepay.api.model.resp.query_pair_resp import QueryPairResp
from src.gatepay.api.model.resp.query_status_resp import QueryStatusResp
from src.gatepay.api.model.resp.supported_convert_currencies_resp import SupportedConvertCurrenciesResp
from src.gatepay.api.model.resp.transaction_detail_resp import TransactionDetailResp
from src.gatepay.api.model.resp.withdraw.create_order_resp import CreateOrderResp as WithdrawCreateOrderResp
from src.gatepay.api.model.resp.withdraw.query_balance_resp import QueryBalanceResp as WithdrawQueryBalanceResp
from src.gatepay.api.model.resp.withdraw.query_order_resp import QueryOrderResp as WithdrawQueryOrderResp
from src.gatepay.client.gatepay_resp import GatePayResp
from src.gatepay.gatepay_config import GatePayConfig


class GatePayClient:
    """
    @Description: GatePayClient 客户端
    @Author: ZJ-BE
    @Date: 2025/07/25
    """

    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 GatePayClient 实例

        :param gate_pay_config: GatePay配置
        """
        self.api_address = ApiAddress(gate_pay_config)
        self.api_bill = ApiBill(gate_pay_config)
        self.api_channel_manage = ApiChannelManage(gate_pay_config)
        self.api_checkout = ApiCheckout(gate_pay_config)
        self.api_convert = ApiConvert(gate_pay_config)
        self.api_gift = ApiGift(gate_pay_config)
        self.api_payment = ApiPayment(gate_pay_config)
        self.api_qr_code = ApiQrCode(gate_pay_config)
        self.api_withdraw = ApiWithdraw(gate_pay_config)

    # 地址支付相关方法
    def gets_address_chains(self, request: ChainsReq) -> GatePayResp[ChainsResp]:
        """
        查询支持链列表

        :param request: 请求参数
        :return: GatePayResp<ChainsResp>
        """
        return GatePayResp(self.api_address.get_address_chains(request))

    def gets_address_currencies(self) -> GatePayResp[CurrenciesResp]:
        """
        查询支持币种列表

        :return: GatePayResp<CurrenciesResp>
        """
        return GatePayResp(self.api_address.get_address_currencies())

    def get_address_supported_convert_currencies(self, request: SupportedConvertCurrenciesReq) -> GatePayResp[
        SupportedConvertCurrenciesResp]:
        """
        创建闪兑地址支付单之前，根据订单币种查询支持闪兑的币种，
        用户从支持闪兑的币种列表中选择实际支付币种创建闪兑支付订单

        :param request: 请求参数
        :return: GatePayResp<SupportedConvertCurrenciesResp>
        """
        return GatePayResp(self.api_address.get_supported_convert_currencies(request))

    def create_address_order(self, request: AddressCreateOrderReq) -> GatePayResp[AddressCreateOrderResp]:
        """
        创建地址支付订单/下单

        :param request: 请求参数
        :return: GatePayResp<CreateOrderResp>
        """
        return GatePayResp(self.api_address.create_order(request))

    def query_address_order(self, request: AddressQueryOrderReq) -> GatePayResp[AddressQueryOrderResp]:
        """
        查询地址支付订单详情

        :param request: 请求参数
        :return: GatePayResp<QueryOrderResp>
        """
        return GatePayResp(self.api_address.query_order(request))

    def create_address_refund(self, request: AddressCreateRefundReq) -> GatePayResp[AddressCreateRefundResp]:
        """
        创建非闪兑支付单退款

        :param request: 请求参数
        :return: GatePayResp<CreateRefundResp>
        """
        return GatePayResp(self.api_address.create_refund(request))

    def create_address_refund_convert(self, request: CreateRefundConvertReq) -> GatePayResp[CreateRefundConvertResp]:
        """
        创建闪兑支付单退款

        :param request: 请求参数
        :return: GatePayResp<CreateRefundConvertResp>
        """
        return GatePayResp(self.api_address.create_refund_convert(request))

    def address_transaction_detail(self, request: TransactionDetailReq) -> GatePayResp[TransactionDetailResp]:
        """
        查询链上交易详情

        :param request: 请求参数
        :return: GatePayResp<TransactionDetailResp>
        """
        return GatePayResp(self.api_address.transaction_detail(request))

    # 账单相关方法
    def query_bill_orders(self, request: QueryOrdersReq) -> GatePayResp[QueryOrdersResp]:
        """
        获取资金流水账单

        :param request: 请求参数
        :return: GatePayResp<QueryOrdersResp>
        """
        return GatePayResp(self.api_bill.query_orders(request))

    # 渠道管理相关方法
    def save_channel_manage(self, request: SaveReq) -> GatePayResp[SaveResp]:
        """
        新增客户渠道

        :param request: 请求参数
        :return: GatePayResp<SaveResp>
        """
        return GatePayResp(self.api_channel_manage.save(request))

    def list_channel_manage(self, request: ListReq) -> GatePayResp[ListResp]:
        """
        查询客户渠道列表

        :param request: 请求参数
        :return: GatePayResp<ListResp>
        """
        return GatePayResp(self.api_channel_manage.list(request))

    def update_channel_manage(self, request: UpdateReq) -> GatePayResp[UpdateResp]:
        """
        修改客户渠道

        :param request: 请求参数
        :return: GatePayResp<UpdateResp>
        """
        return GatePayResp(self.api_channel_manage.update(request))

    def delete_channel_manage(self, request: DeleteReq) -> GatePayResp[DeleteResp]:
        """
        删除客户渠道

        :param request: 请求参数
        :return: GatePayResp<DeleteResp>
        """
        return GatePayResp(self.api_channel_manage.delete(request))

    # 收银台相关方法
    def create_checkout_order(self, request: CheckoutCreateOrderReq) -> GatePayResp[CheckoutCreateOrderResp]:
        """
        创建收银台订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.checkout.model.resp.CreateOrderResp>
        """
        return GatePayResp(self.api_checkout.create_order(request))

    def create_checkout_refund(self, request: CheckoutCreateRefundReq) -> GatePayResp[CheckoutCreateRefundResp]:
        """
        创建退款

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.checkout.model.resp.CreateRefundResp>
        """
        return GatePayResp(self.api_checkout.create_refund(request))

    # 闪兑相关方法
    def query_convert_currency(self, request: QueryCurrencyReq) -> GatePayResp[QueryCurrencyResp]:
        """
        查询可用闪兑币种

        :param request: 请求参数
        :return: GatePayResp<QueryCurrencyResp>
        """
        return GatePayResp(self.api_convert.query_currency(request))

    def query_convert_pair(self, request: QueryPairReq) -> GatePayResp[QueryPairResp]:
        """
        查询可用币种对

        :param request: 请求参数
        :return: GatePayResp<QueryPairResp>
        """
        return GatePayResp(self.api_convert.query_pair(request))

    def preview_convert(self, request: PreviewReq) -> GatePayResp[PreviewResp]:
        """
        预览报价

        :param request: 请求参数
        :return: GatePayResp<PreviewResp>
        """
        return GatePayResp(self.api_convert.preview(request))

    def create_convert_order(self, request: ConvertCreateOrderReq) -> GatePayResp[ConvertCreateOrderResp]:
        """
        闪兑下单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.convert.model.resp.CreateOrderResp>
        """
        return GatePayResp(self.api_convert.create_order(request))

    def query_convert_order(self, request: ConvertQueryOrderReq) -> GatePayResp[ConvertQueryOrderResp]:
        """
        查询闪兑订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.convert.model.resp.QueryOrderResp>
        """
        return GatePayResp(self.api_convert.query_order(request))

    # 礼品卡相关方法
    def create_gift(self, request: CreateReq) -> GatePayResp[CreateResp]:
        """
        创建礼品卡

        :param request: 请求参数
        :return: GatePayResp<CreateResp>
        """
        return GatePayResp(self.api_gift.create(request))

    def list_gift_temp(self, request: ListTempReq) -> GatePayResp[ListTempResp]:
        """
        列出礼品卡模板

        :param request: 请求参数
        :return: GatePayResp<ListTempResp>
        """
        return GatePayResp(self.api_gift.list_temp(request))

    def query_gift(self, request: QueryReq) -> GatePayResp[QueryResp]:
        """
        查询礼品卡

        :param request: 请求参数
        :return: GatePayResp<QueryResp>
        """
        return GatePayResp(self.api_gift.query(request))

    # 二维码支付相关方法
    def create_qr_code_order(self, request: QrCodeCreateOrderReq) -> GatePayResp[QrCodeCreateOrderResp]:
        """
        创建扫码支付订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.qrcode.model.resp.CreateOrderResp>
        """
        return GatePayResp(self.api_qr_code.create_order(request))

    # Web支付相关方法
    def create_web_order(self, request: PaymentCreateOrderReq) -> GatePayResp[PaymentCreateOrderResp]:
        """
        创建web支付订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.payment.model.resp.CreateOrderResp>
        """
        return GatePayResp(self.api_payment.create_order(request))

    def query_web_order(self, request: PaymentQueryOrderReq) -> GatePayResp[PaymentQueryOrderResp]:
        """
        查询订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.payment.model.resp.QueryOrderResp>
        """
        return GatePayResp(self.api_payment.query_order(request))

    def close_web_order(self, request: CloseOrderReq) -> GatePayResp[CloseOrderResp]:
        """
        关闭订单

        :param request: 请求参数
        :return: GatePayResp<CloseOrderResp>
        """
        return GatePayResp(self.api_payment.close_order(request))

    def create_web_refund(self, request: PaymentCreateRefundReq) -> GatePayResp[PaymentCreateRefundResp]:
        """
        创建退款订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.payment.model.resp.CreateRefundResp>
        """
        return GatePayResp(self.api_payment.create_refund(request))

    def query_web_refund(self, request: QueryRefundReq) -> GatePayResp[QueryRefundResp]:
        """
        查询退款订单

        :param request: 请求参数
        :return: GatePayResp<QueryRefundResp>
        """
        return GatePayResp(self.api_payment.query_refund(request))

    def create_batch_transfer(self, request: CreateBatchTransferReq) -> GatePayResp[CreateBatchTransferResp]:
        """
        创建批量转账

        :param request: 请求参数
        :return: GatePayResp<CreateBatchTransferResp>
        """
        return GatePayResp(self.api_payment.create_batch_transfer(request))

    def query_batch_transfer(self, request: QueryBatchTransferReq) -> GatePayResp[QueryBatchTransferResp]:
        """
        查询批量转账

        :param request: 请求参数
        :return: GatePayResp<QueryBatchTransferResp>
        """
        return GatePayResp(self.api_payment.query_batch_transfer(request))

    def query_balance(self, request: PaymentQueryBalanceReq) -> GatePayResp[PaymentQueryBalanceResp]:
        """
        查询余额

        :param request: 请求参数
        :return: GatePayResp<QueryBalanceResp>
        """
        return GatePayResp(self.api_payment.query_balance(request))

    # 提现相关方法
    def create_withdraw_order(self, request: WithdrawCreateOrderReq) -> GatePayResp[WithdrawCreateOrderResp]:
        """
        创建提现订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.withdraw.model.resp.CreateOrderResp>
        """
        return GatePayResp(self.api_withdraw.create_order(request))

    def query_withdraw_order(self, request: WithdrawQueryOrderReq) -> GatePayResp[WithdrawQueryOrderResp]:
        """
        查询提现订单

        detail_status:
        ALL 全部子订单
        PENDING 待处理子订单
        PROCESSING 已提交提现请求，待确认子订单
        CHECK 审核中子订单
        FAIL 失败子订单
        DONE 提现成功子订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.withdraw.model.resp.QueryOrderResp>
        """
        return GatePayResp(self.api_withdraw.query_order(request))

    def query_withdraw_chains(self, request: QueryChainsReq) -> GatePayResp[QueryChainsResp]:
        """
        查询币种支持的链

        :param request: 请求参数
        :return: GatePayResp<QueryChainsResp>
        """
        return GatePayResp(self.api_withdraw.query_chains(request))

    def query_withdraw_balance(self, request: WithdrawQueryBalanceReq) -> GatePayResp[WithdrawQueryBalanceResp]:
        """
        查询个人账户余额

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.withdraw.model.resp.QueryBalanceResp>
        """
        return GatePayResp(self.api_withdraw.query_balance(request))

    def query_withdraw_status(self, request: QueryStatusReq) -> GatePayResp[QueryStatusResp]:
        """
        查询提现状态

        :param request: 请求参数
        :return: GatePayResp<QueryStatusResp>
        """
        return GatePayResp(self.api_withdraw.query_status(request))

    def query_web_order_v3(self, request: PaymentQueryOrderReqV3) -> GatePayResp[PaymentQueryOrderRespV3]:
        """
        查询订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.payment.model.resp.QueryOrderRespV3>
        """
        return GatePayResp(self.api_payment.query_order_v3(request))

    def query_web_refund_support_chains_v3(self, request: QueryRefundSupportChainsReqV3) -> GatePayResp[ChainsResp]:
        """
        查询订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.model.resp.ChainsResp>
        """
        return GatePayResp(self.api_payment.query_refund_support_chain(request))

    def create_web_refund_v3(self, request: PaymentCreateRefundReqV3) -> GatePayResp[PaymentCreateRefundRespV3]:
        """
        查询订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.model.resp.payment.PaymentCreateRefundRespV3>
        """
        return GatePayResp(self.api_payment.create_refund_v3(request))

    def query_web_refund_v3(self, request: PaymentQueryRefundReqV3) -> GatePayResp[PaymentQueryRefundRespV3]:
        """
        查询订单

        :param request: 请求参数
        :return: GatePayResp<com.gatepay.core.api.model.resp.payment.PaymentQueryRefundRespV3>
        """
        return GatePayResp(self.api_payment.query_refund_v3(request))
