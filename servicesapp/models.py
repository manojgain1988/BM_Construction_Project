from django.db import models
from BmApp. models import ConstructionCategory
# Create your models here.

class Service(models.Model):
    STATUS = (
        ('True' ,'True'),
        ('False' ,'Fales')
    )
    title=models.CharField(max_length=200)
    icon=models.CharField(max_length=200)
    image=models.ImageField(upload_to='services')
    details=models.TextField()
    status=models.CharField(max_length=200,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title
    
    
    
class OurTeam(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    name=models.CharField(max_length=200)
    spe_category=models.ForeignKey(ConstructionCategory,on_delete=models.CASCADE)
    facebook_url=models.CharField(max_length=200,blank=True ,null=True)
    twitter_url=models.CharField(max_length=200,blank=True ,null=True)
    instagram_url=models.CharField(max_length=200,blank=True ,null=True)
    linkedin_url=models.CharField(max_length=200,blank=True ,null=True)
    image=models.ImageField(upload_to='team_member/')
    details=models.TextField()
    status= models.CharField(max_length=30, choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""