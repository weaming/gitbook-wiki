## 安装 NumPy

    pip install numpy

更多例子：[Tutorial — Pillow (PIL Fork) 2.6.1 documentation](https://pillow.readthedocs.org/en/3.0.0/handbook/tutorial.html)

## 安装 opencv（开源计算机视觉）

在Python中，使用OpenCV进行图像处理是通过使用 `cv2` 与 `NumPy` 模块进行的。

Installing OpenCV from prebuilt binaries
Below Python packages are to be downloaded and installed to their default locations.

### 下载

1. [Python-2.7.x](http://python.org/ftp/python/2.7.5/python-2.7.5.msi).
2. [Numpy](http://sourceforge.net/projects/numpy/files/NumPy/1.7.1/numpy-1.7.1-win32-superpack-python2.7.exe/download).
3. [Matplotlib](https://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.3.0/matplotlib-1.3.0.win32-py2.7.exe) (Matplotlib is optional, but recommended since we use it a lot in our tutorials).

### 安装

1. Install all packages into their default locations. Python will be installed to `C:/Python27/`.
2. After installation, open Python IDLE. Enter `import numpy` and make sure Numpy is working fine.
3. Download latest OpenCV release from sourceforge site and double-click to extract it.
4. Goto opencv/build/python/2.7 folder.
5. Copy `cv2.pyd` to `C:/Python27/lib/site-packeges`.
6. Open `Python IDLE` and type following codes in Python terminal.

```
>>> import cv2
>>> print cv2.__version__
```
If the results are printed out without any errors, congratulations !!! You have installed OpenCV-Python successfully.

更多例子：[OpenCV-Python Tutorials](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html)

## Demo

源码：https://github.com/weaming/image-processing

```
from PIL import Image, ImageFilter
import cv2
import numpy as np

print '##### PIL #####'
img = Image.open('images/image.jpg')
img.show()

#过滤图像
im_sharp = img.filter( ImageFilter.SHARPEN )
#保存过滤过的图像到文件中
im_sharp.save( 'images/image_sharpened.jpg', 'JPEG' )

#分解图像到三个RGB不同的通道（band）中。
r,g,b = img.split()
r.save( 'images/image_r.jpg', 'JPEG' )
g.save( 'images/image_g.jpg', 'JPEG' )
b.save( 'images/image_b.jpg', 'JPEG' )

#显示被插入到图像中的EXIF标记
exif_data = img._getexif()
print 'EXIF:', exif_data


print '##### CV2 #####'
#读取图像
img = cv2.imread('images/image.jpg')
#显示图像
cv2.imshow('images/image.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Applying Grayscale filter to image 作用Grayscale（灰度）过滤器到图像上
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#保存过滤过的图像到新文件中
cv2.imwrite('images/graytest.jpg',gray)
```

## 参考链接
- [图像处理 — Python最佳实践指南](http://pythonguidecn.readthedocs.org/zh/latest/scenarios/imaging.html)
- [从opencv.org下载 OpenCV 2.4.13.0](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html)
- [Install OpenCV-Python in Windows](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)