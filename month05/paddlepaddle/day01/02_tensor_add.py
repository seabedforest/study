# 高维度张量相加
import paddle.fluid as fluid
import numpy

x = fluid.layers.data(name="x",  # 名称
                      shape=[2, 3],  # 形状
                      dtype="float32")  # 类型

y = fluid.layers.data(name="y",
                      shape=[2, 3],
                      dtype="float32")

x_add_y = fluid.layers.elementwise_add(x, y)  # 按元素相加
x_mul_y = fluid.layers.elementwise_mul(x, y)  # 按元素相乘

place = fluid.CPUPlace()  # 运行在CPU
exe = fluid.Executor(place)  # 执行器
exe.run(fluid.default_startup_program())  # 初始化网络结构

a = numpy.array([[1, 2, 3], [4, 5, 6]])  # 输入x, 并转换为数组
b = numpy.array([[1, 1, 1], [2, 2, 2]])  # 输入y, 并转换为数组

#参数字典，key为字符串，value为张量
params ={"x":a,"y":b}
outs=exe.run(fluid.default_main_program(),   # 默认程序上执行
            feed=params,
            fetch_list=[x_add_y,x_mul_y])  # 获取结果

for i in outs:
    print(i)