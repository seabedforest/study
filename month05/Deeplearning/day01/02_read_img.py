import cv2

# 读取图像
im = cv2.imread("../data/Linus.png", 1)  # 1: 三通道彩色图像 0：单通道的灰度图像

cv2.imshow("Show Img", im)  # 第一个参数： 窗体名称 第二个参数： 图像数据
# 保存图像
cv2.imwrite("Linus_new.png", im)
cv2.waitKey()  # 阻塞函数,等待用户敲击任意按键
cv2.destroyAllWindows()  # 销毁所有创建的窗体
