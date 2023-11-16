"""Scanner"""
import time
import cv2 as cv
from pyzbar.pyzbar import decode


cam = cv.VideoCapture(0)

data = dict()

camera = True
while camera is True:
    ret, frame = cam.read()

    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

    for code in decode(frame):
        if code.data.decode('utf-8') not in data:
            data[code.data.decode('utf-8')] = code.type
            print(code.data.decode('utf-8'), code.type)
            time.sleep(5)
        else:
            print(code.data.decode('utf-8'), code.type)
            time.sleep(5)



cam.release()

cv.destroyAllWindows()
    