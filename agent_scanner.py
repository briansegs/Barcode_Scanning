"""Agent Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from scanner import Scanner
from functions import getCursor
from data import getAgent

class AgentScanner(Scanner):
    "scans agent's barcodes"
    def scanAgent(self):
        "Scans Agent barcodes"
        cur = getCursor()
        print(f'Hit the ({self.closeKey}) key to quit scanning.')
        t.sleep(1)

        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord(self.closeKey):
                break

            for code in decode(frame):
                bCode = str(code.data.decode('utf-8'))
                print(bCode)
                res = cur.execute(getAgent, (bCode,))
                agentData = res.fetchone()

                if agentData is None:
                    print("Agent not found.")
                    t.sleep(1)
                else:
                    name = agentData[0] + " " + agentData[1]
                    agentCode = agentData[2]
                    return name, agentCode

        cam.release()
        cv.destroyAllWindows()
