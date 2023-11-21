"""Scanner"""
import time as t
from datetime import datetime
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
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        time = now.strftime("%H:%M:%S")

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
                        "Location" : self.local,
                        "Date" : date,
                        "Time" : time
                        }
                    print(bCode)
                    t.sleep(5)
                else:
                    print(bCode)
                    t.sleep(5)
        cam.release()
        cv.destroyAllWindows()
