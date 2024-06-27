from django.db import models
from django.forms import ModelForm, TextInput, EmailInput



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
    
    
    
    
    
class ContactMessage(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=40)
    subject=models.CharField(max_length=200, blank=True)
    message=models.TextField(max_length=1000, blank=True)
    status=models.CharField(max_length=50 ,choices=STATUS,default='New')
    ip=models.CharField(max_length=200, blank=True)
    Note=models.CharField(max_length=200, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
     
    def __str__(self):
        return self.name
    
class ContactForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields= ['name','email','message'] 
        widgets= {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Name & Sure name'}),
            'email': EmailInput(attrs={'class' : 'input', 'placeholder' : 'Write your email'}),
            'message': TextInput(attrs={'class' : 'input', 'placeholder' : 'Write your message'}),
        }  

    