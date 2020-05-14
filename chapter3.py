import cv2
import numpy as np

img = cv2.imread("Resources/person.jpg")
print(img.shape)
imgResize = cv2.resize(img,(300,300))
imgCropp = img[0:200,200:400]
cv2.imshow("Image",img)
# cv2.imshow("ImageResize",imgResize)
cv2.imshow("ImageCropped",imgCropp)

cv2.waitKey(0)