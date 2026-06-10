import urllib.request
import cv2
import numpy as np
import imutils
url='http://10.25.155.240:8080/shot.jpg'
while True:
    imgpath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgpath.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    frame=imutils.resize(frame,width=550)
    cv2.imshow('Frame',frame)
    if ord('q')==cv2.waitKey(1):
        exit(0)
