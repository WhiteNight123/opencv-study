# 视觉第四次作业




## Level1

**H1**
167,168,169,168,165,164,167,170,171
167,168,169,168,166,165,167,170,171
168,169,169,168,167,167,167,169,171
169,168,168,167,167,167,167,168,171
169,168,167,167,167,167,168,168,171
168,167,166,166,166,167,167,167,170
167,165,164,164,167,167,165,164,168
167,164,164,164,165,166,165,164,167
161,162,164,166,167,166,165,164,169

**H11**
168,168,168,168,166,166,167,169,170
168,168,168,168,166,166,167,169,170
168,168,168,168,167,167,167,169,170
168,168,168,167,167,167,168,169,169
168,168,167,167,167,167,167,169,169
167,167,166,166,166,167,167,168,167
166,166,165,165,166,166,166,166,166
164,164,164,165,166,166,165,166,165
164,164,164,165,165,166,165,166,165

**H2**
176,166,178,168,155,164,174,165,182
163,228,168,164,188,163,175,165,164
154,181,160,161,163,151,154,176,178
160,164,180,151,228,166,180,160,170
160,169,225,178,149,165,161,171,166
168,235,152,161,166,172,156,180,168
161,165,182,152,194,151,159,164,161
173,160,174,157,156,176,165,163,167
172,172,160,182,157,165,170,157,175

**H21**
194,182,181,171,169,172,168,170,167
183,175,175,167,164,165,165,170,171
180,173,173,174,171,174,166,169,168
167,173,174,177,168,169,165,168,170
180,179,179,177,171,171,168,168,170
181,180,180,173,165,164,164,165,169
180,174,171,166,165,166,165,165,168
167,169,167,168,166,166,163,165,163
167,169,166,164,165,165,167,166,164

<img src="https://s2.loli.net/2022/05/26/Ii3qWFMtmwRf8Bh.png" alt="opencv4demo1" style="zoom:33%;" />

变化原理:中间的像素值为周围8个像素的平均值

## Level2

<img src="https://s2.loli.net/2022/05/26/ZJvl9fgUbsyEwSp.png" alt="opencv4demo2" style="zoom:33%;" />

## Level3

<img src="https://s2.loli.net/2022/05/26/Edym6UPNSX4KwA2.png" alt="opencv4demo3" style="zoom:33%;" />

均值滤波使图像变得模糊,高斯滤波对原图修改较少

![opencv4demo4](https://s2.loli.net/2022/05/26/84bK1LOi29ovxhH.png)

中值滤波取位于中间的灰度值来代替该点的灰度值,图像平滑里中值滤波的效果最好

## 源代码

```python
import cv2
from matplotlib import pyplot as plt
from numpy import array


def level1(src1, src2):
    print(src1[0:9, 0:9])
    print(src2[0:9, 0:9])
    G11 = cv2.blur(src1, (3, 3))
    G21 = cv2.blur(src2, (3, 3))
    cv2.imwrite("G11.png", G11)
    cv2.imwrite("G21.png", G21)
    print(G11[0:9, 0:9])
    print(G21[0:9, 0:9])
    titles = ['P1', 'P2', 'G11', 'G21']
    images = [src1, src2, G11, G21]
    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def level2(src1, src2):
    G11 = customFilter(src1, 3)
    G21 = customFilter(src2, 3)
    titles = ['customG11', 'customG21']
    images = [G11, G21]
    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    print(G11)
    print(G21)


def customFilter(Imge, dim):
    im = array(Imge)
    sigema = 0
    # 滤波求和
    for i in range(int(dim / 2), im.shape[0] - int(dim / 2)):
        for j in range(int(dim / 2), im.shape[1] - int(dim / 2)):
            for a in range(-int(dim / 2), -int(dim / 2) + dim):
                for b in range(-int(dim / 2), -int(dim / 2) + dim):
                    sigema = sigema + im[i + a, j + b]
            im[i, j] = sigema / (dim * dim)
            sigema = 0
    return im


def level3(src1, src2):
    G12 = cv2.GaussianBlur(src1, (3, 3), 0)
    cv2.imwrite("G12.png", G12)
    titles = ['G11', 'G12']
    images = [cv2.imread('G12.png'), G12]
    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    G22 = cv2.GaussianBlur(src2, (3, 3), 0)
    G23 = cv2.medianBlur(src2, 3)
    titles = ['G22', 'G23']
    images = [G22, G23]
    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    G1 = cv2.imread("lenna.png", 0)
    G2 = cv2.imread("lenna_noise.png", 0)
    level1(G1, G2)
    level2(G1, G2)
    level3(G1, G2)

```

