# 文件读取器
import paddle


def reader_creator(file_path):
    def reader():
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                yield line

    return reader


reader = reader_creator("test.txt")  # 原始读取器
shuffle_reader = paddle.reader.shuffle(reader, 10)  # 随机读取器
batch_reader = paddle.batch(shuffle_reader, 3)  # 批量读取器
# for data in reader():    #reader是生成器函数，可迭代对象
# for data in shuffle_reader():
for data in batch_reader():
    print(data, end="")
