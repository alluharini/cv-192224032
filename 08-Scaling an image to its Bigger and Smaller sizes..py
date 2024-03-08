import cv2
image = cv2.imread("C:\cv\example 5.jpeg")
bigger_image = cv2.resize(image, None, fx=2, fy=2)
cv2.imshow('Bigger Image', bigger_image)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5)
cv2.imshow('Smaller Image', smaller_image)

