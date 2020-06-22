"""
拷贝目录
"""
import os
from multiprocessing import Pool

dir_path = "../day12/home_work"
file_list = os.listdir(dir_path)
if not os.path.exists(dir_path.split('/')[-1]):
    new_dir = os.mkdir(dir_path.split('/')[-1])
else:
    new_dir = dir_path.split('/')[-1]


def copy():
    for file in file_list:
        fr = open(dir_path + '/' + file, 'rb')
        fw = open(new_dir + '/' + file, 'wb')
        print(new_dir + '/' + file, "竟在写入")
        while True:
            data = fr.read(1024 * 1024)
            if not data:
                break
            fw.write(data)
        fr.close()
        fw.close()



# 创建进程池
pool = Pool(4)

pool.apply_async(func=copy)

# 关闭进程池
pool.close()

# 阻塞等待回收进程池中的进程
pool.join()
