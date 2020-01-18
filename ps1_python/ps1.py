import cv2
import numpy as np
import sys
from ps1_functions import *


# Question 1: Edge Detection
img1 = cv2.imread('input/ps1-input0.png', cv2.IMREAD_GRAYSCALE)
edge_img = autoCanny.autoCanny(img1, 0.5)
cv2.imwrite('output/ps1-1-a-1.png', edge_img)

# Question 2: Hough Transform
edge_img = autoCanny.autoCanny(img1, 0.5)
# 2a computes the Hough Transform for lines
H, thetas, rhos = hough_lines_acc.hough_lines_acc(edge_img)
cv2.imwrite('output/ps1-2-a-1.png', H)
# 2b finds indices of the accumulator array and local maxima
peaks = hough_peaks.hough_peaks(H, numpeaks=10, threshold=100, nhood_size=50)
H_peaks = H.copy()
for peak in peaks:
    cv2.circle(H_peaks, tuple(peak[::-1]), 5, (255, 255, 255), -1)
