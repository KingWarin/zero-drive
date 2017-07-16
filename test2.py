import numpy as np
import cv2
import zbar

from PIL import Image

cap = cv2.VideoCapture(0)
fast = cv2.FastFeatureDetector()
scanner = zbar.ImageScanner()
scanner.parse_config('enable')
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    pil = Image.fromarray(gray)
    width, height = pil.size
    raw = pil.tobytes()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)

    img = gray
    for symbol in image:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
        topLeft, bottomLeft, bottomRight, topRight = symbol.location
        if 'z10.info' in symbol.data:
            cv2.rectangle(gray, topLeft, bottomRight, (0,255,0),3)
            if topLeft[0] < width/3:
                print "out of left boundary"
            if topRight[0] > 2*width/3:
                print "out of right boundary"
    cv2.imshow('qr', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
