from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField('img', upload_to='images/')