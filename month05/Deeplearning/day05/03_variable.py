# 变量使用示例
# 变量在使用之前，必须进行初始化
import tensorflow as tf

a = tf.constant([1, 2, 3, 4, 5, 6])  # 普通张量
# 变量
val = tf.random_normal([2, 3], mean=0.0, stddev=1.0)
var = tf.Variable(val, name='var1')

with tf.Session() as sess:
    #初始化
    sess.run(tf.global_variables_initializer())
    print(sess.run([a,var])) #同时执行多个op
