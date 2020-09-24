import cv2
import numpy as np

im=cv2.imread("../data/3.png")
cv2.imshow("im",im)
#灰度化处理
im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# 二值化处理
ret,im_bin=cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)

#查找轮廓
img,cnts,hie=cv2.findContours(im_bin,
                              cv2.RETR_EXTERNAL, #只检测外轮廓
                              cv2.CHAIN_APPROX_NONE) #存储所有轮廓点
print("type",type(cnts))
for cnt in cnts:
    print(cnt.shape) #打印每个轮廓的形状

#绘制轮廓
im_cnt=cv2.drawContours(im,cnts,
                        -1, #绘制全部轮廓
                        (0,0,255),2) #轮廓颜色，粗细
cv2.imshow("im_cnt",im_cnt)
cv2.waitKey()
cv2.destroyAllWindows()