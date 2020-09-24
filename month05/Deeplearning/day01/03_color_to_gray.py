"""
彩色图像转换为灰度图像（灰度化)
"""
import cv2

im = cv2.imread("../data/Linus.png", 1)  # 读取彩色图像
cv2.imshow("im", im)  # 显示

# 彩色图像转灰度图像
im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)  # BGR转灰度图像

cv2.imshow("im_gray", im_gray)

cv2.waitKey()
cv2.destroyAllWindows()
