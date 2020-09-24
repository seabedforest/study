#图像缩放
import cv2

im=cv2.imread("../data/Linus.png")
cv2.imshow("im",im)
h,w=im.shape[:2]
dst_size=(200,300) # 缩放目标尺寸，宽200，高300
method=cv2.INTER_NEAREST
resized = cv2.resize(im,dst_size,interpolation=method) # 执行缩放
cv2.imshow("NEAREST",resized)
cv2.waitKey()
cv2.destroyAllWindows()