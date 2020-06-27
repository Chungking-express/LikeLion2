from django.db import models


class upload(models.Model):
    photo = models.ImageField (upload_to="image",blank = True)
    comment = models.TextField (default='간단한 설명')    

# Create your models here.
