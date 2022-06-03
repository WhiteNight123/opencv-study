import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from numpy import matrix


def fun1(src):
    mean = np.mean(src[0:2])
    median = np.median(src[0:2])
    print(mean)
    print(median)
    e1 = matrix(src[0:2] > mean)
    img1 = np.array(e1, dtype=np.uint8) * 255
    img2 = np.vstack((img1, src[2:]))
    # cv.imshow('fun1_image1', img2)
    # cv.waitKey(0)

    e2 = matrix(src[0:2] > median)
    img3 = np.array(e2, dtype=np.uint8) * 255
    img4 = np.vstack((img3, src[2:]))
    # cv.imshow('fun1_image2', img4)
    # cv.waitKey(0)
    return


def fun2(src):
    mean = np.mean(src)
    median = np.median(src)
    print(mean)
    print(median)
    _, thresh1 = cv.threshold(src, mean, 255, cv.THRESH_BINARY)
    # cv.imshow('fun2_image1', thresh1)
    # cv.waitKey(0)

    _, thresh2 = cv.threshold(src, median, 255, cv.THRESH_BINARY)
    # cv.imshow('fun2_image2', thresh2)
    # cv.waitKey(0)
    return


def fun3(src):
    w, h = src.shape
    mean = np.mean(src)
    _, src_binary = cv.threshold(src[0:int(h / 2), :], mean, 255, cv.THRESH_BINARY)
    src_final = np.vstack([src_binary, src[int(h / 2):, :]])
    cv.imshow('fun3_image', src_final)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return


if __name__ == '__main__':
    img = cv.imread('test.jpg')
    cv.imshow('image', img)
    cv.waitKey(0)

    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imshow('image_gray', img_gray)
    cv.waitKey(0)

    ret_binary, img_binary = cv.threshold(img_gray, 128, 255, cv.THRESH_BINARY)
    cv.imshow('image_binary', img_binary)
    cv.waitKey(0)

    # Level1
    fun1(img_gray)
    # Level2
    fun2(img_gray)
    # Level3
    fun3(img_gray)
