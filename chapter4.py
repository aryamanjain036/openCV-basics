import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

# print(img)
# img[:]=255,0,0
# cv2.line(img,(0,0),(300,300),(0,255,0),3)
# to get the line from cross to cross
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(200,300),(255,150,0),4)
cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(150,255,150),1)

cv2.imshow("Image",img)
cv2.waitKey(0)