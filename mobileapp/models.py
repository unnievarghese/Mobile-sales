from django.db import models

class mobile_model(models.Model):
    part_number=models.CharField(max_length=120,unique=True)
    manufacturer=models.CharField(max_length=120)
    mobile_name=models.CharField(max_length=120)
    model_name=models.CharField(max_length=120)
    mobile_image=models.ImageField(upload_to='images')
    color=models.CharField(max_length=120)
    price=models.IntegerField(default=50)

    def __str__(self):
        return self.model_name

class buyer_model(models.Model):
    buyer_name=models.CharField(max_length=120)
    buyer_address=models.TextField(max_length=500)
    buyer_mobile=models.CharField(max_length=100)
    product=models.CharField(max_length=150,null=True)
    user=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.status

from django.contrib.auth.models import AbstractUser, UserManager