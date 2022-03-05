import cv2
from PIL import Image

class CubeReader:

    @staticmethod
    def capture_cube_face():
        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Input', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break

            cv2.imwrite('test_image.jpg', frame)

        cap.release()
        cv2.destroyAllWindows()