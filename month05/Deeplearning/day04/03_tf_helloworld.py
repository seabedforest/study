#tensorflow编写helloworld
import tensorflow as tf

#定义常量(张量)
hello = tf.constant("Hello,world!")
sess = tf.Session() #创建Session对象
print(sess.run(hello)) # 执行hello操作并返回值
sess.close()