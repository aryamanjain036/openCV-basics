import cv2
import numpy as np
# STILL GETTING ISSUES IN THE CODE (NEED TO DO IT AGAIN)
img = cv2.imread("Resources/card1.jpg")
width,height = 250,350
pts1 = np.float32([[352,30],[643,30],[643,434],[352,434]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("ImageOutput",imgoutput)
cv2.waitKey(0)