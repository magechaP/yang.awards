from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.dispatch import receiver
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_pic = models.ImageField(default='image.png',upload_to='profiles/')
    bio = HTMLField(max_length=500,default='About me')
    phone_number = models.CharField(max_length=10,default=000000)
    website = URLOrRelativeURLField() 
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    def update_profile(self):
        self.update()
        
    @classmethod
    def search_profile(cls,username):
        profile=Profile.objects.filter(user_id=username)
        
        return profile

    
    def __str__(self):
        return self.bio