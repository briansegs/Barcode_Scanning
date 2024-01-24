"""Item Scanner"""
import time as t
import cv2 as cv
from pyzbar.pyzbar import decode
from scanner import Scanner
from util import getDate, getTime, getCursorConnection, newLine
from item import Item

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
                newLine()
                print(bCode, "\n")
                res = cur.execute("SELECT id, name FROM item WHERE barcode = ?", (bCode,))
                inventoryData = res.fetchone()

                if inventoryData is None:
                    print("Item not found.")
                    t.sleep(1)

                elif bCode in self.itemData:
                    name = self.itemData[bCode]["name"]
                    print("Item already scanned.")
                    print(f'Would you like to update the quantity of {name}?')
                    ans = input("Enter y to update or n to continue: ")

                    if ans == "y":
                        oldQty = self.itemData[bCode]["quantity"]

                        try:
                            newQty = int(input("Enter Quantity: "))
                            t.sleep(.5)
                            if newQty == 0:
                                del self.itemData[bCode]
                                print(f'{name} quantity updated from {oldQty} to {newQty}.')

                            elif newQty < 0:
                                print("Error: Number can not be less than 0.")
                                print("Could not update the quantity.")
                            elif newQty > 0:
                                self.itemData[bCode]["quantity"] = newQty
                                print(f'{name} quantity updated from {oldQty} to {newQty}.')

                        except ValueError:
                            print("Error: Not a number.")
                            t.sleep(1)
                            print("Could not update the quantity.")
                            t.sleep(1)

                    else:
                        print("Continue scanning.")
                        t.sleep(1)

                else:
                    item = Item(inventoryData[1], inventoryData[0])
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
