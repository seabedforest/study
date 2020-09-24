# 图像校正示例
import cv2
import numpy as np

im = cv2.imread("../data/paper.jpg")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("im", im)

# 模糊
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# 膨胀
dilate = cv2.dilate(blurred,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)))
edged=cv2.Canny(dilate,30,120,3)
# cv2.imshow("edged",edged)
# 轮廓检测
cnts=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,
                      cv2.CHAIN_APPROX_SIMPLE)
cnts=cnts[1]
docCnt=None
# 绘制轮廓
im_cnt=cv2.drawContours(im,cnts,-1,(0,0,255),2)
cv2.imshow("im_cnt",im_cnt)
# 计算轮廓面积，并排序
if len(cnts) >0:
    cnts=sorted(cnts,key=cv2.contourArea,reverse=True)
    for c in cnts:
        peri=cv2.arcLength(c,True) # 计算轮廓周长
        approx = cv2.approxPolyDP(c,0.02*peri,True) # 轮廓多边形拟合
        # 轮廓为4个点表示找到纸张
        if len(approx) == 4:
            docCnt = approx
            break
print(docCnt)

# 用圆圈标记处角点
points=[]
for peak in docCnt:
    peak = peak[0]
    # 绘制圆
    cv2.circle(im,  # 绘制图像
               tuple(peak), 10,  # 圆心、半径
               (0, 0, 255), 2)  # 颜色、粗细
    points.append(peak)
print(points)
cv2.imshow("im_point",im)

# 校正
src=np.float32([points[0],points[1],points[2],points[3]]) # 原来逆时针方向四个点
dst=np.float32([[0,0],[0,488],[337,488],[337,0]]) # 对应变换后逆时针方向四个点
m=cv2.getPerspectiveTransform(src,dst) # 生成透视变换矩阵
result=cv2.warpPerspective(gray.copy(),m,(337,488)) # 透视变换
cv2.imshow("result",result) # 显示透视变换结果
cv2.waitKey()
cv2.destroyAllWindows()