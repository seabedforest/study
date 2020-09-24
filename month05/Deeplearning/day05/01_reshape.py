"""
张量静态形状、动态形状示例
"""
import tensorflow as tf

pld=tf.placeholder(tf.float32,[None,3])  #N行3列
print(pld)
pld.set_shape([4,3])  #设置静态形状
print(pld,'xxxxxx')
# pld.set_shape([3,3])  #报错，静态形状一旦固定就不能再设置静态形状
#动态形状
new_pld=tf.reshape(pld,[3,4])
print(new_pld)
new_pld=tf.reshape(pld,[2,6])
print(new_pld)
# new_pld=tf.reshape(pld,[2,4])  # 报错，元素的数量不匹配

with tf.Session() as sess:
    pass