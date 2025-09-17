from enum import Enum

class CommonUtils:

    @staticmethod
    def filter_none_recursive(obj: object):
        """
        递归过滤对象中的None值
        """
        if isinstance(obj, dict):
            return {k: CommonUtils.filter_none_recursive(v) for k, v in obj.items() if v is not None}
        elif isinstance(obj, list):
            return [CommonUtils.filter_none_recursive(item) for item in obj if item is not None]
        elif hasattr(obj, '__dict__'):  # 对于普通对象，递归处理其属性
            obj_dict = {}
            for attr_name in dir(obj):
                if not attr_name.startswith('_') and not callable(getattr(obj, attr_name)):
                    attr_value = getattr(obj, attr_name)
                    # 判断如果对象是枚举类型，直接取其name
                    if isinstance(getattr(obj, attr_name), Enum):
                        obj_dict[attr_name] =attr_value.name
                        continue
                    if attr_value is not None:
                        obj_dict[attr_name] = CommonUtils.filter_none_recursive(attr_value)
            return obj_dict
        else:
            return obj
