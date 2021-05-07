from django.urls import path, include
from webcamtesting import views


urlpatterns = [
    path('', views.index, name='index'),
    path('facecam_feed', views.testfun, name='facecam_feed'),
    ]