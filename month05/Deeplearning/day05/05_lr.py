# 利用tf实现线性回归
import tensorflow as tf
import os

# 第一步：创建样本数据
x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
y = tf.matmul(x, [[2.0]]) + 5.0  # 计算y=2x+5

# 第二步：创建线性回归模型
## trainable=True表示变量的值运行更新
weight = tf.Variable(tf.random_normal([1, 1], name='w'), trainable=True)
bias = tf.Variable(0.0, name="b", trainable=True)
y_pred = tf.matmul(x, weight) + bias  # 计算wx+b

# 第三步：损失函数，创建优化器
loss = tf.reduce_mean(tf.square(y - y_pred))  # 均方差
## 优化器：对损失函数执行梯度下降优化
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 第四步：模型训练
tf.summary.scalar("losses",loss) # 收集损失函数的值，标量
saver=tf.train.Saver()  #实例化saver对象
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("weight:",weight.eval(),"bias:",bias.eval())
    # 定义文件写入对象
    fw=tf.summary.FileWriter("/home/tarena/summary",graph=sess.graph)
    # 检查模型是否已存在，如果存在则加载
    if os.path.exists("model/linear_model/checkpoint"):
        saver.restore(sess,"model/linear_model/") #从目录下加载

    # 开始训练
    for i in range(200):
        sess.run(train_op) # 执行梯度下降优化操作
        # 收集并合并摘要，返回合并后的数据
        # 合并后的数据可以存入事件文件
        summary=sess.run(tf.summary.merge_all())
        fw.add_summary(summary,i)  # 写入第i次收集的数据
        print("weight:",weight.eval(),"bias:",bias.eval())

    # 保存模型
    saver.save(sess,"model/linear_model/")