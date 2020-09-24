"""
灰度图像直方图均衡化示例
直方图
"""
import cv2
import numbers as np
from matplotlib import pyplot as plt

im = cv2.imread("../data/sunrise.jpg",0)
cv2.imshow("orig",im)

#直方图均衡化
im_equ=cv2.equalizeHist(im)
cv2.imshow("equl",im_equ)

#绘制灰度直方图
#原始直方图
print(im.ravel())
plt.subplot(2,1,1)
plt.hist(im.ravel(),256,[0,256],label="orig")
plt.legend()

#均衡化处理后的直方图
plt.subplot(2,1,2)
plt.hist(im.ravel(),256,[0,256],label="equalize")
plt.legend()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()