from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from subprocess import Popen, PIPE, STDOUT
# import requests
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


from django.shortcuts import render

from .forms import Profile_Form
import exifread
import base64
from io import BytesIO
from .models import User_Profile

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_profile(request):

    form = Profile_Form()

    if request.method == 'POST':

        form = Profile_Form(request.POST, request.FILES)

        if form.is_valid():

            user_pr = form.save(commit=False)

            user_pr.display_picture = request.FILES['display_picture']
            # imagefile = request.FILES['display_picture']
            # imagef = base64.b64encode(imagefile.read())
            # imagedecoded=base64.b64decode(imagef)
            # imagedecoded=BytesIO(imagedecoded)
            # metadata = exifread.process_file(imagedecoded)
            # print(metadata)
            file_type = user_pr.display_picture.url.split('.')[-1]
            
            file_type = file_type.lower()
            # print(file_type)
            if file_type not in IMAGE_FILE_TYPES:

                return render(request, 'create.html', {"form": form})

            user_pr.save()

            return render(request, 'details.html', {'user_pr': user_pr})

    context = {"form": form}

    return render(request, 'create.html', context)