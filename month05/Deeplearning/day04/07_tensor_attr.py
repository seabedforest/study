#打印张量属性
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #调整警告级别
# a=tf.constant(5.0)
# a=tf.constant([1,2,3])
a=tf.constant([[1,2,3],[4,5,6]])
with tf.Session() as sess:
    print(sess.run(a))
    print("name:",a.name)
    print("dtype:",a.dtype)
    print("shape:",a.shape)
    print("op:",a.op)
    print("graph:",a.graph)
