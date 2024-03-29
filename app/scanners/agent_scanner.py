"""Agent Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from util import getCursorConnection, newLine
from data import getAgent
from classes import Scanner

class AgentScanner(Scanner):
    "scans agent's barcodes"
    def scanAgent(self):
        "Scans Agent barcodes"
        cur, conn = getCursorConnection()
        print(f'Hit the ({self.closeKey}) key to quit scanning. \n')
        t.sleep(1)

        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord(self.closeKey):
                break

            for code in decode(frame):
                bCode = str(code.data.decode('utf-8'))
                newLine()
                print(bCode, "\n")

                res = cur.execute(getAgent, (bCode,))
                agentData = res.fetchone()

                if agentData is None:
                    print("Agent not found.")
                    t.sleep(1)
                else:
                    agentId = agentData[0]
                    name = agentData[1] + " " + agentData[2]
                    return name, agentId
        conn.close()
        cam.release()
        cv.destroyAllWindows()
