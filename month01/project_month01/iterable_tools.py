"""
    可迭代对象的工具箱
"""


class IterableHelper:
    """
        可迭代对象助手类:负责定义对可迭代对象的常用操作
    """

    @staticmethod
    def find_all(list_target, func):
        """
        查找各种数据，返回多个结果
        :param list_target: 可迭代对象
        :param func: 匿名函数
        """
        for item in list_target:
            if func(item):
                yield item

    @staticmethod
    def find_single(list_target, func):
        """
        查找各种数据，返回一个结果
        :param list_target: 可迭代对象
        :param func: 匿名函数
        :return: 一个结果
        """
        for item in list_target:
            if func(item):
                return item

    @staticmethod
    def get_count(list_target, func):
        """
        统计迭代对象的长度，某个元素的个数
        :param list_target: 可迭代对象
        :param func: 匿名函数
        :return:总数
        """
        count = 0
        for item in list_target:
            if func(item):
                count += 1
        return count

    @staticmethod
    def select(list_target, func):
        """
        遍历可迭代对象，根据选择条件返回多个结果
        :param list_target: 可迭代对象
        :param func: 匿名函数
        """
        for item in list_target:
            yield func(item)

    @staticmethod
    def get_max(list_target, func):
        """
        查找最大值
        :param list_target: 可迭代对象
        :param func: 匿名函数
        :return: 最大值
        """
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(max_value) < func(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def get_min(list_target, func):
        """
        查找最小值
        :param list_target: 可迭代对象
        :param func: 匿名函数
        :return: 最大值
        """
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(min_value) > func(list_target[i]):
                min_value = list_target[i]
        return min_value

    @staticmethod
    def order_by(list_target, func):
        """
        根据条件进行升序
        :param list_target: 可迭代对象
        :param func: 匿名函数
        """
        for r in range(len(list_target) - 1):
            for c in range(r + 1, len(list_target)):
                if func(list_target[r]) > func(list_target[c]):
                    list_target[r], list_target[c] = list_target[c], list_target[r]
        return list_target
