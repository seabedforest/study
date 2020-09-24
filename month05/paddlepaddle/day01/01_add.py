"""
paddle第一个示例：张量简单相加
"""
import paddle.fluid as fluid

# 创建两个类型为int64, 形状为1*1张量
x = fluid.layers.fill_constant(shape=[1],dtype="int64",value=5)
y = fluid.layers.fill_constant(shape=[1],dtype="int64",value=1)
z=x+y # z只是一个对象,没有run,所以没有值

# 创建执行器
place = fluid.CPUPlace()  #指定在cpu上执行
exe = fluid.Executor(place)  #创建执行器
result=exe.run(fluid.default_main_program(),fetch_list=[z])
print(result)   # result为多维张量

