"""
商品信息查找工具
"""


class IterableHelper:
    @staticmethod
    def find_infos(list_target, func):
        """
        商品信息查找工具
        :param list_target: 商品列表
        :param func: 查找条件函数
        """
        for item in list_target:
            if func(item):
                yield item

    @staticmethod
    def get_count(list_target, func):
        """
        商品信息统计
        :param list_target: 商品列表
        :param func: 统计条件函数
        :return: 计数
        """
        count = 0
        for item in list_target:
            if func(item):
                count += 1
        return count

    @staticmethod
    def get_min(list_target, func):
        min_value = list_target[0]
        for index in range(1, len(list_target)):
            if func(min_value) > func(list_target[index]):
                min_value = list_target[index]
        return min_value

    @staticmethod
    def sort_asc(list_target, func):
        for i in range(len(list_target)-1):
            for index in range(i+1,len(list_target)):
                if func(list_target[i]) > func(list_target[index]):
                    list_target[i], list_target[index] = list_target[index], list_target[i]

