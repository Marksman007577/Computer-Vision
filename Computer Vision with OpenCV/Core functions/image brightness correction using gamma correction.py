import cv2
import numpy as np


image = cv2.imread('WindowsLogo.jpg')
if image is None:
    print('Could not open or find the image')
    exit(0)

gamma = 0.4

look_up_table = np.empty((1, 256), np.uint8)
for i in range(256):
    look_up_table[0, i] = np.clip(pow(i/255.0, gamma) * 255, 0, 255)

result = cv2.LUT(image, look_up_table)

cv2.imshow('Original Image', image)
cv2.imshow('New Image', result)
# Wait until user press some key
cv2.waitKey()