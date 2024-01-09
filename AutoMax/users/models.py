from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField, INPANCardNumberField

class Location(models.Model):
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)  
    state = INStateField(default="Delhi")
    pan_card = INPANCardNumberField(blank=True)

def __str__(self):
    return f'Location {self.id}'
    

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #we are going to create a property on our profile,
    photo = models.ImageField(null=True)                         #which i'm going to call user and this is going to
    bio = models.CharField(max_length=140, blank=True)           # be equal to models.OneToOneField   
    phone_number= models.CharField(max_length=10,blank=True)        
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    
    
     
    def __str__(self):
        return f'{self.user.username}\'s Profile' 
