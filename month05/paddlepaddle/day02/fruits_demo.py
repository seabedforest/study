# 利用深层CNN实现水果分类
# 数据集：爬虫从百度图片搜索结果爬取
# 内容：包含1036张水果图片，共5个类别（苹果288张、香蕉275张、葡萄216张、橙子276张、梨251张）

############################# 预处理部分 ################################
import os

name_dict = {"apple": 0, "banana": 1, "grape": 2, "orange": 3, "pear": 4}
data_root_path = "data/fruits/"  # 数据样本所在目录
test_file_path = data_root_path + "test.txt"  # 测试文件路径
train_file_path = data_root_path + "train.txt"  # 训练文件路径
name_data_list = {}  # 记录每个类别有哪些图片  key:水果名称  value:图片路径构成的列表


# 将图片路径存入name_data_list字典中
def save_train_test_file(path, name):
    if name not in name_data_list:  # 该类别水果不在字典中，则新建一个列表插入字典
        img_list = []
        img_list.append(path)  # 将图片路径存入列表
        name_data_list[name] = img_list  # 将图片列表插入字典
    else:  # 该类别水果在字典中，直接添加到列表
        name_data_list[name].append(path)


# 遍历数据集下面每个子目录，将图片路径写入上面的字典
dirs = os.listdir(data_root_path)  # 列出数据集目下所有的文件和子目录
for d in dirs:
    full_path = data_root_path + d  # 拼完整路径

    if os.path.isdir(full_path):  # 是一个子目录
        imgs = os.listdir(full_path)  # 列出子目录中所有的文件
        for img in imgs:
            save_train_test_file(full_path + "/" + img,  # 拼图片完整路径
                                 d)  # 以子目录名称作为类别名称
    else:  # 是文件
        pass

# 将name_data_list字典中的内容写入文件
## 清空训练集和测试集文件
with open(test_file_path, 'w') as f:
    pass

with open(train_file_path, 'w') as f:
    pass

# 遍历字典，将字典中的内容写入训练集和测试集
for name,img_list in name_data_list.items():
    i = 0
    num = len(img_list) # 获取每个类别图片数量
    print("%s: %d张" % (name,num))
    # 写训练集和测试集
    for img in img_list:
        if i % 10 == 0: # 每10笔写一笔测试集
            with open(test_file_path,'a') as f:
                line = "%s\t%d\n" % (img,name_dict[name])
                f.write(line)
        else:  # 训练集
            with open(train_file_path,"a") as f:
                line = "%s\t%d\n" % (img,name_dict[name])
                f.write(line)
        i += 1

print("数据预处理完成.")