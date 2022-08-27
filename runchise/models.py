from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=20,blank=False, default='')
    email = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=200,blank=False, default='')
