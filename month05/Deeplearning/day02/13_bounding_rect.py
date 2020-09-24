# 绘制图像矩形轮廓
import cv2
import numpy as np

im = cv2.imread("../data/cloud.png", 0)
cv2.imshow("orig", im)

# 提取图像轮廓
ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
img, contours, hierarchy = cv2.findContours(binary,
                                            cv2.RETR_LIST,  # 不建立等级关系
                                            cv2.CHAIN_APPROX_NONE)  # 存储所有的轮廓点

print("contours[0].shape:", contours[0].shape)

# 返回轮廓定点及边长
x, y, w, h = cv2.boundingRect(contours[0])  # 计算矩形包围框的x,y,w,h
print("x:", x, "y:", y, "w:", w, "h:", h)

# 绘制矩形包围框
brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
cv2.drawContours(im,
                 [brcnt],  # 轮廓点列表
                 -1,  # 绘制全部轮廓
                 (255, 255, 255),  # 轮廓颜色:白色
                 2)  # 轮廓粗细

cv2.imshow("result", im)  # 显示绘制后的图像

cv2.waitKey()
cv2.destroyAllWindows()
