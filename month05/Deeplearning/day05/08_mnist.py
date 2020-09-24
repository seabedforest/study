# 手写体识别
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import pylab

# MNIST数据集已经标准化，tf提供了专门的API用于处理
mnist = input_data.read_data_sets("MNIST_data/",  # 样本所在目录，如果没有则下载
                                  one_hot=True)  # 标签采用独热编码表示
# 占位符
x = tf.placeholder(tf.float32, [None, 784])  # N个样本，每个样本784特征
y = tf.placeholder(tf.float32, [None, 10])  # N个样本,每个样本10个概率

# 权重、偏置
w = tf.Variable(tf.random_normal([784, 10]))
b = tf.Variable(tf.zeros([10]))
# 构建神经网络模型（本质线性模型）
pred_y = tf.nn.softmax(tf.matmul(x, w) + b)
print("pred_y.shape:", pred_y.shape)
# 损失函数:交叉商
cross_enctrpy = -tf.reduce_sum(y * tf.log(pred_y), reduction_indices=1)
cost = tf.reduce_mean(cross_enctrpy)  # 求均值
# 优化器
lr = 0.01
optimizer = tf.train.GradientDescentOptimizer(lr).minimize(cost)

train_epochs = 10  # 训练轮次
batch_size = 100  # 批次大小
saver = tf.train.Saver()  # 模型保存加载对象
model_path = "./model/mnist/mnist_model.ckpt"  # 模型前缀

# 打开session,执行训练
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # 外层循环控制循环轮次
    for epoch in range(train_epochs):
        avg_cost = 0.0  # 临时变量，存放损失值
        total_batch = int(mnist.train.num_examples / batch_size)

        # 内层循环，控制每个轮次下循环多个批次
        for i in range(total_batch):
            # 读取一个批次样本
            # 图像存入xs, 标签存入ys
            xs, ys = mnist.train.next_batch(batch_size)
            params = {x: xs, y: ys}  # 参数字典
            o, c = sess.run([optimizer, cost], feed_dict=params)  # 训练
            avg_cost += (c / total_batch)  # 计算平均损失值

        # 每轮训练结束后，打印损失函数值
        print("epoch:%d,cost=%f" % (epoch, avg_cost))
    print("训练结束。。")

    # 评估准确率
    ## 比较预测结果、真实标签最大值的索引，返回布尔类型张量
    corrected_pred = tf.equal(tf.argmax(pred_y, 1), tf.argmax(y, 1))
    ## 将布尔类型的张量转换为浮点数，累加除以样本数量
    accuracy = tf.reduce_mean(tf.cast(corrected_pred,tf.float32))
    params2 = {x:mnist.test.images,y:mnist.test.labels}  # 测试集下的数据
    acc = accuracy.eval(params2)  # 执行准确率计算
    print("accuracy:",acc)  # 打印准确率

    # 保存模型
    save_path=saver.save(sess,model_path)
    print("模型保存成功:",save_path)

# 测试模型
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess,model_path)  #加载模型

    batch_xs,batch_ys = mnist.test.next_batch(2)  #读取2个测试样本
    output=tf.argmax(pred_y,1)  # 预测结果值

    output_val,predv = sess.run([output,pred_y],  # 操作
                                feed_dict={x:batch_xs})  #参数

    print("预测结论:\n",output_val,"\n")
    print("实际结果:\n",batch_ys,"\n")
    print("预测概率:\n",predv,"\n")

    # 显示图片
    im = batch_xs[0]  # 第1个测试样本数据
    im=im.reshape(-1,28)
    pylab.imshow(im)
    pylab.show()

    im = batch_xs[1]  # 第2个测试样本数据
    im = im.reshape(-1,28)
    pylab.imshow(im)
    pylab.show()
