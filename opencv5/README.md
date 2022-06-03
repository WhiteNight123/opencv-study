# 视觉第五次作业



## Level1

<img src="https://s2.loli.net/2022/05/30/vTLOkQyjN3Fn9Da.png" alt="opencv5demo1" style="zoom:33%;" />

X方向模板对垂直边缘影响最大，Y方向模板对水平边缘影响最大。Sobel算子是一阶导数的**边缘检测**算子,能很好的**消除噪声**的影响.

对A的X方向
[[ 0  0 20 20  0  0]
 [ 0  0 20 20  0  0]
 [ 0  0 15 15  0  0]
 [ 0  0  5  5  0  0]
 [ 0  0  0  0  0  0]
 [ 0  0  0  0  0  0]]

对A的Y方向
[[  0   0   0   0   0   0]
 [  0   0   0   0   0   0]
 [  0   0  -5 -15 -20 -20]
 [  0   0  -5 -15 -20 -20]
 [  0   0   0   0   0   0]
 [  0   0   0   0   0   0]]

```python
def level1(src1, src2):
    G11 = cv2.Sobel(src1, cv2.CV_16S, 1, 0)
    G12 = cv2.Sobel(src1, cv2.CV_16S, 0, 1)
    absX = cv2.convertScaleAbs(G11)
    absY = cv2.convertScaleAbs(G12)
    cv2.imshow("absX", absX)
    cv2.imshow("absY", absY)
    cv2.waitKey(0)
    A1 = cv2.Sobel(src2, cv2.CV_16S, 1, 0)
    A2 = cv2.Sobel(src2, cv2.CV_16S, 0, 1)
    print(A1)
    print(A2)
```



## Level2

<img src="https://s2.loli.net/2022/05/30/2b6DTWQAHPMwXGv.png" alt="opencv5demo2" style="zoom:33%;" />

```python
def level2(src1, src2):
    G2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
    cv2.imshow("G2", G2)
    cv2.waitKey(0)
```



## Level3

<img src="https://s2.loli.net/2022/05/30/WKZcopqdG2Ms6Ck.png" alt="opencv5demo3" style="zoom:33%;" />

**Sobel算子原理**:

计算公式为:
$$
\begin{array}{l}
g_{x}=\frac{\partial f}{\partial x}=\left(z_{7}+2 z_{8}+z_{9}\right)-\left(z_{1}+2 z_{2}+z_{3}\right) \\
g_{y}=\frac{\partial f}{\partial y}=\left(z_{3}+2 z_{6}+z_{9}\right)-\left(z_{1}+2 z_{4}+z_{7}\right)
\end{array}
$$


水平边沿横向模板:

$$
\mathbf{G}_{x}=\left[\begin{array}{ccc}
-1 & 0 & +1 \\
-2 & 0 & +2 \\
-1 & 0 & +1
\end{array}\right]
$$

垂直边缘纵向模板:


$$
\mathbf{G}_{y}=\left[\begin{array}{ccc}
-1 & -2 & -1 \\
0 & 0 & 0 \\
+1 & +2 & +1
\end{array}\right]
$$

**Laplacian算子原理:**

拉普拉斯算子是**二阶**微分算子，常用于**图像增强领域**和边缘提取，它通过灰度差分计算领域内的像素。

通过拉普拉斯模板求二阶导数:
$$
\begin{aligned}
\nabla^{2} f(x, y) &=\frac{\partial^{2} f}{\partial x^{2}}+\frac{\partial^{2} f}{\partial y^{2}} \\
&=\{f(x+1, y)+f(x-1, y)-2 f(x, y)\}+\{f(x, y+1)+f(x, y-1)-2 f(x, y)\}
\end{aligned}
$$
四邻域模板如公式:
$$
\left[\begin{array}{ccc}
0 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & 0
\end{array}\right]
$$
拉普拉斯锐化的方法:
$$
g(x, y)=\left\{\begin{array}{l}
f(x, y)-\nabla^{2} f(x, y)   &\text{掩模中心为正}\\
f(x, y)+\nabla^{2} f(x, y)   &\text{掩模中心为正}
\end{array}\right.
$$
拉普拉斯只适用于**无噪声**图象

```python
def level3(src):
    G13 = cv2.Laplacian(src, cv2.CV_16S, ksize=3)
    Laplacian = cv2.convertScaleAbs(G13)
    cv2.imshow("G13", Laplacian)
    cv2.waitKey(0)
```



## 源代码

```python
import cv2
import numpy
import numpy as np


def level1(src1, src2):
    G11 = cv2.Sobel(src1, cv2.CV_16S, 1, 0)
    G12 = cv2.Sobel(src1, cv2.CV_16S, 0, 1)
    absX = cv2.convertScaleAbs(G11)
    absY = cv2.convertScaleAbs(G12)
    cv2.imshow("absX", absX)
    cv2.imshow("absY", absY)
    cv2.waitKey(0)
    A1 = cv2.Sobel(src2, cv2.CV_16S, 1, 0)
    A2 = cv2.Sobel(src2, cv2.CV_16S, 0, 1)
    print(A1)
    print(A2)
    return absX, absY


def level2(src1, src2):
    G2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
    cv2.imshow("G2", G2)
    cv2.waitKey(0)


def level3(src):
    G13 = cv2.Laplacian(src, cv2.CV_16S, ksize=3)
    Laplacian = cv2.convertScaleAbs(G13)
    cv2.imshow("G13", Laplacian)
    cv2.waitKey(0)


if __name__ == '__main__':
    G1 = cv2.imread("P1.png", 0)
    A = numpy.array([
        [5, 5, 5, 10, 10, 10],
        [5, 5, 5, 10, 10, 10],
        [5, 5, 5, 10, 10, 10],
        [5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5]], dtype=np.uint8)
    G11, G12 = level1(G1, A)
    level2(G11, G12)
    level3(G1)

```

