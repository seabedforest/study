# 针对图像某个通道进行操作
import cv2
import numpy as np

im = cv2.imread("../data/opencv2.png")  # 默认读取彩色图像
cv2.imshow("im", im)
# 取出蓝色通道,当做单通道图像显示（系统会认为这是灰度图像)
b = im[:, :, 0]  # 取出索引为0的通道(B通道)
cv2.imshow("blue-channel", b)
# # 抹掉蓝色通道
# im[:, :, 0] = 0  # 取出B通道,将值赋为0（蓝色通道没有值)
# cv2.imshow("im-b0",im)
#抹掉绿色通道
im[:,:,1] = 0 # 取出G通道,将值赋为0（绿色通道没有值)
cv2.imshow("im-g0",im)
cv2.waitKey()
cv2.destroyAllWindows()
