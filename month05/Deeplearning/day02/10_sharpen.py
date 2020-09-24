# 图像锐化示例
#放大像素之间的差异性
import cv2
import numpy as np

im = cv2.imread("../data/lena.jpg", 0)
cv2.imshow("im", im)

# 锐化算子1
sharpen1 = np.array([[-1, -1, -1],
                     [-1, 9, -1],
                     [-1, -1, -1]])

im_sharpen1 = cv2.filter2D(im,
                           -1,  # 所有通道
                           sharpen1)  # 滤波器
cv2.imshow("im_sharpen1", im_sharpen1)


# 锐化算子1
sharpen2 = np.array([[0, -1, 0],
                     [-1, 8, -1],
                     [0, 1, 0]]) / 5.0

im_sharpen2 = cv2.filter2D(im,
                           -1,  # 所有通道
                           sharpen2)  # 滤波器
cv2.imshow("im_sharpen2", im_sharpen2)

cv2.waitKey()
cv2.destroyAllWindows()