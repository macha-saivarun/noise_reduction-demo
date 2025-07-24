import cv2
import numpy as np

image = cv2.imread('noisy_image.jpg')
cv2.namedWindow('Noise Reduction Demo')

def nothing(x):
    pass

cv2.createTrackbar('Kernel Size', 'Noise Reduction Demo', 1, 20, nothing)
cv2.createTrackbar('Method', 'Noise Reduction Demo', 0, 2, nothing)

while True:
    k = cv2.getTrackbarPos('Kernel Size', 'Noise Reduction Demo')
    method = cv2.getTrackbarPos('Method', 'Noise Reduction Demo')
    k = max(1, k*2 + 1)

    if method == 0:
        output = cv2.blur(image, (k, k))
    elif method == 1:
        output = cv2.GaussianBlur(image, (k, k), 0)
    else:
        output = cv2.medianBlur(image, k)

    cv2.imshow('Noise Reduction Demo', output)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
