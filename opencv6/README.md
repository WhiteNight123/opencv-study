# 视觉第六次作业

<center>郭晓强 2021214229 python


## Level1

![opencv6Demo1](https://s2.loli.net/2022/06/06/fLJCiYBKF51vc6b.png)

- F1

$$
\begin{array}{l}
x_{0}=x+\text { width } / 2 \\
y_{0}=y+\text { height } / 2
\end{array}
$$

- F2
  $$
  \begin{array}{l}
  x_{0}=\frac{1}{2} \times \text { width } \\
  y_{0}=\frac{1}{2} \times \text { height }
  \end{array}
  $$

- F3
  $$
  \left\{\begin{array}{l}
  x=r \cos \left(\alpha+45^{\circ}\right)=r \cos \alpha \cos 45^{\circ}-r \sin \alpha \sin 45^{\circ}=x_{0} \cos 45^{\circ}-y_{0} \sin 45^{\circ} \\
  y=r \sin \left(\alpha+45^{\circ}\right)=r \sin \alpha \cos 45^{\circ}+r \cos \alpha \sin 45^{\circ}=x_{0} \sin 45^{\circ}+y_{0} \cos 45^{\circ}
  \end{array}\right.
  $$

- 向前映射

  从原图像计算该像素在变换后图像的坐标位置,向前映射会出现:映射不完全，映射重叠的问题

- 向后映射

  变换后图像的任意像素在原图像的坐标位置,**向后映射**用的比较多

- 插值

  插值算法就是用来处理**浮点数**坐标的

  - 最邻近插值

    最近点插值就相当于四舍五入取整
    
  - 双线性插值
  
    先在x方向上进行两次线性插值：
    $$
    \begin{array}{l}
    f\left(x, y_{0}\right)=\frac{x_{1}-x}{x_{1}-x_{0}} f\left(x_{0}, y_{0}\right)+\frac{x-x_{0}}{x_{1}-x_{0}} f\left(x_{1}, y_{0}\right) \\
    f\left(x, y_{1}\right)=\frac{x_{1}-x}{x_{1}-x_{0}} f\left(x_{0}, y_{1}\right)+\frac{x-x_{0}}{x_{1}-x_{0}} f\left(x_{1}, y_{1}\right)
    \end{array}
    $$
    再在y方向上进行一次线性插值：
    $$
    f(x, y)=\frac{y_{1}-y}{y_{1}-y_{0}} f\left(x, y_{0}\right)+\frac{y-y_{0}}{y_{1}-y_{0}} f\left(x, y_{1}\right)
    $$



```python
def level1(src):
    height, width = src.shape
    M11 = np.float32([[1, 0, width / 2], [0, 1, height / 2]])
    G11 = cv2.warpAffine(src, M11, (width, height))
    cv2.imshow("G11", G11)
    cv2.waitKey(0)
    G12 = cv2.resize(src, None, fx=0.5, fy=0.5)
    cv2.imshow("G12", G12)
    cv2.waitKey(0)
    M13 = cv2.getRotationMatrix2D((0, 0), 45, 1)
    G13 = cv2.warpAffine(src, M13, (width, height))
    cv2.imshow("G13", G13)
    cv2.waitKey(0)
```



## Level2

<img src="https://s2.loli.net/2022/06/06/EUehWMyjiTzxBSk.png" alt="opencv6Demo2" style="zoom:33%;" />

- F4

  先坐标转换到**旋转中心**,再旋转
  $$
  \begin{array}{l}
  \text { 设 } d x=-0.5 W^{\prime} \cos \theta-0.5 H^{\prime} \sin \theta+0.5 W \\
  \text { 设 } d y=0.5 W^{\prime} \sin \theta-0.5 H^{\prime} \cos \theta+0.5 H \\
  \end{array}
  $$
  W'和H'表示转换后的宽和高
  $$
  \begin{array}{l}
  x_{0}=x \cos \theta+x \sin \theta+d x \\
  y_{0}=-y \sin \theta+y \cos \theta+d y
  \end{array}
  $$
  

```python
def level2(src):
    height, width = src.shape
    M21 = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
    G21 = cv2.warpAffine(src, M21, (width, height))
    cv2.imshow("G21", G21)
    cv2.waitKey(0)
```



## Level3

<img src="https://s2.loli.net/2022/06/06/IoCHBvWFkfU6l9i.png" alt="opencv6Demo3" style="zoom:33%;" />



- F5

  先**放缩**,再**旋转**
  $$
  \begin{array}{l}
  x_{0}=\frac{\sqrt{2}}{2} \times \text { width } \\
  y_{0}=\frac{\sqrt{2}}{2} \times \text { height }
  \end{array}
  $$
  
  $$
  \begin{array}{l}
  x_{0}=x \cos \theta+x \sin \theta+d x \\
  y_{0}=-y \sin \theta+y \cos \theta+d y
  \end{array}
  $$
  
  

```python
def level3(src):
    height, width = src.shape
    M3 = cv2.getRotationMatrix2D((width / 2, height / 2), -45, math.sqrt(2) / 2)
    G3 = cv2.warpAffine(src, M3, (width, height))
    cv2.imshow("G3", G3)
    cv2.waitKey(0)

```

## 源代码

```python
import math

import cv2
import numpy as np


def level1(src):
    height, width = src.shape
    M11 = np.float32([[1, 0, width / 2], [0, 1, height / 2]])
    G11 = cv2.warpAffine(src, M11, (width, height))
    cv2.imshow("G11", G11)
    cv2.waitKey(0)
    G12 = cv2.resize(src, None, fx=0.5, fy=0.5)
    cv2.imshow("G12", G12)
    cv2.waitKey(0)
    M13 = cv2.getRotationMatrix2D((0, 0), 45, 1)
    G13 = cv2.warpAffine(src, M13, (width, height))
    cv2.imshow("G13", G13)
    cv2.waitKey(0)


def level2(src):
    height, width = src.shape
    M21 = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
    G21 = cv2.warpAffine(src, M21, (width, height))
    cv2.imshow("G21", G21)
    cv2.waitKey(0)


def level3(src):
    height, width = src.shape
    M3 = cv2.getRotationMatrix2D((width / 2, height / 2), -45, math.sqrt(2) / 2)
    G3 = cv2.warpAffine(src, M3, (width, height))
    cv2.imshow("G3", G3)
    cv2.waitKey(0)


if __name__ == '__main__':
    G1 = cv2.imread("img.png", 0)
    level1(G1)
    level2(G1)
    level3(G1)

```

