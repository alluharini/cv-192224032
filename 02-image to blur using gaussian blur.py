import cv2
image=cv2.imread("C:\cv\example 5.jpeg")
g_i=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
b_i=cv2.GaussianBlur(g_i,(7,7),0)
cv2.imshow("blur",b_i)
