# 图像样本读取示例
import tensorflow as tf
import os

# 读取图像样本函数
def img_read(filelist):
    # 构建文件队列
    file_queue=tf.train.string_input_producer(filelist)
    # 创建reader， 读取内容
    reader=tf.WholeFileReader()
    k,v = reader.read(file_queue)
    # 解码
    img=tf.image.decode_jpeg(v)
    # 批处理, 图片要求设置成统一大小
    img_resized = tf.image.resize(img,[200,200])
    # 设置样本的固定形状
    img_resized.set_shape([200,200,3])
    # 批处理
    img_bat=tf.train.batch([img_resized],batch_size=10,num_threads=1)
    return img_bat

if __name__ == '__main__':
    # 列出所有待测试的文件，构建文件列表
    dir_name="./test_img/"
    file_names=os.listdir(dir_name)
    file_list=[]  #文件列表

    for f in file_names:
        # 拼接目录+文件名，添加到列表
        file_list.append(os.path.join(dir_name,f))

    imgs=img_read(file_list)

    with tf.Session() as sess:
        # 线程协调器，用于对线程管理
        coord=tf.train.Coordinator()
        # 返回一组工作线程
        threads = tf.train.start_queue_runners(sess,coord=coord)

        # 执行文件读取op
        imgs_data=imgs.eval()

        # 回收线程资源
        coord.request_stop() # 请求线程停止
        coord.join(threads)  # 等待并回收线程资源

# 图像显示
import matplotlib.pyplot as plt

plt.figure("ImgShow",facecolor="lightgray")

for i in range(10):     # 循环显示图像
    plt.subplot(2,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgs_data[i].astype("int32"))   #显示第i张图

plt.tight_layout()
plt.show()