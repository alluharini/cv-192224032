import cv2
import numpy as np
image = cv2.imread("C:\cv\example 5.jpeg")
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

sharpened_image = cv2.filter2D(image, -1, kernel)
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
