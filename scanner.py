"""Scanner"""

class Scanner:
    """Scans Barcodes"""
    def __init__(self):
        self.closeKey = 'q'
        self.data = {}

    def getCloseKey(self):
        "returns the key that closes the camera"
        return self.closeKey

    def setCloseKey(self, newKey):
        "sets the key that closes the webcam"
        self.closeKey = newKey

    def getData(self):
        "returns stored data"
        return self.data
