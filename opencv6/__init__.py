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
