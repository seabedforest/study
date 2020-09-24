# 边沿提取示例
import cv2

im = cv2.imread("../data/lily.png", 0)
cv2.imshow("im", im)

# sobel: 粗糙
# cv2.CV_64F: 输出图像通道数,本来应该设置-1,如果设置成-1可能产生计算问题
im_sobel = cv2.Sobel(im,
                     cv2.CV_64F,
                     1, 1,  # 水平、垂直方向滤波
                     ksize=5)  # 滤波器大小
cv2.imshow("im_sobel", im_sobel)

# Laplacian 算法: 对细节反应更加明显
lap = cv2.Laplacian(im, cv2.CV_64F)
cv2.imshow("lap", lap)

# Canny: 去除内部纹理，保留外部
im_canny = cv2.Canny(im,
                     50,  # 滞后阈值
                     240)  # 模糊度
cv2.imshow("im_canny", im_canny)

cv2.waitKey()
cv2.destroyAllWindows()
