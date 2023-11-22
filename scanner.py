"""Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from functions import getLocation, getAgent, getDate, getTime

class Scanner:
    """Scans Barcodes and QR codes"""
    # TODO: add agent
    def __init__(self):
        self.closeKey = 'q'
        self.data = {}

    # TODO: add getAgent to return the current agent
    def getCloseKey(self):
        "returns the key that closes the camera"
        return self.closeKey

    def setCloseKey(self, newKey):
        "sets the key that closes the webcam"
        self.closeKey = newKey

    def getData(self):
        "returns stored data"
        return self.data

    def startScanner(self):
        "Starts the scanner"
        location = getLocation()
        agent = getAgent()

        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord(self.closeKey):
                break

            for code in decode(frame):
                bCode = code.data.decode('utf-8')
                if bCode not in self.data:
                    self.data[bCode] = {
                        "Barcode" : bCode,
                        "Type" : code.type,
                        "agent" : agent,
                        "pickup location" : location,
                        "pickup date" : getDate(),
                        "pickup time" : getTime()
                        }
                    print(bCode)
                    t.sleep(5)
                else:
                    print(bCode)
                    t.sleep(5)
        cam.release()
        cv.destroyAllWindows()
