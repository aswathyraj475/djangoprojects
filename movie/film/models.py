from django.db import models

class Film(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)
    cover=models.ImageField(upload_to='film/img',null=True,blank=True)

