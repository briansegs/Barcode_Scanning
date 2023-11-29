"""Agent Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from scanner import Scanner
from functions import getDate, getTime

# TODO: import a dict of agent info including barcodes to use
# TODO: Scanner should check if agent is in dict
# TODO: Scanner should return a boolean plus agent info to app
# TODO: Scanner should quit when it finds a match in dict
# TODO: Idea - Scanner or app could send a check-in message -
# with time and date

class AgentScanner(Scanner):
    "scans agent's barcodes"
    def scanAgent(self):
        "Scans Agent barcodes"
        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord(self.closeKey):
                # TODO: return False for app
                break

            for code in decode(frame):
                bCode = code.data.decode('utf-8')
                # TODO: change "if statement" to check agent dict
                if bCode not in self.data:
                    # TODO: also add agent info to data{}
                    self.data[bCode] = {
                        "barcode" : bCode,
                        "bar_type" : code.type,
                        "scan_date" : getDate(),
                        "scan_time" : getTime()
                        }
                    # TODO: return True plus data{}
                    # TODO: remove print statment
                    print(bCode)
                    t.sleep(5)
                else:
                    # TODO: change to print that agent is not found
                    print(bCode)
                    t.sleep(5)
        cam.release()
        cv.destroyAllWindows()
