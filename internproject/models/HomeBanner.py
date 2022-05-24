from django.db import models
import os
import datetime

def upload_banner_img(instance, filename):
    ext = filename.split('.')[-1]
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = "{}.{}.{}".format(
        str(instance.title.lower().replace(' ', '_')), ts, ext)
    return os.path.join('homebanner', name)

class HomeBanner (models.Model):
    title = models.CharField(max_length=64)
    photo = models.ImageField(upload_to=upload_banner_img)

    def __str__(self):
        return '%s' % (self.title)