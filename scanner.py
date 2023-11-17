"""Scanner"""
import time
import cv2 as cv
from pyzbar.pyzbar import decode

class Scanner:
    """Scans Barcodes and QR codes"""
    # TODO: Add quitKey feature to edit key that quits scanning
    # TODO: Add showKey to show the current quitKey
    def __init__(self, location):
        self.data = dict()
        self.local = location

    def printData(self):
        # TODO: Change to getData where data is returned
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
                # TODO: put "code.data.decode('utf-8')" into a variable
                # TODO: Structure data (plan first)
                # TODO: add date and time to data{}
                if code.data.decode('utf-8') not in self.data:
                    self.data[code.data.decode('utf-8')] = code.type, self.local
                    print(code.data.decode('utf-8'), code.type)
                    time.sleep(5)
                else:
                    print(code.data.decode('utf-8'), code.type)
                    time.sleep(5)
        cam.release()
        cv.destroyAllWindows()

        # TODO: Id rather make a retun function and remove this return
        return self.data
