import cv2
import numpy as np

# Define global variables
FILTER_SIZE = 3  # A matrix for the gaussian filter

window_name = "Smoothing Images"

# Read in an image
img = cv2.imread('car.jpg')

# Creating the mean filter
mean_filter = np.ones((FILTER_SIZE, FILTER_SIZE), np.float32) / FILTER_SIZE*FILTER_SIZE

smooth_img = cv2.filter2D(img, -1, mean_filter)

# Save images
cv2.imwrite('mean_filtered_img.jpg', smooth_img)

# Show images
cv2.imshow(window_name, np.hstack((img, smooth_img)))
cv2.waitKey(0)
