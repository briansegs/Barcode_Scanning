"""camera"""
import cv2 as cv

class WebCam:
    """Webcam"""
    def __init__(self, closeKey='q'):
        self.closeKey = closeKey

    def showCloseKey(self):
        """prints the key that closes the camera to the terminal"""
        print(self.closeKey)

    def setCloseKey(self, newKey):
        """sets the key that closes the webcam"""
        self.closeKey = newKey

    def startCam(self):
        """starts the webcam"""
        cam = cv.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            cv.imshow('frame', frame)

            if cv.waitKey(1) == ord(self.closeKey):
                break

        cam.release()

        cv.destroyAllWindows()
