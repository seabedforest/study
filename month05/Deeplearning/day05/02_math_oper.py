# 张量数学计算

import tensorflow as tf

x = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
y = tf.constant([[4, 3], [3, 2]], dtype=tf.float32)

x_add_y = tf.add(x, y)  # 张量相加
x_mul_y = tf.matmul(x, y)  # 张量相乘
log_x = tf.log(x)  # log(x)
data = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=tf.float32)
segment_ids = tf.constant([0, 0, 0, 1, 1, 2, 2, 2, 2, 2], dtype=tf.int32)
x_seg_sum = tf.segment_sum(data, segment_ids)  # [6,9,40]
with tf.Session() as sess:
    print(x_add_y.eval())
    print(x_mul_y.eval())
    print(log_x.eval())
    print(x_seg_sum.eval())
