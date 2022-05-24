from django.db import models
import os
from datetime import datetime

def upload_card_img(instance, filename):
    ext = filename.split('.')[-1]
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = "{}.{}.{}".format(
        str(instance.title.lower().replace(' ', '_')), ts, ext)
    return os.path.join('homecards', name)

class Cards (models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    photo = models.ImageField(upload_to=upload_card_img)

    def __str__(self):
        return '%s' % (self.title)