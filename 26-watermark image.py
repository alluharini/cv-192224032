import cv2
image = cv2.imread("C:\cv\example 5.jpeg")
watermark = cv2.imread("C:\cv\Lamborghini-Logo.png", cv2.IMREAD_UNCHANGED)
wm_resized = cv2.resize(watermark, (image.shape[1], image.shape[0]))

if wm_resized.shape[2] == 4:
    wm_resized = cv2.cvtColor(wm_resized, cv2.COLOR_BGRA2BGR)

result = cv2.addWeighted(image, 1, wm_resized, 0.3, 0)

filename = "watermarked_image.jpg"
cv2.imwrite(filename, result)
cv2.imshow("Watermarked Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
