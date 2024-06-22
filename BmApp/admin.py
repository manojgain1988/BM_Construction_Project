from django.contrib import admin
from BmApp. models import ConstructionCategory, ConstructionProject
# Register your models here.

class ConstructionCategoryAdmin(admin.ModelAdmin):
    list_display=['title','status','created_at','updated_at']
    list_filter=['status','created_at']
    prepopulated_fields={'slug':('title',)}
    

class ConstructionProjectAdmin(admin.ModelAdmin):
    list_display=['title','image_tag','status','created_at','updated_at']
    list_filter=['status','created_at']
    prepopulated_fields={'slug':('title',)}



admin.site.register(ConstructionCategory, ConstructionCategoryAdmin)
admin.site.register(ConstructionProject, ConstructionProjectAdmin)