"""Agent Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from scanner import Scanner
from functions import getDate, getTime

class ItemScanner(Scanner):
    "scans item barcodes"
    def scanItems(self):
        "Scans item barcodes and stores them"
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
                        "barcode" : bCode,
                        "bar_type" : code.type,
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
