import json
from typing import TypeVar, Generic, Optional, Type, Any, get_origin, List, get_args

from src.gatepay.common.enums.code import Code
from src.gatepay.common.enums.status import Status

T = TypeVar('T')


class BaseResponse(Generic[T]):
    """
    基础响应类
    """

    def __init__(self):
        self.status: Optional[str] = None
        self.code: Optional[str] = None
        self.data: Optional[T] = None
        self.error_message: Optional[str] = None
        self.label: Optional[str] = None


def is_empty(obj: Any) -> bool:
    """
    判断对象是否为空
    """
    if isinstance(obj, dict):
        return len(obj) == 0
    elif isinstance(obj, list):
        return len(obj) == 0
    return False


class Processor:
    """
    处理器类，用于处理JSON响应
    """

    @staticmethod
    def post_process_response(json_str: str, data_class: Type[T]) -> BaseResponse[T]:
        """
        处理响应JSON字符串

        Args:
            json_str: JSON格式的响应字符串
            data_class: 数据类类型

        Returns:
            BaseResponse: 处理后的响应对象
        """
        base_response = BaseResponse()
        base_response.status = Status.SUCCESS.value
        base_response.code = Code.SUCCESS.code
        base_response.data = None
        base_response.error_message = None

        if not json_str or not json_str.strip():
            return base_response

        try:
            json_node = json.loads(json_str)
            if json_node is not None:
                # 处理status节点
                if "status" in json_node:
                    base_response.status = json_node["status"]

                # 处理code节点
                if "code" in json_node:
                    base_response.code = json_node["code"]

                # 处理error message节点
                if "errorMessage" in json_node:
                    base_response.error_message = json_node["errorMessage"]

                # 处理label节点
                if "label" in json_node:
                    base_response.label = json_node["label"]

                # 处理data节点
                if "data" in json_node:
                    data_node = json_node["data"]
                    if not ((isinstance(data_node, dict) and is_empty(data_node)) or
                            (isinstance(data_node, list) and is_empty(data_node))):
                        # 检查是否为List类型
                        origin = get_origin(data_class)
                        if origin is list or origin is List:
                            # 处理List[T]类型
                            args = get_args(data_class)
                            if args and hasattr(args[0], 'from_dict'):
                                # 如果列表元素类型有from_dict方法
                                element_type = args[0]
                                base_response.data = [element_type.from_dict(item) for item in data_node]
                            else:
                                # 直接赋值列表
                                base_response.data = data_node
                        elif hasattr(data_class, 'from_dict'):
                            # 处理普通类的from_dict方法
                            base_response.data = data_class.from_dict(data_node)
                        else:
                            # 其他情况的处理
                            resp = data_class()
                            for key, value in data_node.items():
                                if hasattr(resp, f"set_{key}"):
                                    getattr(resp, f"set_{key}")(value)
                                elif hasattr(resp, key):
                                    setattr(resp, key, value)
                            base_response.data = resp
                        return base_response
                else:
                    # 没有data字段时的处理
                    origin = get_origin(data_class)
                    if origin is list or origin is List:
                        args = get_args(data_class)
                        if args and hasattr(args[0], 'from_dict'):
                            element_type = args[0]
                            base_response.data = [element_type.from_dict(item) for item in json_node]
                        else:
                            base_response.data = json_node
                    elif hasattr(data_class, 'from_dict'):
                        base_response.data = data_class.from_dict(json_node)
                    else:
                        base_response.data = json_node

            return base_response

        except Exception as e:
            base_response.status = Status.FAIL.value
            base_response.code = Code.FAIL.code
            base_response.data = None
            base_response.error_message = str(e)
            return base_response