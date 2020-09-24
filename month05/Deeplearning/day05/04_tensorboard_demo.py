#tensorboard可视化示例
#将数据、图信息写入事件文件

import tensorflow as tf

# 创建普通张量
a=tf.constant([1,2,3,4,5])
# 创建变量
var=tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0),name="var1")
b=tf.constant(3.0,name="a")
c=tf.constant(4.0,name="b")
d=tf.add(b,c,name="add")

# 变量必须显式初始化, 这里定义的是初始化操作，并没有运行
init_op=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    # 将程序图结构写入事件文件
    fw=tf.summary.FileWriter("/home/tarena/summary/",graph=sess.graph)
    print(sess.run([a,var]))