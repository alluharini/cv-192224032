import cv2
image = cv2.imread("C:\cv\example 5.jpeg")
clockwise_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image', clockwise_image)
