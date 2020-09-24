#图像腐蚀示例
import cv2
import numpy as np

im=cv2.imread("../data/5.png")
cv2.imshow("im",im)

kernel = np.ones((3,3),np.uint8) #用于腐蚀计算的核
erosion = cv2.erode(im,
                    kernel,  #腐蚀核
                    iterations=5) #迭代次数，越大腐蚀越厉害

cv2.imshow('erosion',erosion)
cv2.waitKey()
cv2.destroyAllWindows()