# 张量相加
import tensorflow as tf

a = tf.constant(5.0)  # 常量a(张量)
b = tf.constant(1.0)  # 常量b(张量)
c = tf.add(a, b)
with tf.Session() as sess:
    print(sess.run(c))  #真正执行c操作

