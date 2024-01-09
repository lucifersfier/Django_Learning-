from django.contrib import admin

# Register your models here.
from .models import Profile, Location

'''i am going to basically create a class which i am going to call profile admin '''

class ProfileAdmin(admin.ModelAdmin):
    pass
class LocationAdmin(admin.ModelAdmin):
    pass
#register function register the model for the admin panel so that the admin panel doesn't displays it.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)