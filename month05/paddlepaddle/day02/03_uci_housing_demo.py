#波士顿房价预测案例
''' 数据集介绍:
 1) 共506行，每行14列，前13列描述房屋特征信息，最后一列为价格中位数
 2) 考虑了犯罪率（CRIM）        宅用地占比（ZN）
    非商业用地所占尺寸（INDUS）  查尔斯河虚拟变量（CHAS）
    环保指数（NOX）            每栋住宅的房间数（RM）
    1940年以前建成的自建单位比例（AGE）   距离5个波士顿就业中心的加权距离（DIS）
    距离高速公路便利指数（RAD）          每一万元不动产税率（TAX）
    教师学生比（PTRATIO）              黑人比例（B）
    房东属于中低收入比例（LSTAT）
'''
import paddle
import paddle.fluid as fluid
import numpy as np
import os
import matplotlib.pyplot as plt

# step1: 数据准备
# paddle提供了uci_housing训练集、测试集，直接读取并返回数据
BUF_SIZE = 500
BATCH_SIZE = 20

# 训练数据集读取器
# 创建随机读取器
random_reader = paddle.reader.shuffle(paddle.dataset.uci_housing.train(),buf_size=BATCH_SIZE)
train_reader = paddle.batch(random_reader,batch_size=BATCH_SIZE) # 创建随机读取器
# 打印数据
# train_data = paddle.dataset.uci_housing.train()
# for sample_data in train_data():
#    print(sample_data)

# step2: 配置网络
# 定义输入、输出，类型均为张量
x=fluid.layers.data(name="x",shape=[13],dtype="float32")
y=fluid.layers.data(name="y",shape=[1],dtype="float32")
# 定义个简单的线性网络，连接输入层、输出层
y_predict=fluid.layers.fc(input=x, # 输入数据
                          size=1, # 输出值个数
                          act=None) # 激活函数
# 定义损失函数，并将损失函数指定给优化器
cost=fluid.layers.square_error_cost(input=y_predict,  # 预测值，张量
                                    label=y)  # 期望值，张量
avg_cost=fluid.layers.mean(cost) # 求损失值平均数
optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.001)  # 使用随机梯度下降优化器
opts = optimizer.minimize(avg_cost)  # 优化器最小化损失值

# 创建新的program用于测试计算
test_program=fluid.default_main_program().clone(for_test=True)

# step3: 模型训练、模型评估
place = fluid.CPUPlace()
exe=fluid.Executor(place)
exe.run(fluid.default_startup_program())

feeder = fluid.DataFeeder(place=place,feed_list=[x,y])

iter=0
iters=[]
train_costs=[]
EPOCH_NUM=120
model_save_dir="model/uci_housing"   # 模型保存路径
for pass_id in range(EPOCH_NUM):
    train_cost=0
    i = 0
    for data in train_reader():
        i += 1
        train_cost=exe.run(program=fluid.default_main_program(),
                           feed=feeder.feed(data),
                           fetch_list=[avg_cost])

    if i % 20 == 0:  # 每20笔打印一次损失函数值
        print("PassID: %d, Cost: %0.5f" % (pass_id,train_cost[0][0]))
    iter = iter + BATCH_SIZE #加上每批次笔数
    iters.append(iter) #记录笔数
    train_costs.append(train_cost[0][0]) # 记录损失值

# 保存模型
if not os.path.exists(model_save_dir): # 如果存储模型的目录不存在，则创建
    os.makedirs(model_save_dir)
fluid.io.save_inference_model(model_save_dir, # 保存模型的路径
                              ["x"], # 预测需要喂入的数据
                              [y_predict], # 保存预测结果的变量
                              exe) # 模型

# 训练过程可视化
plt.figure("Training Cost")
plt.title("Training Cost",fontsize=24)
plt.xlabel("iter",fontsize=14)
plt.ylabel("cost",fontsize=14)
plt.plot(iters,train_costs,color="red",label="Training Cost")
plt.grid()
plt.savefig("train.png")

# step4: 模型预测
infer_exe = fluid.Executor(place) # 创建用于预测的Executor
infer_scope=fluid.core.Scope()  # 修改全局/默认作用域, 运行时中的所有变量都将分配给新的scope
infer_result = [] #预测值列表
ground_truths = [] #真实值列表

# with fluid.scope_guard(infer_scope):
# 加载模型，返回三个值
# program: 预测程序(包含了数据、计算规则)
# feed_target_names: 需要喂入的变量
# fetch_targets: 预测结果保存的变量
[infer_program,feed_target_names,fetch_targets] = fluid.io.load_inference_model(model_save_dir,
                                                                                infer_exe)

# 获取测试数据
infer_reader = paddle.batch(paddle.dataset.uci_housing.test(),batch_size=200) # 测试数据读取器
test_data=next(infer_reader())  # 获取一条数据
test_x = np.array([data[0] for data in test_data]).astype("float32")
test_y = np.array([data[1] for data in test_data]).astype("float32")

x_name=feed_target_names[0]  # 模型中保存的输入参数名称
print("x_name",x_name)
results = infer_exe.run(infer_program,feed={x_name:np.array(test_x)},
                       fetch_list=fetch_targets)
# 预测值
for idx,val in enumerate(results[0]):
    print("%d: %.2f" % (idx,val))
    infer_result.append(val)

# 真实值
for idx,val in enumerate(test_y):
    print("%d: %.2f" % (idx,val))
    ground_truths.append(val)


# 可视化
plt.figure('scatter')
plt.title("TestFigure", fontsize=24)
plt.xlabel("ground truth", fontsize=14)
plt.ylabel("infer result", fontsize=14)
x = np.arange(1, 30)
y = x
plt.plot(x, y)
plt.scatter(ground_truths, infer_result, color="green", label="Test")
plt.grid()
plt.legend()
plt.savefig("predict.png")
plt.show()