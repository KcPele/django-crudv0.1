
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('exif/', views.exif, name='exif'),

]