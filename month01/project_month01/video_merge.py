"""
现在有两个视频文件（自己指定），编写一个程序，将两个视频文件合并为一个
@author hailin
@date 2020-05-31
"""


def merge_video_contents(video01, video02, newvideo):
    """
    将两个视频文件合并为一个视频文件
    :param video01: 要被合并的视频1
    :param video02: 要被合并的视频2
    :param newvideo: 合并成的新视频
    :return: None
    """
    fr01 = open(video01,'rb')
    fr02 = open(video02,'rb')
    fw = open(newvideo, 'wb+')
    while True:
        data = fr01.read(1024 * 1024)
        if not data:
            break
        fw.write(data)

    while True:
        data = fr02.read(1024 * 1024)
        if not data:
            break
        fw.write(data)

    fr01.close()
    fr02.close()
    fw.close()


if __name__ == '__main__':
    video01 = input("输入要被合并的视频1路径:")
    video02 = input("输入要被合并的视频2路径:")
    newvideo = input("输入合并后视频所存储的路径:")
    merge_video_contents(video01, video02, newvideo)
