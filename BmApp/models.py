from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class ConstructionCategory(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )
    title=models.CharField(max_length=200)
    keywords=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to='category/')
    details=models.TextField(blank=True)
    status=models.CharField(max_length=50 ,choices=STATUS)
    slug=models.SlugField(null=True, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    

    
class ConstructionProject(models.Model):
    STATUS =(
        ('True', 'True'),
        ('False', 'False'),
    )
    category=models.ForeignKey(ConstructionCategory, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    keywords=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to='product/')
    new_price=models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price=models.DecimalField(decimal_places=2, max_digits=15)
    amount=models.IntegerField(default=0)
    min_amount=models.IntegerField(default=3)
    details=models.TextField(blank=True)
    status=models.CharField(max_length=50 ,choices=STATUS)
    slug=models.SlugField(null=True, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""
    
    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" /> '.format(self.image.url))
    image_tag.short_description = 'Image'
