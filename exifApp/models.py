from django.db import models
from PIL import Image
import os
from PIL.ExifTags import TAGS

import piexif

class UploadImage(models.Model):
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to='image/')
    desc = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
# force_insert=False, force_update=False
    def save(self, force_insert=False, force_update=False):
        if(self.image):
            print(self.image.url)
            img = Image.open(self.image)
            exif_dict = img.info.get("exif")
            if exif_dict:
                
                exifdata = img.getexif()
                for tagid in exifdata:
                    tagname = TAGS.get(tagid, tagid)
  
                   
                    value = exifdata.get(tagid)
                    
                   
                    print(f"{tagname:25}: {value}")
                    # print(tagname)

                #     # get the tag name, instead of human unreadable tag id
                #     tag = TAGS.get(tag_id, tag_id)
                #     data = exifdata.get(tag_id)
                #     # decode bytes 
                #     if isinstance(data, bytes):
                #         data = data.decode()
                #     # print(f"{tag:25}: {data}")
                #     dict_meta = {tag: data}
                  
                
            else:
                info_dict = {
                        "Filename": img.filename,
                        "Image Size": img.size,
                        "Image Height": img.height,
                        "Image Width": img.width,
                        "Image Format": img.format,
                        "Image Mode": img.mode,
                        "Image is Animated": getattr(img, "is_animated", False),
                        "Frames in Image": getattr(img, "n_frames", 1)
                    }
                self.desc = info_dict
                # for label,value in info_dict.items():
                #     print(f"{label:25}: {value}")

        
        else:
            print('no image')
        super(UploadImage, self).save(force_insert=False, force_update=False)    