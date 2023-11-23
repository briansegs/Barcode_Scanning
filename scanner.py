"""Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from functions import getLocation, getAgent, getDate, getTime

# TODO: make parent scanner class 
# TODO: children should be for scanning 1. items and 2. agent barcodes
class Scanner:
    """Scans Barcodes"""
    def __init__(self):
        self.closeKey = 'q'
        self.data = {}

    def getCloseKey(self):
        "returns the key that closes the camera"
        return self.closeKey

    def setCloseKey(self, newKey):
        "sets the key that closes the webcam"
        self.closeKey = newKey

    def getData(self):
        "returns stored data"
        return self.data

    # TODO: should be added to child class when created
    def startScanner(self):
        "Starts the scanner"
        # TODO: put get Location and Agent into main app
        location = getLocation()
        agent = getAgent()

        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord(self.closeKey):
                break

            # TODO: seperate out to make scanner generic
            # look into class inheritance.
            # look into storing the data the same way.
            # make what I do after what is different.
            # I want to be able to scan agent barcodes with -
            # the same scanner. Not have two different scanners -
            # that share 90% of the same code.

            for code in decode(frame):
                bCode = code.data.decode('utf-8')
                if bCode not in self.data:
                    # TODO: remove agent and location
                    self.data[bCode] = {
                        "barcode" : bCode,
                        "bar_type" : code.type,
                        "scan_agent" : agent,
                        "scan_location" : location,
                        "scan_date" : getDate(),
                        "scan_time" : getTime()
                        }
                    print(bCode)
                    t.sleep(5)
                else:
                    print(bCode)
                    t.sleep(5)
        cam.release()
        cv.destroyAllWindows()
