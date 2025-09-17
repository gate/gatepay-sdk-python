from src.gatepay.api.base_api import BaseApi
from src.gatepay.api.model.req.manage.delete_req import DeleteReq
from src.gatepay.api.model.req.manage.list_req import ListReq
from src.gatepay.api.model.req.manage.save_req import SaveReq
from src.gatepay.api.model.req.manage.update_req import UpdateReq
from src.gatepay.api.model.resp.manage.delete_resp import DeleteResp
from src.gatepay.api.model.resp.manage.list_resp import ListResp
from src.gatepay.api.model.resp.manage.save_resp import SaveResp
from src.gatepay.api.model.resp.manage.update_resp import UpdateResp
from src.gatepay.gatepay_config import GatePayConfig


class ApiChannelManage(BaseApi):


    def __init__(self, gate_pay_config: GatePayConfig):
        """
        初始化 ApiChannelManage 实例

        :param gate_pay_config: GatePay配置
        """
        super().__init__(gate_pay_config)

    def save(self, request: SaveReq) -> SaveResp:
        """
        新增客户渠道

        :param request: 保存请求参数
        :return: 保存响应结果
        """
        return super().process(request, SaveResp)

    def list(self, request: ListReq) -> ListResp:
        """
        查询客户渠道列表

        :param request: 列表请求参数
        :return: 列表响应结果
        """
        return super().process(request, ListResp)

    def update(self, request: UpdateReq) -> UpdateResp:
        """
        修改客户渠道

        :param request: 更新请求参数
        :return: 更新响应结果
        """
        return super().process(request, UpdateResp)

    def delete(self, request: DeleteReq) -> DeleteResp:
        """
        删除客户渠道

        :param request: 删除请求参数
        :return: 删除响应结果
        """
        return super().process(request, DeleteResp)
