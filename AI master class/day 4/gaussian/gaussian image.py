import cv2
img=cv2.imread("mu.jpg")
gaussianImg=cv2.GaussianBlur(img,(41,41),50)
gaussianImg1=cv2.GaussianBlur(img,(21,21),0)
cv2.imshow("original",img)
cv2.imshow("gaussianBlur",gaussianImg)
cv2.imshow("gaussianBlur1",gaussianImg1)
cv2.imwrite("gaussianBlur.jpg",gaussianImg1)
