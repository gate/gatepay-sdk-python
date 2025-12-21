from typing import List

from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.gift.create_req import CreateReq
from src.gatepay.api.model.req.gift.list_temp_req import ListTempReq
from src.gatepay.api.model.req.gift.query_req import QueryReq
from src.gatepay.api.model.resp.gift.create_resp import CreateResp
from src.gatepay.api.model.resp.gift.list_temp_resp import ListTempResp
from src.gatepay.api.model.resp.gift.query_resp import QueryResp
from src.gatepay.base_response import BaseResponse
from src.gatepay.gatepay_config import GatePayConfig


class ApiGift(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiGift 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def create(self, request: CreateReq) -> 'BaseResponse[CreateResp]':
        """
        创建礼品卡

        :param request: 创建礼品卡请求参数
        :return: 创建礼品卡响应结果
        """
        return super().process_non_base_response(request, CreateResp)

    def list_temp(self, request: ListTempReq) -> List[ListTempResp]:
        """
        列出礼品卡模板

        :param request: 列出模板请求参数
        :return: 列出模板响应结果
        """
        return super().process_non_base_response(request, List[ListTempResp])

    def query(self, request: QueryReq) -> 'BaseResponse[QueryResp]':
        """
        查询礼品卡

        :param request: 查询礼品卡请求参数
        :return: 查询礼品卡响应结果
        """
        return super().process_non_base_response(request, QueryResp)
