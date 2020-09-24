"""
利用卷积神经网络实现服饰识别
数据集：时尚版ＭＮＩＳＴ，２８＊２８单通道图像，１０个类别
网络结构：
卷积池化 --> 卷积池化 --> fc --> dropout --> fc(softmax)
"""
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


class FashionMnist():
    # 第1卷积层输出通道数(第1个卷基层卷积核数量，超参数)
    out_features1 = 12
    # 第2卷积层输出通道数(第1个卷基层卷积核数量，超参数)
    out_features2 = 24
    # 全连接层神经元数量（超参数）
    con_neurons = 512

    def __init__(self, path):
        """
        构造方法
        :param path: 数据集所在目录
        """
        self.sess = tf.Session()  # 创建session对象
        self.data = read_data_sets(path, one_hot=True)  # 数据集操作对象

    def init_weight_var(self, shape):
        """
        根据指定的形状初始化权重
        :param shape: 权重的形状
        :return: 经过初始化后的权重值
        """
        # 截尾正态分布(截掉两个标准差外的数据)
        inital = tf.truncated_normal(shape, stddev=0.1)

        return tf.Variable(inital)

    def init_bias_var(self, shape):
        """
        根据指定形状初始化偏置
        :param shape: 形状
        :return: 经过初始化后的偏置值
        """
        inital = tf.constant(1.0, shape=shape)
        return tf.Variable(inital)

    def conv2d(self, x, w):
        """
        二维卷积
        :param x: 原始数据
        :param w: 卷积核(本质就是权重)
        :return: 返回卷积运算结果
        """
        # 输入：四维张量 [batch, in_h, in_w, in_chn]
        # 卷积核: [h, w, in_chn, out_chn]
        return tf.nn.conv2d(x,  # 原始数据
                            w,  # 卷积核
                            strides=[1, 1, 1, 1],  # 四个维度上的步长值
                            padding="SAME")  # 输出矩阵和输入矩阵相同大小

    def max_pool_2x2(self, x):
        """
        池化函数
        :param x: 原始数据
        :return: 返回池化运算结果
        """
        return tf.nn.max_pool(x,  # 原始数据
                              ksize=[1, 2, 2, 1],  # 各维度上池化区域大小
                              strides=[1, 2, 2, 1],  # 步长
                              padding="SAME")

    def create_conv_pool_layer(self, x, input_features, out_features):
        """
        创建卷积、激活、池化操作层
        :param x: 原始数据
        :param input_features: 输入数据通道数
        :param out_features: 输出数据通道数
        :return: 经过卷积、激活、池化计算结果
        """
        filter = self.init_weight_var([5, 5, input_features, out_features])  # 卷积核
        # 偏置，等于卷运算输出通道数
        b_conv = self.init_bias_var([out_features])
        # 卷积、激活运算
        h_conv = tf.nn.relu(self.conv2d(x, filter) + b_conv)
        # 池化
        h_pool = self.max_pool_2x2(h_conv)
        return h_pool

    def create_fc_layer(self, h_pool_flat, input_features, con_neurons):
        """
        全连接层
        :param h_pool_flat:  输入数据，经拉伸后的一维张量
        :param input_features:  输入特征数量
        :param con_neurons:  输出特征数量(等与神经元数量)
        :return:  经过全连接计算的值
        """
        # 权重
        w_fc = self.init_weight_var([input_features, con_neurons])
        # 偏置，数量等于前一个操作输出的数量
        b_fc = self.init_bias_var([con_neurons])
        # 全连接计算操作
        h_fc1 = tf.nn.relu(tf.matmul(h_pool_flat, w_fc) + b_fc)
        return h_fc1

    def build(self):
        """
        组件CNN
        :return:
        """
        self.x = tf.placeholder(tf.float32, shape=[None, 784])
        # 变维，从而输入到卷基层
        x_image = tf.reshape(self.x, [-1, 28, 28, 1])
        self.y_ = tf.placeholder(tf.float32, shape=[None, 10])  # 标签
        # 第一组卷积池化
        h_pool1 = self.create_conv_pool_layer(x_image, 1, self.out_features1)
        # 第二组卷积池化
        h_pool2 = self.create_conv_pool_layer(h_pool1,  # 上一层输出作为输入
                                              self.out_features1,  # 输入通道数为上一层输出通道数
                                              self.out_features2)  # 当前层输出通道数
        # 全连接层
        ## 计算特征点数量
        h_pool2_flat_features = 7 * 7 * self.out_features2
        ## 拉伸成一维
        h_pool2_flat = tf.reshape(h_pool2, [-1, h_pool2_flat_features])
        ## 喂入全连接层
        h_fc = self.create_fc_layer(h_pool2_flat,  # 输入数据，经过拉伸一维张量
                                    h_pool2_flat_features,  # 输入特征值数量
                                    self.con_neurons)  # 输出特征值数量(等于本层神经元数量)
        # dropout(丢弃学习，防止过拟合)
        self.keep_prob = tf.placeholder("float")
        h_fc1_drop = tf.nn.dropout(h_fc, self.keep_prob)
        # 输出层
        w_fc = self.init_weight_var([self.con_neurons, 10])  # 权重
        b_fc = self.init_bias_var([10])  # 偏置
        # 全连接计算
        y_conv = tf.matmul(h_fc1_drop, w_fc) + b_fc

        # 评估准确率
        ## 比较预测值、真实值最大概率索引是否相等，返回布尔类型张量
        correct_pred = tf.equal(tf.argmax(y_conv, 1),
                                tf.argmax(self.y_, 1))
        self.accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))  # 准确率

        # 损失函数
        loss = tf.nn.softmax_cross_entropy_with_logits(labels=self.y_,  # 真实结果
                                                       logits=y_conv)  # 预测结果
        cross_entropy = tf.reduce_mean(loss)
        # 优化器
        ## Adam优化器：震荡相对较小，自动调整学习率
        optimizer = tf.train.AdadeltaOptimizer(0.001)
        self.train_step = optimizer.minimize(cross_entropy)

    def train(self):
        self.sess.run(tf.global_variables_initializer())
        batch_size = 100
        print("开始训练...")

        for i in range(10):  # 外层循环控制训练轮次
            # 计算总批次数量
            total_batch = int(self.data.train.num_examples / batch_size)

            for j in range(total_batch):  # 内层循环控制训练批次
                # 读取一个批次样本
                xs, ys = self.data.train.next_batch(batch_size)
                params = {self.x: xs, self.y_: ys, self.keep_prob: 0.5}  # 参数字典
                # 训练
                t, acc = self.sess.run([self.train_step, self.accuracy], params)

                if j % 100 == 0:  # 每100批次打印一次
                    print("i:%d,j:%d,acc:%f" % (i, j, acc))

    def eval(self, x, y, keep_prob):  # 评估准确率
        # 图像 标签 保持率
        params = {self.x: x, self.y_: y, self.keep_prob: 1.0}
        # 传入测试集数据，执行预测并计算准确率
        test_acc = self.sess.run(self.accuracy, params)
        print("Test Accuracy: %f" % test_acc)
        return test_acc


if __name__ == '__main__':
    mnist = FashionMnist("FASHION_MNIST_data/")
    mnist.build()  # 组建CNN
    mnist.train()  # 训练

    print("\t ---------- Test ---------- \n")
    # 读取100个测试集样本
    xs, ys = mnist.data.test.next_batch(100)
    mnist.eval(xs, ys, 1.0)
    mnist.sess.close()
