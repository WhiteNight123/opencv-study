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
