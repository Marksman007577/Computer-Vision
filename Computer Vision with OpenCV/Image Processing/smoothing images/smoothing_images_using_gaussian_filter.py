import cv2
import numpy as np

# Define global variables
FILTER_SIZE = 5  # A matrix for the gaussian filter
SIGMA_VALUE = 5  # the standard deviation

window_name = "Smoothing Images"

# Read in an image
img = cv2.imread('car.jpg')

# Applying Gaussian Blur
filtered_img = cv2.GaussianBlur(img, (FILTER_SIZE, FILTER_SIZE), SIGMA_VALUE)

# Save images
cv2.imwrite('gaussian_filtered_img.jpg', filtered_img)

# Show images
cv2.imshow(window_name, np.hstack((img, filtered_img)))
cv2.waitKey(0)
