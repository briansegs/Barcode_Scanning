"""Agent Scanner"""
import time as t
import sqlite3
import cv2 as cv
from pyzbar.pyzbar import decode
from scanner import Scanner

class AgentScanner(Scanner):
    "scans agent's barcodes"
    def scanAgent(self):
        "Scans Agent barcodes"
        db = 'testDb.sqlite'
        conn = sqlite3.connect(db)
        cur = conn.cursor()
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
                res = cur.execute("SELECT name, barcode FROM Agents WHERE barcode = ?", (bCode,))
                agentData = res.fetchone()
                if agentData is None:
                    print("Agent not found.")
                    t.sleep(1)
                else:
                    name = agentData[0]
                    agentCode = agentData[1]
                    return name, agentCode

        cam.release()
        cv.destroyAllWindows()
