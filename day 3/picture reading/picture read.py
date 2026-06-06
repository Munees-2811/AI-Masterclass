import cv2
img=cv2.imread("m.jpg")
cv2.imshow("show",img)
cv2.imwrite("photo.jpg",img)
