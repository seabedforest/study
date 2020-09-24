#创建张量
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #调整警告级别
#创建值全为0的张量
tensor_zeros = tf.zeros(shape=[2,3],
                        dtype="float32")

#创建值全为1的张量
tensor_ones=tf.ones(shape=[3,4],
                    dtype="float32")
#创建正态分布张量
tensor_nd=tf.random_normal(shape=[10],
                           mean=1.7,
                           stddev=0.2,
                           dtype="float32")

#生成和另一个张量形状相同的张量,值全为0
tensoor_zeros_like=tf.zeros_like(tensor_zeros)
with tf.Session() as sess:
    # eval表示在session中执行该张量(简化写法)
    print(tensor_zeros.eval())
    print(tensor_ones.eval())
    print(tensor_nd.eval())
    print(tensoor_zeros_like.eval())