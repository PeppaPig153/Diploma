import cv2 as cv
from matplotlib import pyplot as plt

# толщина линии контура
THICKNESS = 3
# цвет линии контура в формате BGR
CONTOUR_COLOR = (0, 0, 0)

def Test(filename):
    x, y = (3, 3)
    img = cv.imread(filename, 0)
    plt.subplot(x, y, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    laplacian = cv.Laplacian(img, cv.CV_64F)
    plt.subplot(3, 3, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    sobel = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    plt.subplot(x, y, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 5), plt.imshow(sobel, cmap='gray')
    plt.title('XY Sobel'), plt.xticks([]), plt.yticks([])

    scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)
    scharry = cv.Scharr(img, cv.CV_64F, 0, 1)
    scharr = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    plt.subplot(x, y, 6), plt.imshow(scharrx, cmap='gray')
    plt.title('Scharr X'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 7), plt.imshow(scharry, cmap='gray')
    plt.title('Scharr Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 8), plt.imshow(scharr, cmap='gray')
    plt.title('XY Scharr'), plt.xticks([]), plt.yticks([])

    canny = cv.Canny(img, 100, 200, 1)
    plt.subplot(x, y, 9), plt.imshow(canny, cmap='gray')
    plt.title('Canny'), plt.xticks([]), plt.yticks([])

    plt.show()


def TestContours(filename):
    x, y = (3, 3)
    img = cv.imread(filename, 0)
    plt.subplot(x, y, 1), plt.imshow(img)
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    laplacian = cv.Laplacian(img, cv.CV_64F)
    plt.subplot(3, 3, 2), plt.imshow(laplacian)
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    sobel = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    plt.subplot(x, y, 3), plt.imshow(sobelx)
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 4), plt.imshow(sobely)
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 5), plt.imshow(sobel)
    plt.title('XY Sobel'), plt.xticks([]), plt.yticks([])

    scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)
    scharry = cv.Scharr(img, cv.CV_64F, 0, 1)
    scharr = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    plt.subplot(x, y, 6), plt.imshow(scharrx)
    plt.title('Scharr X'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 7), plt.imshow(scharry)
    plt.title('Scharr Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(x, y, 8), plt.imshow(scharr)
    plt.title('XY Scharr'), plt.xticks([]), plt.yticks([])

    canny = cv.Canny(img, 100, 200, 1)
    plt.subplot(x, y, 9), plt.imshow(canny)
    plt.title('Canny'), plt.xticks([]), plt.yticks([])

    plt.show()

if __name__=="__main__":
    TestContours("../src/prob.jpg")



