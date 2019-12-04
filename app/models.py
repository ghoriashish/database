from django.db import models

# Create your models here.
class user(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    profile_pic=models.ImageField(upload_to='img/',default='doc_male.png')
