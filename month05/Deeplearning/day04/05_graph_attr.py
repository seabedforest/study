#查看图以及图的属性
import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(1.0)
c=tf.add(a,b)
#获取默认图
graph=tf.get_default_graph()
print(graph)

with tf.Session() as sess:
    print(sess.run(c))
    print(a.graph)  #通过tensor获取graph属性
    print(c.graph)  #通过op获取graph属性
    print(sess.graph) #通过session获取graph对象