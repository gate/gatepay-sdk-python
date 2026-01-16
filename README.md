# gatepay-sdk-python

GatePay API官方Python语言客户端代码库。

## 功能介绍

1. GatePay Python SDK适用于Python 3.7及以上版本。
2. 在开始使用GatePay SDK之前需要提前去GatePay注册中心注册账号，申请secretKey，密钥信息请妥善保管，如果遗失可能会造成非法用户使用此信息操作您的资源，给您造成数据和财产损失。
3. 接口SDK
4. 客户端GatePayClient，支持通过HTTP签名发送请求和接收应答。

## 安装

### 通过pip安装（推荐）

```bash
pip3 install gatepay-sdk-python
```


### 从源码安装

1. 下载地址:
todo

2. 您也可以使用以下命令获取安装包，代码会被下载到您本地的目录中。
```bash
git clone https://github.com/gatepay2025/gatepay-sdk-python
cd gatepay-sdk-python
pip3 install -r requirements.txt
```


## 依赖

- Python 3.7+

## 调用SDK

**业务侧调用SDK主要分为如下步骤：**

1. 引用GatePay Python版本SDK

2. 创建GatePayConfig

3. 创建GatePayClient

4. 设置业务请求参数

5. 调用SDK API接口

6. 处理得到响应

### 示例代码

#### 创建支付订单

```python
import time

from src.gatepay.gatepay_config import GatePayConfig
from src.gatepay.infrastructure.credential import Credential
from src.gatepay.client.gatepay_client import GatePayClient

from src.gatepay.api.model.req.env_req import EnvReq
from src.gatepay.api.model.req.goods_req import GoodsReq
from src.gatepay.api.model.req.address.create_order_req import CreateOrderReq as AddressCreateOrderReq
from src.gatepay.common.utils.random_utils import RandomUtils

# env_address 终端地址，不同环境请根据实际情况填写
# client_id 商户api密钥
# secret_key 密钥
# api_key 商户api密钥
gate_pay_config = GatePayConfig("env_address", 30, "api_key", Credential("secret_key", "api_key")
                                )
gatepay_client = GatePayClient(gate_pay_config)

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
# your merchantUserId
create_order_req.set_merchant_user_id(6790011)
create_order_req.set_chain("ETH")
create_order_req.set_full_curr_type("USDT_ETH")
create_order_req.set_channel_id("")
print("merchantOrderNo:" + create_order_req.get_merchant_trade_no())
response = create_order_resp = gatepay_client.create_address_order(create_order_req)
print(create_order_resp.get_data().__str__())

# 处理响应
print(f"Status: {response.get_status()}")
print(f"Code: {response.get_code()}")
```

## API模块

GatePay SDK包含以下主要API模块：

- [ApiAddress](src/gatepay/api/api_address.py): 地址支付接口
- [ApiPayment](src/gatepay/api/api_payment.py): 普通支付接口
- [ApiCheckout](src/gatepay/api/api_checkout.py): 收银台支付接口
- [ApiQrCode](src/gatepay/api/api_qrcode.py): 二维码支付接口
- [ApiBill](src/gatepay/api/api_bill.py): 账单接口
- [ApiChannelManage](src/gatepay/api/api_channel_manage.py): 渠道管理接口
- [ApiConvert](src/gatepay/api/api_convert.py): 闪兑接口
- [ApiGift](src/gatepay/api/api_gift.py): 礼品卡接口
- [ApiWithdraw](src/gatepay/api/api_withdraw.py): 提现接口

## 错误处理

SDK会抛出异常来处理错误情况：

```python
        try:
            # 前置处理
            self._pre_process(req)

            # 执行请求处理
            http_response = self._do_process(req)

            # 使用PROCESSOR处理响应
            return self.processor.post_process_response(http_response.text, resp_class)

        except Exception as e:
            raise RuntimeError(str(e))
```


## 安全建议

1. 请妥善保管您的secretKey和apiKey
2. 不要在客户端代码中硬编码密钥信息
3. 使用环境变量或配置文件来管理密钥
4. 定期更换密钥以提高安全性

## 技术支持

如有技术问题，请联系GatePay技术支持团队：
- 邮箱: gatepay@gate.com
- 官方文档: https://www.gate.com/pay

## 版本更新

请关注GitHub仓库获取最新版本更新和功能增强。

## 许可证

本SDK遵循MIT许可证协议。




