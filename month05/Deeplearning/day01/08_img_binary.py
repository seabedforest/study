# 二值化、反二值化
import cv2

im = cv2.imread("../data/lena.jpg", 0)
cv2.imshow('im', im)

# 二值化
t, rst = cv2.threshold(im,
                       50,  # 阈值
                       255,  # 大于阈值设置成255
                       cv2.THRESH_BINARY)
cv2.imshow('rst', rst)

# 反二值化
t1, rst2 = cv2.threshold(im,
                         50,  # 阈值
                         255,  # 小于阈值设置成255
                         cv2.THRESH_BINARY_INV)
cv2.imshow('rst2', rst2)
print(t1,'xxxxxxxxxxxxxxxx')
cv2.waitKey()
cv2.destroyAllWindows()
