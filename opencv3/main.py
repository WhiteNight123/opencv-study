import math

import cv2
import matplotlib.pyplot as plt
import numpy as np


def show_hist(title, img_ravel):
    plt.hist(img_ravel, 256, [0, 256])
    plt.title(title)
    plt.show()


def level1(src):
    show_hist("H1", src.ravel())
    height, width = src.shape
    img_bright = src.copy()
    for i in range(height):
        for j in range(width):
            if src[i][j] * 2 > 255:
                img_bright[i][j] = 255
            else:
                img_bright[i][j] += src[i][j]
    show_hist("H2", img_bright.ravel())
    img_dark = src.copy()
    for i in range(height):
        for j in range(width):
            img_dark[i][j] -= src[i][j] * 0.5
    show_hist("H3", img_dark.ravel())
    return img_bright, img_dark


def level2(src):
    height, width = src.shape
    img_log = src.copy()
    for i in range(height):
        for j in range(width):
            img_log[i, j] = 1.0 * (math.log(1.0 + src[i, j]))
    img_log = cv2.normalize(img_log, img_log, 0, 255, cv2.NORM_MINMAX)
    show_hist('H4', img_log.ravel())


def level3(img, img_bright, img_dark):
    equ1 = cv2.equalizeHist(img)
    res1 = np.hstack((img, equ1))
    cv2.imshow('P11', res1)
    cv2.waitKey()
    show_hist('H11', equ1.ravel())

    equ2 = cv2.equalizeHist(img_bright)
    res2 = np.hstack((img_bright, equ2))
    cv2.imshow('P21', res2)
    cv2.waitKey()
    show_hist('H21', equ2.ravel())

    equ3 = cv2.equalizeHist(img_dark)
    res3 = np.hstack((img_dark, equ3))
    cv2.imshow('P31', res3)
    cv2.waitKey()
    show_hist('H31', equ3.ravel())


if __name__ == '__main__':
    img = cv2.imread('lenna.png', 0)
    img_bright, img_dark = level1(img)
    level2(img)
    level3(img, img_bright, img_dark)
