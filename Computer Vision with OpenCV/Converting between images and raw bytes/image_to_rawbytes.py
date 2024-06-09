import os
import numpy as np
import cv2

# Make and array of 120000 random bytes
random_byte_arrays = bytearray(os.urandom(120000))
#random_byte_arrays = np.random.randint(0, 256, 120000)

# Flatten the byte array into numpy
flat_numpy_array = np.array(random_byte_arrays)

# Convert an array to make a 300x400 grayscale image
gray_image = flat_numpy_array.reshape(300, 400)
cv2.imwrite("Random_grayscale_image.png", gray_image)

# Convert an array to make a 100x400x3channel colored image
color_image = flat_numpy_array.reshape(100, 400, 3)
cv2.imwrite("Random_color_image.png", gray_image)
