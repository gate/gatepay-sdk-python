import time
import unittest
from datetime import datetime

from src.gatepay.api.model.base_withdraw import Withdraw
from src.gatepay.api.model.batch_order import BatchOrder
from src.gatepay.api.model.custom_field import CustomField
from src.gatepay.api.model.merchant_channel import MerchantChannel
from src.gatepay.api.model.req.address.create_order_req import CreateOrderReq as AddressCreateOrderReq
from src.gatepay.api.model.req.address.create_refund_req import CreateRefundReq as AddressCreateRefundReq
from src.gatepay.api.model.req.address.query_order_req import QueryOrderReq as AddressQueryOrderReq
from src.gatepay.api.model.req.chain_req import ChainsReq
from src.gatepay.api.model.req.checkout.create_order_req import CreateOrderReq as CheckOutCreateOrderReq
from src.gatepay.api.model.req.checkout.create_refund_req import CreateRefundReq as CheckOutCreateRefundReq
from src.gatepay.api.model.req.close_order_req import CloseOrderReq
from src.gatepay.api.model.req.convert.create_order_req import CreateOrderReq as ConvertCreateOrderReq
from src.gatepay.api.model.req.convert.query_order_req import QueryOrderReq as ConvertQueryOrderReq
from src.gatepay.api.model.req.create_batch_transfer_req import CreateBatchTransferReq
from src.gatepay.api.model.req.create_refund_convert_req import CreateRefundConvertReq as AddressCreateRefundConvertReq
from src.gatepay.api.model.req.env_req import EnvReq
from src.gatepay.api.model.req.gift.create_req import CreateReq
from src.gatepay.api.model.req.gift.list_temp_req import ListTempReq
from src.gatepay.api.model.req.gift.query_req import QueryReq
from src.gatepay.api.model.req.goods_req import GoodsReq
from src.gatepay.api.model.req.manage.delete_req import DeleteReq
from src.gatepay.api.model.req.manage.list_req import ListReq
from src.gatepay.api.model.req.manage.save_req import SaveReq
from src.gatepay.api.model.req.manage.update_req import UpdateReq
from src.gatepay.api.model.req.payment.create_order_req import CreateOrderReq as PaymentCreateOrderReq
from src.gatepay.api.model.req.payment.create_refund_req import CreateRefundReq as PaymentCreateRefundReq
from src.gatepay.api.model.req.payment.create_refund_req_v3 import CreateRefundReqV3 as PaymentCreateRefundReqV3
from src.gatepay.api.model.req.payment.query_balance_req import QueryBalanceReq
from src.gatepay.api.model.req.payment.query_order_req import QueryOrderReq as WebQueryOrderReq
from src.gatepay.api.model.req.payment.query_order_req_v3 import QueryOrderReqV3 as WebQueryOrderReqV3
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
from src.gatepay.client.gatepay_client import GatePayClient
from src.gatepay.common.utils.random_utils import RandomUtils
from src.gatepay.gatepay_config import GatePayConfig
from src.gatepay.infrastructure.credential import Credential


class GatePayClientTest(unittest.TestCase):

    def init_gate_pay_client(self):
        """
        初始化GatePay客户端
        """
        gate_pay_config = GatePayConfig(
            "http://dev.halftrust.xyz/gfpay",
            30,
            "mZ96D37oKk-HrWJc",
            Credential("Mz6M_q4AkDnZCSoTDo03A6OtWzN5ut8_Uix3jyVjxAU=", "SkZlbKOqPoMwnxhl")
        )
        return GatePayClient(gate_pay_config)

    def test_get_address_chains(self):
        chains_req = ChainsReq()
        chains_req.set_currency("USDT")
        # 调用获取地址链的方法
        res=self.init_gate_pay_client().gets_address_chains(chains_req)
        print(res.get_data().__str__())

    def test_get_address_currencies(self):
        res =self.init_gate_pay_client().gets_address_currencies()
        print(res.get_data().__str__())

    def test_get_address_supported_convert_currencies(self):
        supported_convert_currencies_req = SupportedConvertCurrenciesReq()
        supported_convert_currencies_req.set_currency("USDT")
        res=self.init_gate_pay_client().get_address_supported_convert_currencies(supported_convert_currencies_req)
        print(res.get_data().__str__())

    def test_create_address_order(self):
        env_req = EnvReq()
        env_req.set_terminal_type("MINIAPP")

        # 创建商品请求对象
        goods_req = GoodsReq()
        goods_req.set_goods_name("test")
        goods_req.set_goods_detail("testDetail")
        # 创建地址订单请求对象
        create_order_req = AddressCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(24))
        create_order_req.set_currency("USDT")
        create_order_req.set_order_amount("9.9")
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        create_order_req.set_order_expire_time(int(time.time() * 1000) + 3 * 60 * 60 * 1000)
        create_order_req.set_return_url("https://www.gate.com/")
        create_order_req.set_cancel_url("https://www.gate.com/")
        create_order_req.set_merchant_user_id(6790011)
        create_order_req.set_chain("ETH")
        create_order_req.set_full_curr_type("USDT_ETH")
        create_order_req.set_channel_id("")
        print("merchantOrderNo:"+create_order_req.get_merchant_trade_no())
        create_order_resp=self.init_gate_pay_client().create_address_order(create_order_req)
        print(create_order_resp.get_data().__str__())

    def test_query_address_order(self):
        query_order_req=AddressQueryOrderReq()
        query_order_req.set_prepay_id("35297827964846503")
        query_order_req.set_merchant_trade_no("43wGhuujHKwAoLXRd7mMjihU")
        print(self.init_gate_pay_client().query_address_order(query_order_req).get_data().__str__())

        # todo test 订单状态未终态
    def test_create_address_refund(self):
        address_create_refund_req=AddressCreateRefundReq()
        address_create_refund_req.set_prepay_id("35297827964846503")
        address_create_refund_req.set_refund_request_id("38242376781523689472")
        address_create_refund_req.set_refund_amount("9.9")
        address_create_refund_req.set_refund_reason("test refund")
        address_create_refund_req.set_receiver_id(6790011)
        print(self.init_gate_pay_client().create_address_refund(address_create_refund_req).get_data().__str__())


        # todo test 订单状态未终态
    def test_create_address_refund_convert(self):
        address_create_refund_req=AddressCreateRefundConvertReq()
        address_create_refund_req.set_prepay_id("35297827964846503")
        address_create_refund_req.set_refund_request_id("38242376781533689472")
        address_create_refund_req.set_refund_order_amount("9.9")
        address_create_refund_req.set_refund_order_currency("ETH")
        address_create_refund_req.set_refund_pay_currency("ETH")
        address_create_refund_req.set_refund_pay_amount("9.9")
        address_create_refund_req.set_refund_reason("test refund")
        address_create_refund_req.set_receiver_id(6790011)
        print(self.init_gate_pay_client().create_address_refund_convert(address_create_refund_req).get_data().__str__())


    def test_address_transaction_detail(self):
        transaction_detail=TransactionDetailReq()
        transaction_detail.set_prepay_id("35297827964846503")
        print(self.init_gate_pay_client().address_transaction_detail(transaction_detail).get_data().__str__())


    def test_query_bill_orders(self):
        query_orders_req=QueryOrdersReq()
        query_orders_req.set_start_time(1705297715000)
        query_orders_req.set_end_time(1705297825000)
        query_orders_req.set_page(1)
        query_orders_req.set_count(10)
        query_orders_req.set_currency("USDT")
        query_orders_req.set_order_type("1")
        query_orders_req.set_order_id_no("1689667326891627")
        print(self.init_gate_pay_client().query_bill_orders(query_orders_req).get_data().__str__())

    # todo fail
    def test_save_channel_manage(self):
        custom_field=CustomField()
        custom_field.set_code("87")
        custom_field.set_name("sam")
        custom_field.set_value("val")

        merchant_channel= MerchantChannel()
        merchant_channel.set_channel_id("44")
        merchant_channel.set_custom_fields([custom_field])
        merchant_channel.set_desc("test")
        merchant_channel.set_channel_type("0")
        merchant_channel.set_chain("Lorem sed elit id aliqua")
        merchant_channel.set_address("辽宁省 安乡县 芜湖县 幸路681号 93单元")
        merchant_channel.set_create_time(1723004848459)
        merchant_channel.set_update_time(int(datetime.now().timestamp()*1000))

        save_req=SaveReq()
        save_req.set_merchant_channel_list([merchant_channel])
        print(self.init_gate_pay_client().save_channel_manage(save_req).get_data().__str__())

    def test_list_channel_manage(self):
        list_req = ListReq()
        list_req.set_channel_id("100")
        list_req.set_page(1)
        list_req.set_count(10)
        print(self.init_gate_pay_client().list_channel_manage(list_req).get_data().__str__())


    # todo fail
    def test_update_channel_manage(self):
        custom_field = CustomField()
        custom_field.set_code("87")
        custom_field.set_name("sam")
        custom_field.set_value("test")

        merchant_channel= MerchantChannel()
        merchant_channel.set_channel_id("44")
        merchant_channel.set_custom_fields([custom_field])

        update_req =UpdateReq()
        update_req.set_merchant_channel_list([merchant_channel])
        print(self.init_gate_pay_client().update_channel_manage(update_req).get_data().__str__())

    def test_delete_channel_manage(self):
        delete_req = DeleteReq()
        delete_req.set_channel_id("100")
        print(self.init_gate_pay_client().delete_channel_manage(delete_req).get_data().__str__())

    def test_create_checkout_order(self):
        env_req = EnvReq()
        env_req.set_terminal_type("APP")

        goods_req=GoodsReq()
        goods_req.set_goods_type("02")
        goods_req.set_goods_name("test")
        goods_req.set_goods_detail("testDetail")


        create_order_req=CheckOutCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(24))
        create_order_req.set_currency("USDT")
        create_order_req.set_order_amount("10")
        create_order_req.set_pay_currency("USDT")
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        create_order_req.set_merchant_user_id(10002)

        create_order_req.set_return_url("https://lotkeys.com/tr/gate-payment-response")
        create_order_req.set_cancel_url("https://lotkeys.com/tr/gate-payment-response")
        create_order_req.set_chain("ETH")
        create_order_req.set_full_curr_type("USDT_ETH")
        create_order_req.set_channel_id("123")
        print("merchantOrderNo:" + create_order_req.get_merchant_trade_no())
        print(self.init_gate_pay_client().create_checkout_order(create_order_req).get_data().__str__())

    # todo  状态未到达状态
    def test_create_checkout_refund(self):
        create_refund_req=CheckOutCreateRefundReq()
        create_refund_req.set_prepay_id("35301792219791413")
        create_refund_req.set_refund_request_id("1860036668897340")
        create_refund_req.set_refund_order_amount("10.0")
        create_refund_req.set_refund_pay_amount("10.0")
        create_refund_req.set_refund_pay_currency("USDT")
        create_refund_req.set_refund_order_currency("USDT")
        create_refund_req.set_refund_reason("test refund")
        create_refund_req.set_receiver_id(6790011)
        print(self.init_gate_pay_client().create_checkout_refund(create_refund_req).get_data().__str__())

    def test_query_convert_currency(self):
        query_currency_req=QueryCurrencyReq()
        query_currency_req.set_side("sell")
        print(self.init_gate_pay_client().query_convert_currency(query_currency_req).get_data().__str__())

    def test_query_convert_pair(self):
        query_pair_req=QueryPairReq()
        query_pair_req.set_currency("LLT")
        query_pair_req.set_side("buy")
        print(self.init_gate_pay_client().query_convert_pair(query_pair_req).get_data().__str__())

    def test_preview_convert(self):
        preview_req=PreviewReq()
        preview_req.set_buy_amount("0.01")
        preview_req.set_buy_currency("GT")
        preview_req.set_sell_currency("USDT")
        print(self.init_gate_pay_client().preview_convert(preview_req).get_data().__str__())

    # todo createOrder fail
    def test_create_convert_order(self):
        create_order_req=ConvertCreateOrderReq()
        create_order_req.set_quote_id("PAY-"+RandomUtils.generate_nonce(8))
        create_order_req.set_client_req_id(RandomUtils.generate_nonce(11))
        create_order_req.set_price("0.04268034")
        create_order_req.set_sell_currency("USDT")
        create_order_req.set_sell_amount("0.23429989")
        create_order_req.set_buy_currency("GT")
        create_order_req.set_buy_amount("0.01")

        print("clientReqId:" + create_order_req.get_client_req_id())
        print(self.init_gate_pay_client().create_convert_order(create_order_req).get_data().__str__())

    def test_query_convert_order(self):
        convert_query_order_req =ConvertQueryOrderReq()
        convert_query_order_req.set_order_id("326850433152987136")
        print(self.init_gate_pay_client().query_convert_order(convert_query_order_req).get_data().__str__())


    def test_create_gift(self):
        create_req =CreateReq()
        create_req.set_title("anlitest20250210001")
        create_req.set_template_id("293409440220057600")
        create_req.set_currency("USDT")
        create_req.set_amount("0.99")
        print(self.init_gate_pay_client().create_gift(create_req).get_data().__str__())

    def test_list_gift_temp(self):
        list_temp_req =ListTempReq()
        print(self.init_gate_pay_client().list_gift_temp(list_temp_req).get_data().__str__())

    # todo 缺乏礼品卡号
    def test_query_gift(self):
        query_req =QueryReq()
        print(self.init_gate_pay_client().query_gift(query_req).get_data().__str__())


    def test_create_qr_code_order(self):
        env_req = EnvReq()
        env_req.set_terminal_type("APP")

        # 创建商品请求对象
        goods_req = GoodsReq()
        goods_req.set_goods_name("NF2T")
        goods_req.set_goods_detail("nef-book")

        # 创建地址订单请求对象
        create_order_req = QrCodeCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(24))
        create_order_req.set_currency("USDT")
        create_order_req.set_order_amount("9.9")
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        create_order_req.set_return_url("https://www.gate.com/")
        print("merchantOrderNo:"+create_order_req.get_merchant_trade_no())
        create_order_resp=self.init_gate_pay_client().create_qr_code_order(create_order_req)
        print(create_order_resp.get_data().__str__())

    def test_create_web_order(self):
        env_req = EnvReq()
        env_req.set_terminal_type("MINIAPP")

        # 创建商品请求对象
        goods_req = GoodsReq()
        goods_req.set_goods_name("25000000元宝")
        goods_req.set_goods_detail("充值")

        # 创建地址订单请求对象
        create_order_req = PaymentCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(14))
        create_order_req.set_currency("USDT")
        create_order_req.set_order_amount("9.9")
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        create_order_req.set_channel_id("123")
        create_order_req.set_extend_info("1_elbt01_16882172126048")

        print("merchantOrderNo:" + create_order_req.get_merchant_trade_no())
        create_order_resp = self.init_gate_pay_client().create_web_order(create_order_req)
        print(create_order_resp.get_data().__str__())

    def test_query_web_order(self):
        web_query_order_req=WebQueryOrderReq()
        web_query_order_req.set_prepay_id("35297827964846503")
        web_query_order_req.set_merchant_trade_no("43wGhuujHKwAoLXRd7mMjihU")
        print(self.init_gate_pay_client().query_web_order(web_query_order_req).get_data().__str__())

    # todo 关闭订单失败
    def test_close_web_order(self):
        close_order_req=CloseOrderReq()
        close_order_req.set_prepay_id("35297827964846503")
        close_order_req.set_merchant_trade_no("43wGhuujHKwAoLXRd7mMjihU")
        print(self.init_gate_pay_client().close_web_order(close_order_req).get_data().__str__())

    def test_create_web_refund(self):
        refund_order_req=PaymentCreateRefundReq()
        refund_order_req.set_prepay_id("35297827964846503")
        refund_order_req.set_refund_amount("9.9")
        print(self.init_gate_pay_client().create_web_refund(refund_order_req).get_data().__str__())

    def test_create_batch_transfer(self):
        batch_order=BatchOrder()
        batch_order.set_user_id(6790011)
        batch_order.set_amount("2")

        create_batch_transfer_req=CreateBatchTransferReq()
        create_batch_transfer_req.set_batch_id(RandomUtils.generate_nonce(14))
        create_batch_transfer_req.set_merchant_batch_no(RandomUtils.generate_nonce(24))
        create_batch_transfer_req.set_biz_scene("DIRECT_TRANSFER")
        create_batch_transfer_req.set_merchant_id("10002")
        create_batch_transfer_req.set_client_id("mZ96D37oKk-HrWJc")
        create_batch_transfer_req.set_currency("USDT")
        create_batch_transfer_req.set_name("Larry")
        create_batch_transfer_req.set_description("bonus")
        create_batch_transfer_req.set_batch_order_list([batch_order])
        print("merchantBatchNo:"+create_batch_transfer_req.get_merchant_batch_no())
        print(self.init_gate_pay_client().create_batch_transfer(create_batch_transfer_req).get_data().__str__())

    def test_query_batch_transfer(self):
        query_batch_transfer_req=QueryBatchTransferReq()
        query_batch_transfer_req.set_batch_id("UpnEUu3NmWZX8L")
        query_batch_transfer_req.set_merchant_batch_no("E2CUCbspERZPjl3yQLqCMSFv")
        query_batch_transfer_req.set_detail_status("ALL")
        print(self.init_gate_pay_client().query_batch_transfer(query_batch_transfer_req).get_data().__str__())

    def test_query_balance(self):
        query_balance_req=QueryBalanceReq()
        balance=self.init_gate_pay_client().query_balance(query_balance_req)
        print(balance.__str__())

    def test_create_withdraw_order(self):
        with_draw=Withdraw()
        with_draw.set_currency("USDT")
        with_draw.set_amount("0.001")
        with_draw.set_chain("ETH")
        with_draw.set_address("0x1234567890abcdef")
        with_draw.set_memo("Payment for services-1")
        with_draw.set_merchant_withdraw_id(RandomUtils.generate_nonce(19))
        with_draw.set_fee_type(1)

        with_draw_create_order_req=WithdrawCreateOrderReq()
        with_draw_create_order_req.set_withdraws([with_draw])
        with_draw_create_order_req.set_batch_id(RandomUtils.generate_nonce(24))
        print("batchId:"+with_draw_create_order_req.get_batch_id())
        print(self.init_gate_pay_client().create_withdraw_order(with_draw_create_order_req).get_data().__str__())

    def test_query_withdraw_order(self):
        withdraw_query_order_req=WithdrawQueryOrderReq()
        withdraw_query_order_req.set_batch_id("237394559478075555")
        withdraw_query_order_req.set_detail_status("ALL")
        print(self.init_gate_pay_client().query_withdraw_order(withdraw_query_order_req).get_data().__str__())

    def test_query_withdraw_chains(self):
        query_chains_req=QueryChainsReq()
        query_chains_req.set_currency("GT")
        print(self.init_gate_pay_client().query_withdraw_chains(query_chains_req).get_data().__str__())

    def test_query_withdraw_balance(self):
        query_chains_req=WithdrawQueryBalanceReq()
        query_chains_req.set_currency("GT")
        print(self.init_gate_pay_client().query_withdraw_balance(query_chains_req).get_data().__str__())

    # 该接口不存在
    def test_query_withdraw_status(self):
        query_status_req=QueryStatusReq()
        query_status_req.set_currency("USDT")
        print(self.init_gate_pay_client().query_withdraw_status(query_status_req).get_data().__str__())

    def test_query_web_order_v3(self):
        web_query_order_req=WebQueryOrderReqV3()
        web_query_order_req.set_prepay_id("35297827964846503")
        web_query_order_req.set_merchant_trade_no("43wGhuujHKwAoLXRd7mMjihU")
        print(self.init_gate_pay_client_v3().query_web_order_v3(web_query_order_req).get_data().__str__())

    def test_query_web_refund_support_chains_v3(self):
        query_refund_support_chains_req=QueryRefundSupportChainsReqV3()
        query_refund_support_chains_req.set_currency("USDT")
        print(self.init_gate_pay_client_v3().query_web_refund_support_chains_v3(query_refund_support_chains_req).get_data().__str__())

    def test_query_web_refund_v3(self):
        query_refund_req=PaymentQueryRefundReqV3()
        query_refund_req.set_refund_request_id("35297827964846503")
        print(self.init_gate_pay_client_v3().query_web_refund_v3(query_refund_req).get_data().__str__())

    def test_web_create_refund_v3(self):
        create_order_req = PaymentCreateRefundReqV3()
        create_order_req.set_merchant_id(RandomUtils.generate_nonce(14))
        create_order_req.set_client_id("USDT")
        create_order_req.set_refund_request_id("9.9")
        create_order_req.set_prepay_id("123")
        create_order_req.set_refund_amount("1_elbt01_16882172126048")
        create_order_req.set_refund_reason("1_elbt01_16882172126048")
        create_order_req.set_refund_gate_id("1_elbt01_16882172126048")
        create_order_req.set_refund_to_gate_uid("1_elbt01_16882172126048")
        create_order_req.set_refund_style("1_elbt01_16882172126048")
        create_order_req.set_refund_pay_channel("1_elbt01_16882172126048")
        create_order_req.set_refund_address("1_elbt01_16882172126048")
        create_order_req.set_refund_chain("1_elbt01_16882172126048")
        create_order_req.set_refund_amount_type_full("1_elbt01_16882172126048")

        print("merchantOrderNo:" + create_order_req.get_merchant_trade_no())
        create_order_resp = self.init_gate_pay_client().create_web_refund_v3(create_order_req)
        print(create_order_resp.get_data().__str__())


if __name__ == '__main__':
    unittest.main()
