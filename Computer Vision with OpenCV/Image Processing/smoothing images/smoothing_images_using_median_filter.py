import cv2
import numpy as np

# Define global variables
FILTER_SIZE = 3  # A matrix for the gaussian filter

window_name = "Smoothing Images"

# Read in an image
img = cv2.imread('megan.jpg')

# smooth image
smooth_img = cv2.medianBlur(img, FILTER_SIZE)

# Save images
cv2.imwrite('median_filtered_img.jpg', smooth_img)

# Show images
cv2.imshow(window_name, np.hstack((img, smooth_img)))
cv2.waitKey(0)
