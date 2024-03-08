import cv2
import numpy as np
image = cv2.imread("C:\cv\example 5.jpeg")
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)
cv2.imshow('Sobel y-axis Edge Detection', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
