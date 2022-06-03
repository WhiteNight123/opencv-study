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
