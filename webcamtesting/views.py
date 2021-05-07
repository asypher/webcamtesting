from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from webcamtesting.testingwebcam import Webcam


# Create your views here.
def index(request):
    return render(request, 'webcamtesting/home.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def testfun(request):
    return StreamingHttpResponse(gen(Webcam()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')