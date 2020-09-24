#图像仿射变换
#仿射变换：旋转、平移，不改变图像平直性,垂直性
import cv2
import numpy as np

def translate(img,x,y):
    """
    图像平移变换
    :param img: 原始图像数据
    :param x:  水平方向平移像素
    :param y:  垂直方向平移像素
    :return:  经过平移后的图像
    """
    print(img.shape)
    h,w=img.shape[:2]
    #定义平移矩阵
    M = np.float32([[1,0,x],
                    [0,1,y]])
    #warpAffine实现仿射变换
    shifted=cv2.warpAffine(img,M,(w,h)) # 第三个参数为输出图像尺寸
    return  shifted #返回平移后的图像

def rotate(img,angle,center=None,scale=1.0):
    """
    图像旋转变换
    :param img: 原始图像数据
    :param angle: 旋转角度
    :param center: 旋转中心，如果为None则以原图中心为旋转中心
    :param scale: 缩放比例，默认为1
    :return: 返回旋转后的图像
    """
    h,w=img.shape[:2]
    #旋转中心默认为图像中心
    if center is None:
        center = (w/2,h/2)

    # 计算旋转矩阵
    M=cv2.getRotationMatrix2D(center,angle,scale)

    #使用openCV仿射变换实现函数旋转
    rotated=cv2.warpAffine(img,M,(w,h))
    return rotated

if __name__ == '__main__':
    # 读取并显示原始图像
    im=cv2.imread("../data/Linus.png")
    cv2.imshow("SrcImg",im)

    #图像向下移动50像素
    shifted= translate(im,0,50,)
    cv2.imshow("shifted1",shifted)

    # 图像向左移动40, 下移动40像素
    shifted2=translate(im,-40,40)
    cv2.imshow("shifted2",shifted2)

    #逆时针旋转45度
    rotated1=rotate(im,45)
    cv2.imshow("rotated1",rotated1)
    
    #顺时针旋转90度
    rotated2=rotate(im,-90)
    cv2.imshow("rotated2",rotated2)

    cv2.waitKey()
    cv2.destroyAllWindows()