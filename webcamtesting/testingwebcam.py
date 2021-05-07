from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import cv2,os,urllib.request,pickle
import numpy as np
from django.conf import settings


class Webcam(object):
    def __init__(self):
        self.vs = VideoStream(src=0).start()
        self.fps = FPS().start()

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        frame = self.vs.read()
        frame = cv2.flip(frame, 1)
        frame = imutils.resize(frame, width=600)
        frame = cv2.circle(frame , (150,150),radius= 5 , color= (100,244,220))
        self.fps.update()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
