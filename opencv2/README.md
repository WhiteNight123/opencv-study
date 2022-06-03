# 视觉第二次作业




## Level1

### I

直接用255减

```python
img_reverse = 255 - img
```

### II

变亮30%,灰度值*1.3,若超过了255,就直接赋值255



```python
for i in range(height):
    for j in range(width):
        if src[i][j] * 1.3 > 255:
            img_bright[i][j] = 255
        else:
            img_bright[i][j] += src[i][j] * 0.3
```

### III

变暗30%,灰度值*0.7

```python
for i in range(height):
	for j in range(width):
		img_dark[i][j] -= src[i][j] * 0.3
```



## Level2

### I

与Level1的I一致

### II

对<100的加20,对大于150的减20,其余设为125

```python
for i in range(height):
    for j in range(width):
        if src[i][j] < 100:
            img_custom[i][j] = src[i][j] + 20
        elif src[i][j] > 150:
            img_custom[i][j] = src[i][j] - 20
        else:
            img_custom[i][j] = 125
```



## Level3

### I

提取BGR颜色

```python
(img_blue, img_green, img_red) = cv.split(src)
```



### II

红色通道+20,绿色通道-20

```python
img_red += 20
img_green -= 20
img_reverse = cv.merge([img_blue, img_green, img_red])
```



### III

对数变换  **s=clog(1+r)**

**normalize**把范围变换到[0,255]

```python
# 对数变化
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
height, width = img_gray.shape
img_log = img_gray
for i in range(height):
    for j in range(width):
        img_log[i, j] = 1.0 * (math.log(1.0 + img_gray[i, j]))
img_log = cv.normalize(img_log, img_log, 0, 255, cv.NORM_MINMAX)
```



### IV

伽马变换 **s=cr^γ**

```python
img_gamma = img_gray
for i in range(height):
    for j in range(width):
        img_gamma[i][j] = 1 * math.pow(img_gray[i, j], 2.5)
cv.normalize(img_gamma, img_gamma, 0, 255, cv.NORM_MINMAX)
```





## 效果图

![image-20220512151041208](https://gitee.com/heihun666/picture/raw/master/pictures/opencv_demo2.png)

## 全部代码

```python
import math
import cv2 as cv


def level1(src):
    height, width = src.shape
    img_reverse = 255 - src
    cv.imshow('img_reverse', img_reverse)
    cv.waitKey(0)
    img_bright = src
    img_dark = src
    for i in range(height):
        for j in range(width):
            if src[i][j] * 1.3 > 255:
                img_bright[i][j] = 255
            else:
                img_bright[i][j] += src[i][j] * 0.3
    cv.imshow('img_bright', img_bright)
    cv.waitKey(0)

    for i in range(height):
        for j in range(width):
            img_dark[i][j] -= src[i][j] * 0.3
    cv.imshow('img_dark', img_dark)
    cv.waitKey(0)


def level2(src):
    height, width = src.shape
    img_reverse = 255 - src
    img_custom = src
    for i in range(height):
        for j in range(width):
            if src[i][j] < 100:
                img_custom[i][j] = src[i][j] + 20
            elif src[i][j] > 150:
                img_custom[i][j] = src[i][j] - 20
            else:
                img_custom[i][j] = 125
    cv.imshow('img_custom', img_custom)
    cv.waitKey(0)


def level3(src):
    (img_blue, img_green, img_red) = cv.split(src)
    img_red += 20
    img_green -= 20
    img_reverse = cv.merge([img_blue, img_green, img_red])
    cv.imshow('img_reverse2', img_reverse)
    cv.waitKey(0)
    # 对数变化
    img_gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    height, width = img_gray.shape
    img_log = img_gray
    for i in range(height):
        for j in range(width):
            img_log[i, j] = 1.0 * (math.log(1.0 + img_gray[i, j]))
    img_log = cv.normalize(img_log, img_log, 0, 255, cv.NORM_MINMAX)
    cv.imshow('img_log', img_log)
    cv.waitKey(0)
    # 伽马变化
    img_gamma = img_gray
    for i in range(height):
        for j in range(width):
            img_gamma[i][j] = 1 * math.pow(img_gray[i, j], 2.5)
    cv.normalize(img_gamma, img_gamma, 0, 255, cv.NORM_MINMAX)
    cv.imshow('img_gamma', img_gamma)
    cv.waitKey(0)


if __name__ == '__main__':
    img = cv.imread('lenna.png')
    level1(cv.cvtColor(img, cv.COLOR_RGB2GRAY))
    level2(cv.cvtColor(img, cv.COLOR_RGB2GRAY))
    level3(img)

```

