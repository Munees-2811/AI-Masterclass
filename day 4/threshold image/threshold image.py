import cv2
img=cv2.imread("mu.jpg")
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresholdimg=cv2.threshold(grayimg,200,255,cv2.THRESH_BINARY)[1]
cv2.imshow("original",img)
cv2.imshow("thresholdimage",thresholdimg)
cv2.imwrite("thresholdimage.jpg",thresholdimg)
