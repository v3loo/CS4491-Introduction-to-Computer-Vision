import cv2
import numpy as np
import os.path

# Question 1: Input images
img1 = np.zeros((400, 255, 3), np.uint8)
img2 = np.zeros((155, 255, 3), np.uint8)
if not os.path.isfile('output/ps0-1-a-1.png')\
        or not os.path.isfile('output/ps0-1-a-2.png'):
    img1 = cv2.imread('input/fruit.png', cv2.IMREAD_COLOR)
    cv2.imwrite('output/ps0-1-a-1.png', img1)
    img2 = cv2.imread('input/woman.tiff', cv2.IMREAD_COLOR)
    cv2.imwrite('output/ps0-1-a-2.png', img2)
else:
    img1 = cv2.imread('output/ps0-1-a-1.png', cv2.IMREAD_COLOR)
    img2 = cv2.imread('output/ps0-1-a-2.png', cv2.IMREAD_COLOR)

# Question 2: Color planes
'''
    a.Swap the red and blue pixels
    b.Monochrome image of green channel
    c.Monochrome image of red channel
    d.Monochrome image of blue channel
'''
img1_swapped = img1.copy()
img1_swapped[:, :, 0], img1_swapped[:, :,
                                    2] = img1_swapped[:, :, 2], img1_swapped[:, :, 0]
img1_green = img1[:, :, 1]
img1_red = img1[:, :, 2]
img1_blue = img1[:, :, 0]

cv2.imwrite('output/ps0-2-a-1.png', img1_swapped)
cv2.imwrite('output/ps0-2-b-1.png', img1_green)
cv2.imwrite('output/ps0-2-c-1.png', img1_red)
cv2.imwrite('output/ps0-2-d-1.png', img1_blue)

# Question 3: Replacement of pixels
img1_center = [dim//2 for dim in img1.shape[:2]]
img2_center = [dim//2 for dim in img1.shape[:2]]

img1_mono1 = img1_green.copy()
img1_mono2 = img1_red.copy()

img1_mono2[img2_center[0]-50:img2_center[0]+50,
           img2_center[1]-50:img2_center[1]+50] =\
    img1_mono1[img1_center[0]-50:img1_center[0]+50,
               img1_center[1]-50:img1_center[1]+50]

cv2.imwrite('output/ps0-3-a-1.png', img1_mono2)

# Question 4: Arithmetic and Geometric operations
'''
    a. Min, max, mean, standard value of img1_green
    b.normalise img1_green and then multiply with 10 and add the mean
    c. shift img by 2 pixels to the left
    d.subtract shifted version from original
'''

# 4a
min1 = img1_green.min()
max1 = img1_green.max()
mean1 = img1_green.mean()
std1 = img1_green.std()
print('4a) img1_green: min=%d, max=%d, mean=%f std=%f' %
      (min1, max1, mean1, std1))

# 4b
img1_green_normed = img1_green.copy()
img1_green_normed = cv2.add(cv2.multiply(cv2.divide(cv2.subtract(
    img1_green_normed, mean1), std1), 10), mean1)
cv2.imwrite('output/ps0-4-b-1.png', img1_green_normed)

# 4c
img1_shifted = img1_green.copy()
rows, cols = img1_shifted.shape[0:2]
M = np.float32([[1, 0, -2], [0, 1, 0]])
img1_shifted = cv2.warpAffine(img1_shifted, M, (cols, rows))
cv2.imwrite('output/ps0-4-c-1.png', img1_shifted)

# 4d
img1_diff_shifted = img1_shifted.copy()
img1_diff_shifted = img1_diff_shifted-img1_green
cv2.imwrite('output/ps0-4-d-1.png', img1_diff_shifted)

# Question 5: Noise
