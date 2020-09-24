#透视变换
import cv2
import numpy as np

img = cv2.imread("../data/pers.png")
rows,cols=img.shape[:2]
print(rows,cols)

pts1=np.float32([[58,2],[167,9],[8,196],[126,196]]) # 输入图像四个顶点坐标
pts2=np.float32([[16,2],[167,8],[8,196],[169,196]]) # 输出图像四个顶点坐标

#生成透视变换矩阵
M =cv2.getPerspectiveTransform(pts1,pts2)

print(img.shape)
print(M.shape)

# 执行透视变换，返回变换后的图像
dst = cv2.warpPerspective(img, # 原始图像
                          M, # 3*3的变换矩阵
                          (cols, rows)) # 输出图像大小

#生成透视变换矩阵
M =cv2.getPerspectiveTransform(pts2,pts1)
print(M.shape)
# 执行透视变换，返回变换后的图像
dst2=cv2.warpPerspective(img,M,(cols,rows))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)

cv2.waitKey()
cv2.destroyAllWindows()