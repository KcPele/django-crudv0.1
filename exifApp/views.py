from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from subprocess import Popen, PIPE, STDOUT
import requests
import json
import os


PROJECT_MEDIA_DIR = os.getcwd() + "/media/images/"


def homepage(request):
    return render(request, 'home.html')


def exif(request):
    # pass in file name after upload for production
    image_file_name = f"{PROJECT_MEDIA_DIR}/1652373898994.png"
    process = Popen(['exiftool', image_file_name], stdout=PIPE, stderr=STDOUT)
    output_byte = process.stdout.read()
    print(output_byte)
    output_list = str(output_byte)[2:-1].strip().split('\\n')
    return render(request, 'exif.html', {"output": output_list, "filename": image_file_name.split('/')[-1]})