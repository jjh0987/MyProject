import sys

import cv2
import matplotlib.pyplot as plt
print(cv2.__version__)
path = '../main/big_data/lecture/week9/data/cat.bmp'
img = cv2.imread(path)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

cv2.imread(path,cv2.IMREAD_COLOR).shape
cv2.imread(path,cv2.IMREAD_GRAYSCALE).shape
cv2.imread(path,cv2.IMREAD_ANYCOLOR).shape
cv2.imread(path,cv2.IMREAD_UNCHANGED).shape
cv2.imread(path,cv2.IMREAD_LOAD_GDAL).shape

plt.imshow(cv2.imread(path,cv2.IMREAD_REDUCED_COLOR_4))
plt.imshow(cv2.imread(path,cv2.IMREAD_REDUCED_GRAYSCALE_8))

img = cv2.imread(path,cv2.IMREAD_COLOR)
img.shape
img.dtype
img.ndim
img[0]

img_copy = img.copy()
img2 = img[40:180,30:150].copy()
plt.imshow(img2)
plt.imshow(cv2.hconcat([img,img_copy]))
#
img_resize = cv2.resize(img,(320,320))
#
img_light = img + 50
img_dark = img - 50
plt.imshow(cv2.hconcat([img,img_light,img_dark]))
img[100][0]
img_light[100][0]

import numpy as np
img_light = np.clip(img.astype('int32') + 50,0,255).astype('uint8')
img_dark = np.clip(img.astype('int32') - 50,0,255).astype('uint8')

height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((width/2,height/2),45,0.5) # 변환행렬
dst = cv2.warpAffine(img,matrix,(width,height))
plt.imshow(dst)

