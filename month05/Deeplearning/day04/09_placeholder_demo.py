# 占位符的使用
import tensorflow as tf

plhd = tf.placeholder(tf.float32,
                      [2, 3])  # 形状 2行3列

plhd2 = tf.placeholder(tf.float32, [None, 3])  # 形状N行3列

with tf.Session() as sess:
    d = [[1, 2, 3],
         [4, 5, 6]]
    print(sess.run(plhd, feed_dict={plhd: d}))
    print(sess.run(plhd2, feed_dict={plhd2: d}))
