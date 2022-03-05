import cv2
from PIL import Image

class CubeReader:

    @staticmethod
    def capture_cube_face():
        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        bound = cv2.imread('Bounding_Box.jpg')
            
        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Input', cv2.addWeighted(frame, 1, bound, 0.2, 0))

            c = cv2.waitKey(1)
            if c == 32: # if space bar was pressed
                cv2.imwrite('test_image.jpg', frame)
            if c == 27: # if esc key was pressed
                break

        cap.release()
        cv2.destroyAllWindows()