from django.db import models
from PIL import Image
from PIL.ExifTags import TAGS
# import pandas as pd

from exiffield.fields import ExifField

import exifread
import os
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
class User_Profile(models.Model):

    fname = models.CharField(max_length=200)

    display_picture = models.FileField()

    def __str__(self):

        return self.fname
@receiver(post_save, sender=User_Profile)
def save_profile(sender, instance, **kwargs):
    # print(instance.display_picture.url, "great")
    img = open(f'{os.getcwd()}{instance.display_picture.url}', 'rb')
    print(img)
    tags = exifread.process_file(img, details=False, strict=True)
    for tag in tags.keys(): 
        print("%s: %s" % (tag, tags[tag]))
        # if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'EXIF MakerNote'):
        #     print("%s: %s" % (tag, tags[tag]))


class UploadImage(models.Model):
    image = models.ImageField(upload_to='image/')
    upload_file = models.FileField(upload_to='files/', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    exif = ExifField(
        source='image',
    )

@receiver(pre_save, sender=UploadImage)
def uploadImage(sender, instance, **kwargs):
    print(instance.exif)

# force_insert=False, force_update=False


    # def save(self, force_insert=False, force_update=False):
    #     if(self.image):

            # img = Image.open(self.image)
        

        #     exif_dict = img.info.get("exif")
        #     if exif_dict:
        #         result = {
        #                 "ImageSize": img.size,
        #                 "ImageHeight": img.height,
        #                 "ImageWidth": img.width,
        #                 "ImageFormat": img.format,
        #                 "ImageMode": img.mode
        #         }
        #         exifdata = img.getexif()
        #         for tagid in exifdata:
        #             tagname = TAGS.get(tagid, tagid)
        #             value = exifdata.get(tagid)
                 
        #             if tagname == 'UserComment' or tagname == 'MakerNote':
        #                 continue
                    
        #             result[tagname] = value
                
        #         print(result)
        #         # df = pd.DataFrame(data=result)
        #         # print(df)
                
        #     else:
        #         info_dict = {
        #                 "Filename": img.filename,
        #                 "Image Size": img.size,
        #                 "Image Height": img.height,
        #                 "Image Width": img.width,
        #                 "Image Format": img.format,
        #                 "Image Mode": img.mode,
        #                 "Image is Animated": getattr(img, "is_animated", False),
        #                 "Frames in Image": getattr(img, "n_frames", 1)
        #             }
        #         self.desc = info_dict
        #         print("hit the last part")
        #         for label,value in info_dict.items():
        #             print(f"{label}: {value}")

        
        # else:
        #     print('no image')
        # super(UploadImage, self).save(force_insert=False, force_update=False)    