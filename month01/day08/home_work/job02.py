"""
4.  参照下列代码,定义函数,计算孩子身高.
    father_height = float(input("请输入父亲的身高（厘米）:"))
    mother_height = float(input("请输入母亲的身高（厘米）:"))
    son_height = (father_height + mother_height) * 0.54
    print("预测儿子的身高是:" + str(son_height) + "厘米")
@author hailin
@date 2020-05-11
"""


def calculate_child_height(father_height, mother_height):
    """
    计算孩子身高
    :param father_height: 父亲的身高
    :param mother_height: 母亲的身高
    :return:
    """
    return (father_height + mother_height) * 0.54


# 应用定义函数
father_height = float(input("请输入父亲的身高（厘米）:"))
mother_height = float(input("请输入母亲的身高（厘米）:"))
child_height = calculate_child_height(father_height, mother_height)
print("预测儿子的身高是:%.2f厘米" % child_height)
