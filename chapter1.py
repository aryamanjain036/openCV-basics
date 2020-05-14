import cv2
import numpy as np

print("package imported")
img = cv2.imread("Resources\person.jpg")

cv2.imshow("Image",img)
cv2.waitKey(0)

cap = cv2.VideoCapture("Resources/videoplayback (1).mp4")
# //to open webcam instead of "Resources/videoplayback (1).mp4" type (0)
# //cap.set(3,640)--->width
# //cap.set(4,480)--->height
# //cap.set(10,100)--->brightness

while True:
    success,img1 = cap.read()
    cv2.imshow("Video", img1)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

