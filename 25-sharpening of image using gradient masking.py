import cv2
image = cv2.imread("C:\cv\example 5.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grad_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.addWeighted(cv2.convertScaleAbs(grad_x), 0.5, cv2.convertScaleAbs(grad_y), 0.5, 0)

sharpened_image = cv2.addWeighted(gray_image, 1.5, gradient, -0.5, 0)

cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
