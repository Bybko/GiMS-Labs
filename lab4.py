import cv2
import numpy as np

image = cv2.imread('Images\Hands.bmp')

# 1. Однородное сглаживание
kernel_size = (5, 5)
blurred_image = cv2.blur(image, kernel_size)

# 2. Выделение краев (фильтр Кенни)
edges_image = cv2.Canny(blurred_image, 50, 150)

# 3. Повышение резкости с помощью свертки
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
sharpened_image = cv2.filter2D(blurred_image, -1, sharpening_kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Edges Image (Canny Filter)', edges_image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
