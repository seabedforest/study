# 图像相加示例
import cv2

a = cv2.imread("../data/lena.jpg", 0)
b = cv2.imread("../data/lily_square.png", 0)

dst1 = cv2.add(a, b)  # 图像直接相加，会导致图像过亮、过白

# 加权求和：addWeighted
# 图像进行加权和计算时，要求src1和src2必须大小、类型相同
dst2 = cv2.addWeighted(a, 1, b, 0.4, 0)  # 最后一个参数为亮度调节量
cv2.imshow("a", a)
cv2.imshow("b", b)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()
