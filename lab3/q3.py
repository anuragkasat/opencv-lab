import cv2
import numpy as np

# Load the image
image = cv2.imread('r.jpg')

# Apply a box filter (averaging filter)
box_filtered = cv2.boxFilter(image, -1, (5, 5))  # (5, 5) is the kernel size

# Display the original and box-filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Box Filtered Image', box_filtered)

gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)  # (5, 5) is the kernel size, 0 is the standard deviation
cv2.imshow('Gaussian Filtered Image', gaussian_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()