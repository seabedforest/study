from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sn

#读取原始图像
im = misc.imread("zebra.png",flatten=True)

fit=np.array([[-1,0,1],
              [-2,0,2],
              [-1,0,1]])

fit2=np.array([[1,2,1],
              [0,0,0],
              [-1,-2,-1]])

conv_img1=signal.convolve2d(im,
                            fit,
                            boundary='symm',
                            mode='same').astype("int32")

conv_img2=signal.convolve2d(im,
                            fit2,
                            boundary='symm',
                            mode='same').astype("int32")

plt.figure("Conv2D")
plt.subplot(131)
plt.xticks([])
plt.yticks([])
plt.imshow(im,cmap='gray') # 显示原始的图

plt.subplot(132)
plt.xticks([])
plt.yticks([])
plt.imshow(conv_img1,cmap='gray') # 卷积后的图

plt.subplot(133)
plt.xticks([])
plt.yticks([])
plt.imshow(conv_img2,cmap='gray') # 卷积后的图


plt.show()
