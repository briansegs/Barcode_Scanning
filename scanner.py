"""Scanner"""
import time
import cv2 as cv
from pyzbar.pyzbar import decode

class Scanner:
    """Scans Barcodes and QR codes"""
    def __init__(self):
        self.data = dict()

    def printData(self):
        """prints stored data"""
        print('Scanned information:')
        for key, value in self.data.items():
            print(f'Data: {key}, Type: {value}')

    def startScanner(self):
        """Starts the scanner"""
        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord('q'):
                break

            for code in decode(frame):
                if code.data.decode('utf-8') not in self.data:
                    self.data[code.data.decode('utf-8')] = code.type
                    print(code.data.decode('utf-8'), code.type)
                    time.sleep(5)
                else:
                    print(code.data.decode('utf-8'), code.type)
                    time.sleep(5)
        cam.release()
        cv.destroyAllWindows()

        return self.data
