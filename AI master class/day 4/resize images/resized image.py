import cv2
import imutils
img=cv2.imread("mu.jpg")
resizedimg=imutils.resize(img,width=500)
cv2.imshow("original",img)
cv2.imshow("resizeimage",resizedimg)
cv2.imwrite("resizeimage.jpg",resizedimg)
