from django.db import models

# Create your models here.


class Empower(models.Model):
    user_name = models.CharField(max_length=200,default='')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    email = models.EmailField()