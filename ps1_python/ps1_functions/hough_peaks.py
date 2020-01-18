import numpy as np
import cv2


def clip(idx):
    return int(max(idx, 0))


def hough_peaks(H, numpeaks=1, threshold=100, nhood_size=5):
    peaks = np.zeros((numpeaks, 2), dtype=np.uint64)
    temp_H = H.copy()
    for i in range(numpeaks):
        _, max_val, _, max_loc = cv2.minMaxLoc(temp_H)  # find maximum peak
        if max_val > threshold:
            peaks[i] = max_loc
            (c, r) = max_loc
            t = nhood_size//2.0
            temp_H[clip(r-t):int(r+t+1), clip(c-t):int(c+t+1)] = 0
        else:
            peaks = peaks[:i]
            break
    return peaks[:, ::-1]
