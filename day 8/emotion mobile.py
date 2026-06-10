from facial_emotion_recognition import EmotionRecognition
import urllib.request
import cv2
import numpy as np
import imutils
er=EmotionRecognition(device='cpu')
url='http://10.25.155.240:8080/shot.jpg'
while True:
    imgpath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgpath.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    frame=er.recognise_emotion(frame,return_type='BGR')
    frame=imutils.resize(frame,width=450)
    cv2.imshow('Frame',frame)
    key=cv2.waitKey(1)
    if key==27:
        break
url.release()
cv2.destroyAllWindows()
