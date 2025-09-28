# -*- coding: gbk -*-
import time
import unittest
from datetime import datetime
from symbol import return_stmt
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

from src.gatepay.api.model.req.payment.query_refund_req import QueryRefundReq as PaymentQueryRefundReq

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
import time
import jsonpath
#allenby
from src.gatepay.api.model.req.manage.save_req import SaveReq

#no sdk api
from src.gatepay.api.model.req.currencies_req import CurrenciesReq

class GatePayClientTest(unittest.TestCase):

    def init_gate_pay_client(self):
        gate_pay_config = GatePayConfig(
            "",
            30,
            "",
            Credential("", "")
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

    def test_get_address_supported_convert_currencies(self,currency:str="USDT"):
        supported_convert_currencies_req = SupportedConvertCurrenciesReq()
        supported_convert_currencies_req.set_currency(currency)
        res=self.init_gate_pay_client().get_address_supported_convert_currencies(supported_convert_currencies_req).__dict__
        print("获取地址支付支持闪兑的币种",res)
        return res

    def test_create_address_order(self,currency:str="USDT",amount:str="0.001",user_id:int=2124505156,
                                  chain:str="TRX",full_curr_type:str="USDT_TRX"):
        testdata={"merchantTradeNo":"9965839856","currency":"USDT","orderAmount":"10","env":
            {"terminalType":"MINIAPP"},"goods":{"goodsName":"自动化订单","goodsDetail":"自动化订单：地址支付-直付"},
                  "orderExpireTime":1758712237898,"returnUrl":"www.baidu.com","cancelUrl":"www.taobao.com",
                  "merchantUserId":2124505156,"chain":"TRX","fullCurrType":"USDT_TRX"}

        env_req = EnvReq()
        env_req.set_terminal_type("MINIAPP")

        # 创建商品请求对象
        goods_req = GoodsReq()
        goods_req.set_goods_name("test")
        goods_req.set_goods_detail("testDetail")
        # 创建地址订单请求对象
        create_order_req = AddressCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(10))#原24
        create_order_req.set_currency(currency)
        create_order_req.set_order_amount(amount)
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        time_ms=int(time.time() * 1000) + 8 * 60 * 60 * 1000
        create_order_req.set_order_expire_time(time_ms)#原int(time.time() * 1000) + 3 * 60 * 60 * 1000
        create_order_req.set_return_url("https://www.gate.com/")
        create_order_req.set_cancel_url("https://www.gate.com/")
        create_order_req.set_merchant_user_id(user_id)
        create_order_req.set_chain(chain)
        create_order_req.set_full_curr_type(full_curr_type)
        # create_order_req.set_channel_id("")
        print("merchantOrderNo:"+create_order_req.get_merchant_trade_no())
        create_order_resp=self.init_gate_pay_client().create_address_order(create_order_req).__dict__
        print(create_order_resp)
        return create_order_resp,create_order_req.get_merchant_trade_no()

    def test_query_address_order(self,prepay_id:str="35425315479093450",merchant_trade_no:str="43wGhuujHKwAoLXRd7mMjihU"):
        query_order_req=AddressQueryOrderReq()
        query_order_req.set_prepay_id(prepay_id)
        query_order_req.set_merchant_trade_no(merchant_trade_no)#商户系统交易号。不输入也可以
        # print(self.init_gate_pay_client().query_address_order(query_order_req).get_data().__str__())
        res=self.init_gate_pay_client().query_address_order(query_order_req).__dict__
        print("查询地址支付订单列表-返回值:",res)
        return res

    def test_create_address_refund(self,prepay_id:str="35432002743304519",refund_amount:str="0.001",
                                   receiver_id:int=2124505156):
        address_create_refund_req=AddressCreateRefundReq()
        address_create_refund_req.set_prepay_id(prepay_id)#商家订单号
        address_create_refund_req.set_refund_request_id(RandomUtils.generate_nonce(9))#退款订单号，可以随机 38242376781523689472
        address_create_refund_req.set_refund_amount(refund_amount)
        address_create_refund_req.set_refund_reason("test refund")
        address_create_refund_req.set_receiver_id(receiver_id)
        # print(self.init_gate_pay_client().create_address_refund(address_create_refund_req).get_data().__str__())
        res=self.init_gate_pay_client().create_address_refund(address_create_refund_req).__dict__
        return res

        # todo test 订单状态未终态
    def test_create_address_refund_convert(self,prepay_id:str="35425837317750961",amount:str="1"):
        address_create_refund_req=AddressCreateRefundConvertReq()
        address_create_refund_req.set_refund_request_id(RandomUtils.generate_nonce(9))#随机数 38242376781533689472
        address_create_refund_req.set_prepay_id(prepay_id)
        address_create_refund_req.set_refund_order_currency("USDT")#ETH
        address_create_refund_req.set_refund_order_amount(amount)
        address_create_refund_req.set_refund_pay_currency("USDT")#ETH
        address_create_refund_req.set_refund_pay_amount(amount)
        address_create_refund_req.set_refund_reason("test refund")
        address_create_refund_req.set_receiver_id(2124505156)
        print(self.init_gate_pay_client().create_address_refund_convert(address_create_refund_req).get_data().__str__())
        res=self.init_gate_pay_client().create_address_refund_convert(address_create_refund_req).__dict__
        print("地址支付闪兑退款-返回值",res)
        return res

    def test_address_transaction_detail(self,prepay_id:str="35297827964846503"):
        transaction_detail=TransactionDetailReq()
        transaction_detail.set_prepay_id(prepay_id)
        res=self.init_gate_pay_client().address_transaction_detail(transaction_detail).__dict__
        print("查询链上交易详情：",res)
        return res

    def test_query_bill_orders(self,order_id_no:str="yLEKbCFFJ",currency:str="USDT"):
        query_orders_req=QueryOrdersReq()
        time_start=int(time.time() * 1000)-30*24 * 60 * 60 * 1000
        time_end = int(time.time() * 1000) + 10 * 60 * 60 * 1000
        print(time_start,time_end)
        query_orders_req.set_start_time(time_start)#1705297715000
        query_orders_req.set_end_time(time_end)#1758737591957
        query_orders_req.set_page(1)
        query_orders_req.set_count(10)
        query_orders_req.set_currency(currency)
        query_orders_req.set_order_type("2")
        query_orders_req.set_order_id_no(order_id_no)
        # print(self.init_gate_pay_client().query_bill_orders(query_orders_req).get_data().__str__())
        res=self.init_gate_pay_client().query_bill_orders(query_orders_req).__dict__
        return res

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

    def test_list_channel_manage(self,channel_id:str='100'):
        list_req = ListReq()
        list_req.set_channel_id(channel_id)
        list_req.set_page(1)
        list_req.set_count(10)
        res=self.init_gate_pay_client().list_channel_manage(list_req).__dict__
        print("客户渠道列表",res)
        return res

    # todo fail
    def test_update_channel_manage(self,channel_id:str="44"):
        custom_field = CustomField()
        custom_field.set_code("87")
        custom_field.set_name("sam")
        custom_field.set_value("test")

        merchant_channel= MerchantChannel()
        merchant_channel.set_channel_id(channel_id)
        merchant_channel.set_custom_fields([custom_field])

        update_req =UpdateReq()
        update_req.set_merchant_channel_list([merchant_channel])
        res=self.init_gate_pay_client().update_channel_manage(update_req).__dict__
        print("更新客户渠道-返回结果：",res)
        return res

    def test_delete_channel_manage(self,channel_id:str="channel_id"):
        delete_req = DeleteReq()
        delete_req.set_channel_id(channel_id)
        res=self.init_gate_pay_client().delete_channel_manage(delete_req).__dict__
        print("删除客户渠道返回：",res)
        return res
    def test_create_checkout_order(self,currency:str="USDT",amount:str="0.0001",user_id:int=2124505156
                                   ,chain:str="BSC",full_curr_type:str="USDT_BSC"):
        test_data={"merchantTradeNo":"M1465894218","currency":"USDT","orderAmount":"0.0001",
                   "payCurrency":"USDT","env":{"terminalType":"1234"},"goods":{"goodsName":
                   "autocheckout loragoodsName","goodsDetail":"autocheckout loragoodsDetail"},
                   "returnUrl":"https://www.baidu.com","cancelUrl":"www.baidu.com","merchantUserId":2124505156,
                   "chain":"BSC","fullCurrType":"USDT_BSC"}
        env_req = EnvReq()
        env_req.set_terminal_type("APP")

        goods_req=GoodsReq()
        goods_req.set_goods_type("02")
        goods_req.set_goods_name("test")
        goods_req.set_goods_detail("testDetail")
        create_order_req=CheckOutCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(24))
        create_order_req.set_currency(currency)
        create_order_req.set_order_amount(amount)
        create_order_req.set_pay_currency(currency)
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        create_order_req.set_merchant_user_id(user_id)

        create_order_req.set_return_url("https://lotkeys.com/tr/gate-payment-response")
        create_order_req.set_cancel_url("https://lotkeys.com/tr/gate-payment-response")
        create_order_req.set_chain(chain)
        create_order_req.set_full_curr_type(full_curr_type)
        # create_order_req.set_channel_id("123")#不用这个号
        print("merchantOrderNo:" + create_order_req.get_merchant_trade_no())
        # print(self.init_gate_pay_client().create_checkout_order(create_order_req).get_data().__str__())
        res=self.init_gate_pay_client().create_checkout_order(create_order_req).__dict__
        print(res)
        return res

    def test_create_checkout_refund(self,prepay_id:str="35425551702294728",receiver_id:int=2124505156,amount:str="0.0001"):
        create_refund_req=CheckOutCreateRefundReq()
        create_refund_req.set_prepay_id(prepay_id)#GatePay订单号 :35419639679942788
        create_refund_req.set_refund_request_id(RandomUtils.generate_nonce(9))#商户退款订单号，1860036668897340随机数
        create_refund_req.set_refund_order_amount(amount)
        create_refund_req.set_refund_pay_amount(amount)
        create_refund_req.set_refund_pay_currency("USDT")
        create_refund_req.set_refund_order_currency("USDT")
        create_refund_req.set_refund_reason("test refund")
        create_refund_req.set_receiver_id(receiver_id)
        # print(self.init_gate_pay_client().create_checkout_refund(create_refund_req).get_data().__str__())
        res=self.init_gate_pay_client().create_checkout_refund(create_refund_req).__dict__
        print(res)
        return res
    def test_query_convert_currency(self):
        query_currency_req=QueryCurrencyReq()
        query_currency_req.set_side("sell")
        print(self.init_gate_pay_client().query_convert_currency(query_currency_req).get_data().__str__())

    def test_query_convert_pair(self):
        query_pair_req=QueryPairReq()
        query_pair_req.set_currency("LLT")
        query_pair_req.set_side("buy")
        print(self.init_gate_pay_client().query_convert_pair(query_pair_req).get_data().__str__())

    def test_preview_convert(self,amount:str="1"):
        preview_req=PreviewReq()
        preview_req.set_buy_amount(amount)
        preview_req.set_buy_currency("GT")
        preview_req.set_sell_currency("USDT")
        print(self.init_gate_pay_client().preview_convert(preview_req).get_data().__str__())
        res=self.init_gate_pay_client().preview_convert(preview_req).__dict__
        print("预览报价返回值：",res)
        return res

    def test_create_convert_order(self):
        """
        闪兑下单，不同币种之间快速闪兑
        :return:
        """
        create_order_req=ConvertCreateOrderReq()
        create_order_req.set_quote_id("PAY-"+RandomUtils.generate_nonce(8))
        create_order_req.set_client_req_id(RandomUtils.generate_nonce(11))
        create_order_req.set_price("0.04268034")
        create_order_req.set_sell_currency("USDT")#卖家币种
        create_order_req.set_sell_amount("0.23429989")#原始0.23429989
        create_order_req.set_buy_currency("GT")#买家币种
        create_order_req.set_buy_amount("0.01")

        print("clientReqId:" + create_order_req.get_client_req_id())
        res= self.init_gate_pay_client().create_convert_order(create_order_req).__dict__
        print("闪兑下单返回数据：",res)
        return res

    def test_create_convert_order_new(self,quote_id:str,amount:str="1"):
        """
        闪兑下单，不同币种之间快速闪兑
        :return:
        """
        create_order_req = ConvertCreateOrderReq()
        # create_order_req.set_quote_id("PAY-" + RandomUtils.generate_nonce(8))
        create_order_req.set_quote_id(quote_id)
        create_order_req.set_client_req_id(RandomUtils.generate_nonce(10))
        # create_order_req.set_price("0.04268034")
        create_order_req.set_sell_currency("USDT")  # 卖家币种
        create_order_req.set_sell_amount(amount)  # 原始0.23429989
        create_order_req.set_buy_currency("GT")  # 买家币种
        create_order_req.set_buy_amount(amount)

        print("clientReqId:",create_order_req.get_client_req_id())
        print("quote_id:",create_order_req.get_quote_id())
        # print(self.init_gate_pay_client().create_convert_order(create_order_req).get_data().__str__())
        res = self.init_gate_pay_client().create_convert_order(create_order_req).__dict__
        print("闪兑下单返回数据：", res)
        return res

    def test_create_convert_preview(self):
        """
        闪兑下单前需要查询对应的预览报价和quoteId
        :return:
        """
        # 通过sdk接口v1/pay/convert/preview，预览报价：
        # 请求         { "buyCurrency": "GT", "buyAmount": "", "sellCurrency": "USDT","sellAmount": "0.1"        }
        # 返回：
        convert_preview = {"clientReqId": "8320289173", "sellCurrency": "USDT", "buyCurrency": "GT", "buyAmount": "1",
                           "sellAmount": "1", "quoteId": "PAY-7d6fef9d"}
        # 实际请求：
        # {"clientReqId": "3845654414", "sellCurrency": "USDT", "buyCurrency": "GT", "buyAmount": "0.0060247",
        # "sellAmount": "0.1", "quoteId": "PAY-820da3ec"}

        create_order_req = ConvertCreateOrderReq()
        # quote_id="PAY-"+RandomUtils.generate_nonce(8)
        create_order_req.set_quote_id(convert_preview['quoteId'])
        # create_order_req.set_quote_id("PAY-bb1d7082")
        # create_order_req.set_client_req_id(RandomUtils.generate_nonce(10))#5813764260
        create_order_req.set_client_req_id(convert_preview['clientReqId'])  # 5813764260
        # create_order_req.set_price("")
        create_order_req.set_sell_currency("USDT")  # 卖家币种
        create_order_req.set_sell_amount("1")  # 原始0.23429989
        create_order_req.set_buy_currency("GT")  # 买家币种
        create_order_req.set_buy_amount("1")

        print("clientReqId:" + create_order_req.get_client_req_id())
        # print(self.init_gate_pay_client().create_convert_order(create_order_req).get_data().__str__())
        res = self.init_gate_pay_client().create_convert_order(create_order_req).__dict__
        print("闪兑下单返回数据：", res)
        return res

    def test_query_convert_order(self,order_id:str="35424772165861688"):
        convert_query_order_req =ConvertQueryOrderReq()
        convert_query_order_req.set_order_id(order_id)
        # print(self.init_gate_pay_client().query_convert_order(convert_query_order_req).get_data().__str__())
        res=self.init_gate_pay_client().query_convert_order(convert_query_order_req).__dict__
        print("order_id:",order_id)
        print("查询闪兑订单：",res)
        return res


    def test_create_gift(self,template_id:str="293409440220057600",currency:str="USDT",amount:str="0.99"):
        create_req =CreateReq()
        create_req.set_title("anlitest20250210001")
        create_req.set_template_id(template_id)
        create_req.set_currency(currency)
        create_req.set_amount(amount)
        # print(self.init_gate_pay_client().create_gift(create_req).get_data().__str__())
        get_data=self.init_gate_pay_client().create_gift(create_req).get_data()
        return get_data

    def test_list_gift_temp(self):
        """
        列出礼品卡模版，要礼品卡模版id即可
        :return:
        """
        list_temp_req =ListTempReq()
        print(self.init_gate_pay_client().list_gift_temp(list_temp_req).get_data().__str__())
        res=self.init_gate_pay_client().list_gift_temp(list_temp_req)
        return res

    def test_query_gift(self,card_numbe:str=""):
        query_req =QueryReq()
        query_req.set_card_number(card_numbe)
        query_req.set_key("")
        # print(self.init_gate_pay_client().query_gift(query_req).get_data().__str__())
        res=self.init_gate_pay_client().query_gift(query_req).__dict__
        print("查看礼品卡列表返回值：",res)
        return res
    def test_create_qr_code_order(self,currency:str="USDT",amount:str="0.1"):
        env_req = EnvReq()
        env_req.set_terminal_type("APP")

        # 创建商品请求对象
        goods_req = GoodsReq()
        goods_req.set_goods_name("NF2T")
        goods_req.set_goods_detail("nef-book")

        # 创建地址订单请求对象
        create_order_req = QrCodeCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(24))
        create_order_req.set_currency(currency)
        create_order_req.set_order_amount(amount)
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        create_order_req.set_return_url("https://www.gate.com/")
        merchantOrderNo=create_order_req.get_merchant_trade_no()
        print("merchantOrderNo:",merchantOrderNo)
        create_order_resp=self.init_gate_pay_client().create_qr_code_order(create_order_req).__dict__
        print("create_order_resp:",create_order_resp)
        return create_order_resp,merchantOrderNo

    def test_create_web_order(self,currency:str="USDT",order_amount:str="0.001"):
        env_req = EnvReq()
        env_req.set_terminal_type("MINIAPP")

        # 创建商品请求对象
        goods_req = GoodsReq()
        goods_req.set_goods_name("25000000元宝")
        goods_req.set_goods_detail("充值")

        # 创建地址订单请求对象
        create_order_req = PaymentCreateOrderReq()
        create_order_req.set_merchant_trade_no(RandomUtils.generate_nonce(14))
        create_order_req.set_currency(currency)
        create_order_req.set_order_amount(order_amount)
        create_order_req.set_env(env_req)
        create_order_req.set_goods(goods_req)
        # create_order_req.set_channel_id("123")
        create_order_req.set_extend_info("1_elbt01_16882172126048")
        merchantOrderNo=create_order_req.get_merchant_trade_no()
        print("merchantOrderNo:",merchantOrderNo)
        create_order_resp = self.init_gate_pay_client().create_web_order(create_order_req).__dict__
        print("create_order_resp",create_order_resp)
        return create_order_resp,merchantOrderNo

    def test_query_web_order(self,prepay_id:str="35297827964846503",merchant_trade_no:str="43wGhuujHKwAoLXRd7mMjihU"):
        web_query_order_req=WebQueryOrderReq()
        web_query_order_req.set_prepay_id(prepay_id)
        web_query_order_req.set_merchant_trade_no(merchant_trade_no)
        res=self.init_gate_pay_client().query_web_order(web_query_order_req).__dict__
        print("查询订单:",res)
        return res


    # todo 关闭订单失败
    def test_close_web_order(self,prepay_id:str="35297827964846503",merchant_trade_no:str="43wGhuujHKwAoLXRd7mMjihU"):
        close_order_req=CloseOrderReq()
        close_order_req.set_prepay_id(prepay_id)
        close_order_req.set_merchant_trade_no(merchant_trade_no)
        res=self.init_gate_pay_client().close_web_order(close_order_req).__dict__
        print("关闭订单返回结果",res)
        return res

    def test_create_web_refund(self,prepay_id:str="35432097232453869",amount:str="1"):
        refund_order_req=PaymentCreateRefundReq()
        refund_order_req.set_prepay_id(prepay_id)
        refund_order_req.set_refund_amount(amount)
        refund_order_req.set_refund_request_id(RandomUtils.generate_nonce(11))
        refund_request_id=refund_order_req.get_refund_request_id()#"GzpNbjuLnH4"
        res=self.init_gate_pay_client().create_web_refund(refund_order_req).__dict__
        print("创建退款订单",res)
        return res,refund_request_id

    def test_create_batch_transfer(self,user_id:str="6790011",amount:str="1"):
        batch_order=BatchOrder()
        batch_order.set_user_id(user_id)
        batch_order.set_amount(amount)

        create_batch_transfer_req=CreateBatchTransferReq()
        create_batch_transfer_req.set_batch_id(RandomUtils.generate_nonce(14))
        create_batch_transfer_req.set_merchant_batch_no(RandomUtils.generate_nonce(24))
        create_batch_transfer_req.set_biz_scene("DIRECT_TRANSFER")
        create_batch_transfer_req.set_merchant_id("")#原
        create_batch_transfer_req.set_client_id("aaaa")#
        create_batch_transfer_req.set_name("")
        create_batch_transfer_req.set_description("bonus")
        create_batch_transfer_req.set_batch_order_list([batch_order])
        print("merchantBatchNo:"+create_batch_transfer_req.get_merchant_batch_no())
        print(self.init_gate_pay_client().create_batch_transfer(create_batch_transfer_req).get_data().__str__())
        return create_batch_transfer_req
    def test_query_batch_transfer(self,batch_id,merchant_batch_no):
        """
        批量转账查询
        :param batch_id: 批次id
        :param merchant_batch_no: 商户批次单号
        :return:
        """

        print("批量转账查询-开始",batch_id,merchant_batch_no)
        query_batch_transfer_req=QueryBatchTransferReq()
        query_batch_transfer_req.set_batch_id(batch_id)#
        query_batch_transfer_req.set_merchant_batch_no(merchant_batch_no)#
        #query_batch_transfer_req.set_detail_status("ALL")
        print("批量转账查询-结束",self.init_gate_pay_client().query_batch_transfer(query_batch_transfer_req).get_data().__str__())

    def test_query_balance(self):
        """
        查询余额，个人账户余额。特别说明，需要预发环境才可以查询
        :return:
        """
        query_balance_req=QueryBalanceReq()
        balance=self.init_gate_pay_client().query_balance(query_balance_req)
        print(balance.__str__())
        return balance

    def test_create_withdraw_order(self,currency:str="USDT"):
        with_draw=Withdraw()
        with_draw.set_currency(currency)
        with_draw.set_amount("0.001")
        with_draw.set_chain("TRC")
        with_draw.set_address("")#静态收款码-名称：
        # with_draw.set_memo("Payment for services-1")
        with_draw.set_merchant_withdraw_id(RandomUtils.generate_nonce(19))
        with_draw.set_fee_type(1)

        with_draw_create_order_req=WithdrawCreateOrderReq()
        with_draw_create_order_req.set_withdraws([with_draw])
        with_draw_create_order_req.set_batch_id(RandomUtils.generate_nonce(24))
        batchId=with_draw_create_order_req.get_batch_id()
        print("batchId:"+batchId)
        print("钱包提现下发订单-返回结果",self.init_gate_pay_client().create_withdraw_order(with_draw_create_order_req).__dict__)
        return batchId

    def test_query_withdraw_order(self,batch_id="7OMriYhPEUyHfdUVbkYCM3kp"):
        withdraw_query_order_req=WithdrawQueryOrderReq()
        withdraw_query_order_req.set_batch_id(batch_id)
        withdraw_query_order_req.set_detail_status("ALL")
        res=self.init_gate_pay_client().query_withdraw_order(withdraw_query_order_req).__dict__
        print("查询提现订单：",res)
        return res

    def test_query_withdraw_chains(self,currency:str="GT"):
        query_chains_req=QueryChainsReq()
        query_chains_req.set_currency(currency)
        #测试环境查不到
        # print(self.init_gate_pay_client().query_withdraw_chains(query_chains_req).get_data().__str__())
        res=self.init_gate_pay_client().query_withdraw_chains(query_chains_req).__dict__
        print("查询币种支持的链（/v1/pay/wallet/currency_chains）-生产环境:",res)


    def test_query_withdraw_balance(self,currency:str="USDT"):
        """
        :param currency: 币种
        :return:
        """
        query_chains_req=WithdrawQueryBalanceReq()
        query_chains_req.set_currency(currency)
        res=self.init_gate_pay_client().query_withdraw_balance(query_chains_req).get_data()
        print("查询提现支持币种：",res)
        return res
    # 该接口不存在
    def test_query_withdraw_status(self,currency:str="USDT"):
        print("=====test_query_withdraw_status=======")
        query_status_req=QueryStatusReq()
        query_status_req.set_currency(currency)
        res=self.init_gate_pay_client().query_withdraw_status(query_status_req).__dict__
        print("查询提现状态：",res)
        return None

    def test_query_web_order_v3(self):
        web_query_order_req=WebQueryOrderReqV3()
        web_query_order_req.set_prepay_id("35297827964846503")
        web_query_order_req.set_merchant_trade_no("43wGhuujHKwAoLXRd7mMjihU")
        print(self.init_gate_pay_client().query_web_order_v3(web_query_order_req).get_data().__str__())

    def test_query_web_refund_support_chains_v3(self):
        query_refund_support_chains_req=QueryRefundSupportChainsReqV3()
        query_refund_support_chains_req.set_currency("USDT")
        print(self.init_gate_pay_client().query_web_refund_support_chains_v3(query_refund_support_chains_req).get_data().__str__())

    def test_query_web_refund_v3(self):
        query_refund_req=PaymentQueryRefundReqV3()
        query_refund_req.set_refund_request_id("35297827964846503")
        print(self.init_gate_pay_client().query_web_refund_v3(query_refund_req).get_data().__str__())

    def test_query_web_refund(self,refund_request_id:str="GzpNbjuLnH4"):
        query_refund_req=PaymentQueryRefundReq()
        query_refund_req.set_refund_request_id(refund_request_id)
        res=self.init_gate_pay_client().query_web_refund(query_refund_req).__dict__
        print("查询退款订单：",res)
        return res


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

    def test_channelmanage_save(self):
        real_data={"merchantChannelList":[{"channelId":"test003","desc":"1","address":
            "Noaddressavailable","chain":"SEPOLIA","customfiles_filed6":"3","email":"2",
             "customFields":[{"code":"customfiles_filed6","name":"自定义属性1","value":"3"}]}]}
        real_min_data={"merchantChannelList":[{"channelId":"test004",
                  "customFields":  [{"code":"customfiles_filed6","name":"自定义属性1"}]}]}
        custom_fields=CustomField()
        custom_fields.set_code("customfiles_filed6")
        custom_fields.set_name("自定义属性1")
        # custom_fields.set_value("3")

        merchant_channel=MerchantChannel()
        merchant_channel.set_channel_id(f"customer{RandomUtils.generate_nonce(7)}")#{RandomUtils.generate_nonce(7)}
        merchant_channel.set_custom_fields([custom_fields])

        channelmanage=SaveReq()
        channelmanage.set_merchant_channel_list([merchant_channel])
        print("新增客户渠道-名称", merchant_channel.get_channel_id())
        res = self.init_gate_pay_client().save_channel_manage(channelmanage).__dict__
        print("新增客户渠道-结果返回", res)
        return merchant_channel.get_channel_id()

    def test_create_batch_transfer_new(self,user_id:int=2124496616,amount:str="1",currency:str="USDT"):
        """
        批量转账
        :param user_id: 转账到哪个用户id
        :param amount: 转账金额
        :param currency: 币种
        :return:
        """
        batch_order = BatchOrder()
        batch_order.set_user_id(user_id)  # 测试账户从6790011 转给2124496616
        batch_order.set_amount(amount)

        create_batch_transfer_req = CreateBatchTransferReq()
        create_batch_transfer_req.set_batch_id(RandomUtils.generate_nonce(14))
        create_batch_transfer_req.set_merchant_batch_no(RandomUtils.generate_nonce(24))
        create_batch_transfer_req.set_biz_scene("DIRECT_TRANSFER")  # 场景
        create_batch_transfer_req.set_merchant_id("10002")  # 商户id 原始数据 10002
        create_batch_transfer_req.set_client_id("mZ96D37oKk-HrWJc")#原始数据mZ96D37oKk-HrWJc  其他数据UsidqkQusxhpkrQV
        create_batch_transfer_req.set_currency(currency)
        create_batch_transfer_req.set_name("Larry")
        create_batch_transfer_req.set_description("bonus")
        create_batch_transfer_req.set_batch_order_list([batch_order])
        print("#merchantBatchNo:" + create_batch_transfer_req.get_merchant_batch_no())
        print("#batch_id:" + create_batch_transfer_req.get_batch_id())
        res=self.init_gate_pay_client().create_batch_transfer(create_batch_transfer_req).__dict__
        print("批量转账返回值：",res)
        return create_batch_transfer_req

    def test_creat_batch_transfer_process(self):
        """
        主要测试：成功批量转账
        :return:
        """
        currency="USDT"
        res=self.test_query_balance()
        balance_data=jsonpath.jsonpath(res.get_data(),f"$.{currency}")
        print("#余额返回：",balance_data)

        print("#创建批量转账订单")
        create_batch_transfer_req=self.test_create_batch_transfer_new(2124496616,amount="0.001",currency=currency)
        time.sleep(2)

        print("#查询批量转账")
        self.test_query_batch_transfer(create_batch_transfer_req.get_batch_id(),create_batch_transfer_req.get_merchant_batch_no())
        print("查询余额，个人账户余额。特别说明，需要预发环境才可以查询")
        res = self.test_query_balance()
        balance_data = jsonpath.jsonpath(res.get_data(), f"$.{currency}")
        print("#余额再次返回：", balance_data)

        #self.assertEqual("1","2","转账失败，收支不平衡")

    def test_create_withdraw_order_proces(self):
        """
         特别注意 是生产环境：主要测试 个人账户-提现成功
        :return:
        """
        #查询币种支持的链（/v1/pay/wallet/currency_chains）
        res_=self.test_query_withdraw_chains()

        currency="USDT"
        print("#查询个人账户余额-是生产环境")
        res=self.test_query_withdraw_balance(currency)# 有返回值，但是拿不到
        print("#创建提现订单-是生产环境")
        batchId=self.test_create_withdraw_order(currency)

        print("#查询提现订单-是生产环境")
        self.test_query_withdraw_order(batchId)#查询提现订单

        print("#提现状态查询-是生产环境")
        self.test_query_withdraw_status(currency)

        print("#再次-提现个人账户查询-是生产环境")
        res = self.test_query_withdraw_balance(currency)  # 提现个人账户查询
        #断言
        #账户查询
        # self.assertIs()
    def test_create_gift_process(self):
        """
        主要测试 礼品卡创建
        :return:
        """
        print("#列出礼品卡模板")
        list_temp_req=self.test_list_gift_temp()
        card_temp_id=jsonpath.jsonpath(list_temp_req.get_data(),"$.[0].card_temp_id")[0]
        print("#创建礼品卡,礼品卡card_temp_id：",card_temp_id)
        get_data=self.test_create_gift(card_temp_id)
        batch_id=jsonpath.jsonpath(get_data,"$.batch_id")[0]
        card_num=jsonpath.jsonpath(get_data,"$.card_num")[0]
        print("礼品卡批次号:",batch_id)
        print("礼品卡卡号	:", card_num)
        print("#查看礼品卡列表")
        query_gift=self.test_query_gift(card_num)
        card_num_res=jsonpath.jsonpath(query_gift,"$.data.card_num")[0]
        self.assertEqual(card_num,card_num_res,"创建和查询礼品卡失败")

    def test_create_convert_order_process(self):
        """
        主要测试 。闪兑下单
        :return:
        """
        #查询可用闪兑币种（/v1/pay/convert/currency）
        # res_convert_currency=self.test_query_convert_currency()
        #查询可用闪兑币种对（/v1/pay/convert/pair）
        # res_=self.test_query_convert_pair()

        print("预览报价")
        amount="1"
        res=self.test_preview_convert(amount)
        quote_id=jsonpath.jsonpath(res,"$.data.quote_id")[0]
        print("闪兑下单:")
        res_order=self.test_create_convert_order_new(quote_id,amount)
        order_id=jsonpath.jsonpath(res_order,"$.data.order_id")[0]
        print("闪兑订单查询:")
        res_query=self.test_query_convert_order(order_id)
        status=jsonpath.jsonpath(res_query,"$.code")[0]
        self.assertEqual(status,"000000","闪兑下单失败")

    def test_channelmanage_save_process(self):
        """
        主要测试：创建渠道，修改渠道，删除渠道等
        :return:
        """
        channel_manage_fix=f"修改客户渠道{RandomUtils.generate_nonce(7)}"
        print("创建渠道")
        channel_id=self.test_channelmanage_save()
        print("查询客户渠道列表")
        res_list_channel=self.test_list_channel_manage(channel_id)
        print("修改客户渠道")
        res_update=self.test_update_channel_manage(channel_id)
        print("删除客户渠道")
        res_delete=self.test_delete_channel_manage(channel_id)
        print("查询客户渠道列表-查看是否删除")
        res_list=self.test_list_channel_manage(channel_id)

    def test_create_address_order_refund_convert_process(self):
        """
        主要测试 闪兑支付地址支付退款
        :return:
        """
        currencies="USDT"
        print("根据订单币种查询支持闪兑的币种")
        real_req={'code': '000000', 'data': {'currencies': ['USDT', 'USDC', 'DAI', 'POL']}, 'error_message': '', 'label': None, 'status': 'SUCCESS'}
        convert_currencies_res=self.test_get_address_supported_convert_currencies(currencies)
        chain=jsonpath.jsonpath(convert_currencies_res,"$.data.currencies[0]")[0]

        print("创建地址支付订单/下单-这是直接支付")
        address_order_res,merchant_trade_no=self.test_create_address_order(currencies,"1",2124505156,"TRX",f"{currencies}_TRX")

        print("查询地址支付订单详情")
        print("mock-这是直接支付")
        prepay_id=jsonpath.jsonpath(address_order_res,"$.data.prepay_id")[0]
        res=self.test_query_address_order(prepay_id,merchant_trade_no)
        print("创建地址支付闪兑支付单退款：")
        res=self.test_create_address_refund_convert(prepay_id,"1")

    def test_create_checkout_order_process(self):
        """
        主要测试 收银台流程，包括退款
        :return:
        """
        print("创建收银台订单")
        res=self.test_create_checkout_order(currency="USDT",amount="0.0001",user_id=2124505156
                                   ,chain="BSC",full_curr_type="USDT_BSC")
        prepay_id=jsonpath.jsonpath(res,"$.data.prepay_id")[0]
        print("中心化直付（非sdk接口）-gateapp直接支付")#使用订单返回的连接-扫码支付
        print("收款订单详情（非sdk/")
        print("创建退款")
        # prepay_id="35425216694845512"
        self.test_create_checkout_refund(prepay_id)

    def test_create_address_order_process(self):
        """
        主要测试 地址支付退款-获取资金流水账单
        :return:
        """
        #查询支持链列表
        # res_address_chains=self.test_get_address_chains()
        #查询支持币种列表（/v1/pay/address/currencies）
        res=self.test_get_address_currencies()

        res_c=CurrenciesReq()
        print("创建地址支付订单/下单-这是直接支付")
        currencies = "USDT"
        address_order_res = self.test_create_address_order(currencies, "0.0001", "2124505156", "TRX",

                                                          f"USDT_TRX")
        print("地址支付链上确认（/gfpay/v1/internal/pay/address/addresspayrecord）")#mock接口
        print("查询地址支付订单详情")

        print("#创建退款-地址支付退款")
        prepay_id="35424585334653161"
        self.test_create_address_refund(prepay_id)
        print("获取资金流水账单")
        self.test_query_bill_orders(prepay_id)
    def test_create_web_order_process(self):
        """
        创建web支付订单-查询链上交易详情-查询订单-关闭订单
        :return:
        """
        print("创建web支付订单")
        create_order_resp,merchantOrderNo=self.test_create_web_order()
        prepay_id=jsonpath.jsonpath(create_order_resp,"$.data.prepay_id")[0]

        time.sleep(5)
        print("查询链上交易详情")
        self.test_address_transaction_detail(prepay_id)
        print("查询订单")
        self.test_query_web_order(prepay_id,merchantOrderNo)
        print("关闭订单")
        self.test_close_web_order(prepay_id,merchantOrderNo)
    def test_create_qr_code_order_pross(self):
        """
        创建扫码支付订单（/v1/pay/transactions/native）-创建退款订单（/v1/pay/order/refund）-
        查询退款订单（/v1/pay/order/refund/query）
        :return:
        """
        print("创建扫码支付订单")
        create_order_resp,merchantOrderNo=self.test_create_qr_code_order("USDT","1")#扫码返回数据失效
        prepay_id=jsonpath.jsonpath(create_order_resp,"$.data.prepay_id")[0]
        print("创建退款订单")
        self.test_create_web_refund(prepay_id,"1")
        print("查询退款订单")
        self.test_query_web_refund(prepay_id)

# if __name__ == "__main__":
#     unittest.main()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromName(
        "gatepay_client_test.GatePayClientTest.test_creat_batch_transfer_process"
    )
    unittest.TextTestRunner().run(suite)