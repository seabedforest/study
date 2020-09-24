# 一个程序包含多个graph示例
# 创建session时，可以指定执行哪个graph
import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(1.0)
c = tf.add(a, b)
graph = tf.get_default_graph()  # 获取默认graph
print(graph)

# 创建新的graph,并在该graph下创建op
graph2 = tf.Graph()
print(graph2)
with graph2.as_default():  # 指定在graph2上创建op
    d = tf.constant(11)

with tf.Session() as sess:  # 执行默认的graph
    print("执行默认的graph", sess.run(c))
1
with tf.Session(graph=graph2) as sess:  # 执行新创建的graph
    print("执行新创建的graph", sess.run(d))
