from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #we are going to create a property on our profile,
    photo = models.ImageField(null=True)                         #which i'm going to call user and this is going to
    bio = models.CharField(max_length=140, blank=True)           # be equal to models.OneToOneField   
    phone_number= models.CharField(max_length=10,blank=True)        
     
    
