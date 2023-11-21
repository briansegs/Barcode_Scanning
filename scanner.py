"""Scanner"""
import time
import cv2 as cv
from pyzbar.pyzbar import decode

class Scanner:
    """Scans Barcodes and QR codes"""
    def __init__(self, location):
        self.closeKey = 'q'
        self.data = {}
        self.local = location

    def showCloseKey(self):
        """prints the key that closes the camera to the terminal"""
        print(self.closeKey)

    def setCloseKey(self, newKey):
        """sets the key that closes the webcam"""
        self.closeKey = newKey

    def getData(self):
        """returns stored data"""
        return self.data

    def startScanner(self):
        """Starts the scanner"""
        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord(self.closeKey):
                break

            for code in decode(frame):
                bCode = code.data.decode('utf-8')
                # TODO: Structure data (plan first)
                # TODO: add date and time to data{}
                if bCode not in self.data:
                    self.data[bCode] = code.type, self.local
                    print(bCode, code.type)
                    print(bCode not in self.data)
                    time.sleep(5)
                else:
                    print(bCode, code.type)
                    print("else:")
                    time.sleep(5)
        cam.release()
        cv.destroyAllWindows()
