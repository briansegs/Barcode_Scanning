"""Item Scanner"""
import time as t
import sqlite3
import cv2 as cv
from pyzbar.pyzbar import decode
from scanner import Scanner
from functions import getDate, getTime

class ItemScanner(Scanner):
    "scans item barcodes"
    def scanItems(self):
        "Scans item barcodes and stores them"
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
                res = cur.execute("SELECT name, barcode FROM Inventory WHERE barcode = ?", (bCode,))
                inventoryData = res.fetchone()

                if inventoryData is None:
                    print("Item not found.")
                    t.sleep(1)

                elif bCode in self.itemData:
                    print("Item already scanned.")
                    print("Would you like to update the quanity?")

                else:
                    itemName = inventoryData[0]
                    itemCode = inventoryData[1]
                    print(itemName)
                    t.sleep(.5)
                    while True:
                        try:
                            qty = int(input("Enter Quanity: "))
                            t.sleep(.5)
                            if qty <= 0:
                                print("Error: Enter a number greater than 0.")
                                t.sleep(1)
                            elif qty > 0:
                                break
                        except ValueError:
                            print("Error: Not a number.")
                            t.sleep(1)

                    self.itemData[bCode] = {
                        "barcode" : itemCode,
                        "name" : itemName,
                        "quantity" : qty,
                        "scan_date" : getDate(),
                        "scan_time" : getTime()
                        }
                    t.sleep(2)

        cam.release()
        cv.destroyAllWindows()
