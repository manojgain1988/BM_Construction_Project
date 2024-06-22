from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )
    title=models.CharField(max_length=150)
    keyword=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    company=models.CharField(max_length=50)
    address=models.CharField(blank=True,max_length=50)
    phone=models.CharField(blank=True,max_length=15)
    fax=models.CharField(blank=True,max_length=15)
    email=models.EmailField(blank=True,max_length=50)
    smtpserver=models.CharField(blank=True,max_length=50)
    smtpemail=models.CharField(blank=True,max_length=50)
    smtppassword=models.CharField(blank=True,max_length=50)
    smtpport=models.CharField(blank=True,max_length=5)
    icon=models.ImageField(blank=True,upload_to='images/')
    facebook=models.CharField(blank=True,max_length=50)
    instagram=models.CharField(blank=True,max_length=50)
    twitter=models.CharField(blank=True,max_length=50)
    youtube=models.CharField(blank=True,max_length=50)
    about=models.TextField(blank=True)
    contact=models.TextField(blank=True)
    references=models.TextField(blank=True)
    status=models.CharField(max_length=50 ,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    