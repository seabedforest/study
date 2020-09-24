# csv文件读取示例
import tensorflow as tf
import os


# csv文件读取函数
def csv_read(filelist):  # 参数为文件列表
    # 2. 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 3. 构建csv reader，读取队列内容（一行）
    reader = tf.TextLineReader()
    ## k:文件名称  v:读取的数据
    k, v = reader.read(file_queue)
    # 4. 对每行内容进行解码
    ## record_defaults：指定每一个样本每一列的类型，指定默认值
    records = [["None"], ["None"]]  # 默认值
    example, label = tf.decode_csv(v,
                                   record_defaults=records)  # 解码失败设置默认值
    # 5. 批处理
    # batch_size: 跟队列大小无关，只决定本批次取多少数据
    example_bat, label_bat = tf.train.batch([example, label],  # 参与批处理的数据
                                            batch_size=4, # 批次大小
                                            num_threads=1) # 线程数量

    return example_bat,label_bat  #返回一个批次数据

if __name__ == '__main__':
    # 列出所有待测试的文件，构建文件列表
    dir_name="./test_data"
    file_names=os.listdir(dir_name)
    file_list=[]  #文件列表

    for f in file_names:
        # 拼接目录+文件名，添加到列表
        file_list.append(os.path.join(dir_name,f))

    example,lable = csv_read(file_list)

    with tf.Session() as sess:
        # 线程协调器，用于对线程管理
        coord=tf.train.Coordinator()
        # 返回一组工作线程
        threads = tf.train.start_queue_runners(sess,coord=coord)

        # 执行文件读取op
        print(sess.run([example, lable]))
        # 回收线程资源
        coord.request_stop() # 请求线程停止
        coord.join(threads) # 等待并回收线程资源
