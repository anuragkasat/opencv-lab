import cv2
import numpy as np

image = cv2.imread('o.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)

unsharp_mask = gray_image - blurred_image

sharpened_image = gray_image + unsharp_mask

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
