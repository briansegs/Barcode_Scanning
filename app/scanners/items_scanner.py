"""Item Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from util import getDate, getTime, getCursorConnection, newLine
from classes import Item, Scanner

class ItemScanner(Scanner):
    "scans item barcodes"
    def scanItems(self):
        "Scans item barcodes and stores them"
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
                res = cur.execute("SELECT id, name FROM item WHERE barcode = ?", (bCode,))
                inventoryData = res.fetchone()

                if inventoryData is None:
                    newLine()
                    print("Item not found.")
                    t.sleep(1)

                elif bCode in self.itemData:
                    pass

                else:
                    item = Item(inventoryData[1], inventoryData[0])
                    newLine()
                    print(bCode, "\n")
                    print(item.name)
                    t.sleep(.5)
                    while True:
                        try:
                            qty = int(input("Enter Quantity: "))
                            t.sleep(.5)
                            if qty <= 0:
                                print("Error: Enter a number greater than 0.")
                                t.sleep(1)
                            elif qty > 0:
                                break
                        except ValueError:
                            print("Error: Not a number. \n")
                            t.sleep(1)

                    self.itemData[bCode] = {
                        "name" : item.name,
                        "item_id" : item.id,
                        "quantity" : qty,
                        "scan_date" : getDate(),
                        "scan_time" : getTime()
                        }
                    print("item saved.")
                    t.sleep(1)
        conn.close()
        cam.release()
        cv.destroyAllWindows()
