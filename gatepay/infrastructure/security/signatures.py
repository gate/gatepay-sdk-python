import hmac
import base64

class Signature:
    HMAC_SHA512 = "sha512"
    INVALID_SIGNATURE = "invalid signature"

    @staticmethod
    def verify_signature(timestamp: str, nonce: str, body: str, secret_key: str) -> str:
        """
        生成签名
        :param timestamp: 时间戳
        :param nonce: 随机字符串
        :param body: 请求体
        :param secret_key: 密钥
        :return: 签名字符串
        """
        payload = f"{timestamp}\n{nonce}\n{body}\n"
        return Signature.sign(payload, secret_key)

    @staticmethod
    def sign(signing_data: str, key: str) -> str:
        """
        对数据进行签名
        :param signing_data: 要签名的数据
        :param key: 密钥
        :return: 签名字符串
        """
        try:
            hmac_obj = hmac.new(
                key.encode('utf-8'),
                signing_data.encode('utf-8'),
                Signature.HMAC_SHA512
            )
            signature = hmac_obj.digest()
            return signature.hex()
        except Exception as e:
            raise RuntimeError("Error generating signature") from e

    @staticmethod
    def hex_string_to_byte_array(hex_string: str) -> bytes:
        """
        将十六进制字符串转换为字节数组
        :param hex_string: 十六进制字符串
        :return: 字节数组
        """
        return bytes.fromhex(hex_string)

    @staticmethod
    def constant_time_equals(a: bytes, b: bytes) -> bool:
        """
        常量时间比较两个字节数组是否相等，防止时间侧信道攻击
        :param a: 第一个字节数组
        :param b: 第二个字节数组
        :return: 如果两个字节数组相等返回True，否则返回False
        """
        if len(a) != len(b):
            return False

        result = 0
        for i in range(len(a)):
            result |= a[i] ^ b[i]
        return result == 0

    @staticmethod
    def verify_sign(signing_data: str, signature: str, key: str) -> str:
        """
        验证签名是否有效
        :param signing_data: 签名数据
        :param signature: 签名
        :param key: 密钥
        :return: 如果签名有效返回None，否则返回错误信息
        """
        try:
            decoded_signature = Signature.hex_string_to_byte_array(signature)

            hmac_obj = hmac.new(
                key.encode('utf-8'),
                signing_data.encode('utf-8'),
                Signature.HMAC_SHA512
            )
            calculated_signature = hmac_obj.digest()

            if not Signature.constant_time_equals(decoded_signature, calculated_signature):
                return Signature.INVALID_SIGNATURE

            return None
        except Exception:
            return Signature.INVALID_SIGNATURE

    @staticmethod
    def generate_signature(timestamp: str, nonce: str, body: str, secret_key: str) -> str:
        """
        生成签名
        :param timestamp: 时间戳
        :param nonce: 随机字符串
        :param body: 请求体
        :param secret_key: 密钥
        :return: 签名字符串
        """
        try:
            # Concatenate timestamp, nonce and body
            message = timestamp + nonce + body

            # Create HMAC-SHA512
            hmac_sha512 = hmac.new(
                secret_key.encode('utf-8'),
                message.encode('utf-8'),
                Signature.HMAC_SHA512
            )

            # Calculate signature
            hash_bytes = hmac_sha512.digest()

            # Encode with Base64
            return base64.b64encode(hash_bytes).decode('utf-8')
        except Exception as e:
            raise RuntimeError("Failed to generate signature") from e
