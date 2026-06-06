import cv2
img=cv2.imread("mu.jpg")
grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",img)
cv2.imshow("grayimage",grayImage)
cv2.imwrite("gray.jpg",grayImage)
