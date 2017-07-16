import numpy as np
import cv2
import zbar

cap = cv2.VideoCapture(0)
fast = cv2.FastFeatureDetector()
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    kp = fast.detect(frame, None)
    img2 = cv2.drawKeypoints(gray, kp, color=(255,0,0))
    #cv2.imshow('img2', img2)
    img3 = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst, None)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
