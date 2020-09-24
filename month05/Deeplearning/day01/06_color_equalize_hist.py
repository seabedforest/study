# 彩色图像直方图均衡化
import cv2

im = cv2.imread("../data/sunrise.jpg", 1)
cv2.imshow("orig", im)

yuv = cv2.cvtColor(im, cv2.COLOR_BGR2YUV)
#取出亮度通道，执行均衡化，将均衡化后的值覆盖原来的亮度通道
yuv[..., 0] = cv2.equalizeHist(yuv[..., 0])

#将YUV色彩表示图像转换会BGR，用以显示
equalized_color=cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)
cv2.imshow('equ',equalized_color)

cv2.waitKey()
cv2.destroyAllWindows()
