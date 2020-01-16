import cv2
import numpy as np
import os.path

#Question 1: Input images
img1 = np.zeros((400,255,3), np.uint8)
img2 = np.zeros((155,255,3), np.uint8)
if not os.path.isfile('output/ps0-1-a-1.png')\
    or not os.path.isfile('output/ps0-1-a-2.png'):
    img1 = cv2.imread('input/fruit.png', cv2.IMREAD_COLOR)
    cv2.imwrite('output/ps0-1-a-1.png', img1)
    img2 = cv2.imread('input/woman.tiff', cv2.IMREAD_COLOR)
    cv2.imwrite('output/ps0-1-a-2.png', img2)
else:
    img1 = cv2.imread('output/ps0-1-a-1.png', cv2.IMREAD_COLOR)
    img2 = cv2.imread('output/ps0-1-a-2.png',cv2.IMREAD_COLOR)

#Question 2: Color planes
'''
    a.Swap the red and blue pixels
    b.Monochrome image of green channel
    c.Monochrome image of red channel
    d.Monochrome image of blue channel
'''
img1_swapped = img1.copy()
img1_swapped[:,:,0], img1_swapped[:,:,2] = img1_swapped[:,:,2], img1_swapped[:,:,0]
img1_green = img1[:,:,1]
img1_red = img1[:,:,2]
img1_blue = img1[:,:,0]

cv2.imwrite('output/ps0-2-a-1.png', img1_swapped)
cv2.imwrite('output/ps0-2-b-1.png', img1_green)
cv2.imwrite('output/ps0-2-c-1.png', img1_red)
cv2.imwrite('output/ps0-2-d-1.png', img1_blue)

#Question 3: Replacement of pixels
img1_center = [dim//2 for dim in img1.shape[:2]]
img2_center = [dim//2 for dim in img1.shape[:2]]

img1_mono1 = img1_green.copy()
img1_mono2 = img1_red.copy()

img1_mono2[img2_center[0]-50:img2_center[0]+50,
              img2_center[1]-50:img2_center[1]+50] =\
        img1_mono1[img1_center[0]-50:img1_center[0]+50,
                      img1_center[1]-50:img1_center[1]+50]

cv2.imwrite('output/ps0-3-a-1.png', img1_mono2)