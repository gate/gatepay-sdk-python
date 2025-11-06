class Credential:
    """
    密钥类
    """

    def __init__(self, secret_key: str, api_key: str):
        """
        初始化 Credential 实例

        :param secret_key: 商户密钥
        :param api_key: 商户api密钥
        """
        self.secret_key = secret_key
        self.api_key = api_key

    def get_secret_key(self) -> str:
        """
        获取商户密钥

        :return: 商户密钥
        """
        return self.secret_key

    def set_secret_key(self, secret_key: str) -> None:
        """
        设置商户密钥

        :param secret_key: 商户密钥
        """
        self.secret_key = secret_key

    def get_api_key(self) -> str:
        """
        获取商户api密钥

        :return: 商户api密钥
        """
        return self.api_key

    def set_api_key(self, api_key: str) -> None:
        """
        设置商户api密钥

        :param api_key: 商户api密钥
        """
        self.api_key = api_key
