# 利用inRange函数，提取指定的颜色
import cv2
import numpy as np

im = cv2.imread("../data/opencv2.png")
cv2.imshow('im', im)
# BGR==> HSV(色相、饱和度、亮度)
im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
####指定蓝色的范围####
# 蓝色H通道值为120，通常取120上下10的范围
minBlue = np.array([110, 50, 50])  # 色相、饱和度、亮度最低值
maxBlue = np.array([130, 255, 255])  # 色相、饱和度、亮度最高值
# inrange返回满足条件的区域
mask = cv2.inRange(im_hsv, minBlue, maxBlue)
cv2.imshow("mask", mask)
blue = cv2.bitwise_and(im, im, mask=mask)
cv2.imshow("blue", blue)

####指定绿色的范围####
minGreen = np.array([50, 50, 50])  # 色相、饱和度、亮度最低值
maxGreen = np.array([70, 255, 255])  # 色相、饱和度、亮度最高值
# inrange返回满足条件的区域
mask = cv2.inRange(im_hsv, minGreen, maxGreen)
cv2.imshow("mask", mask)
green = cv2.bitwise_and(im, im, mask=mask)
cv2.imshow("Green", green)

####指定红色的范围####
minRed = np.array([0, 50, 50])  # 色相、饱和度、亮度最低值
maxRed = np.array([30, 255, 255])  # 色相、饱和度、亮度最高值
# inrange返回满足条件的区域
mask = cv2.inRange(im_hsv, minRed, maxRed)
cv2.imshow("mask", mask)
red = cv2.bitwise_and(im, im, mask=mask)
cv2.imshow("Red", red)

cv2.waitKey()
cv2.destroyAllWindows()
