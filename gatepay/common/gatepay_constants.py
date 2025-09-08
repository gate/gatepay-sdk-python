class GatePayConstants:
    """
    常量类
    """

    # 请求地址相关
    END_POINT_DEFAULT = "http://dev.halftrust.xyz/gfpay"
    END_POINT_OPEN_PLATFORM = ""

    # 请求方法相关
    SCHEME_HTTP = "http"
    SCHEME_HTTPS = "https"
    METHOD_GET = "GET"
    METHOD_PUT = "PUT"
    METHOD_POST = "POST"
    METHOD_DELETE = "DELETE"
    METHOD_PATCH = "PATCH"
    METHOD_HEAD = "HEAD"

    # 请求头相关
    HEADER_CONTENT_TYPE = "Content-Type"
    HEADER_APPLICATION_JSON = "application/json"
    HEADER_ACCEPT = "Accept"  # Header 中的 Accept 字段
    HEADER_USER_AGENT = "User-Agent"
    HEADER_GATEPAY_API_KEY = "X-GatePay-Certificate-SN"
    HEADER_GATEPAY_CERTIFICATE_CLIENT_ID = "X-GatePay-Certificate-ClientId"
    HEADER_GATEPAY_TIMESTAMP = "X-GatePay-Timestamp"
    HEADER_GATEPAY_NONCE = "X-GatePay-Nonce"
    HEADER_GATEPAY_SIGNATURE = "X-GatePay-Signature"
    HEADER_GATE_CHANNEL_ID = "X-GatePay-ChannelId"
    HEADER_GATE_CLIENT_ID = "X-GatePay-ClientId"

    VERSION = "0.0.1"  # SDK 版本号
    USER_AGENT_FORMAT = "GatePay-SDK-Python/%s (%s) Python/%s"  # UserAgent中的信息
