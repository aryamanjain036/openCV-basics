import cv2
import numpy as np

print("package imported")
kernal = np.ones((5,5),np.uint8)

img = cv2.imread("Resources\person.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDilation = cv2.dilate(imgCanny,kernal,iterations=1)
imgErosion = cv2.erode(imgDilation,kernal,iterations=1)
cv2.imshow("ImageGray",imgGray)
cv2.imshow("ImageBlur",imgBlur)
cv2.imshow("ImageCanny",imgCanny)
cv2.imshow("ImageDilation",imgDilation)
cv2.imshow("ImageErosion",imgErosion)
cv2.waitKey(0)