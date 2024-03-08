import cv2
image = cv2.imread('your_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, threshold1=30, threshold2=100) 
cv2.imshow('Edge-detected Image', edges)

