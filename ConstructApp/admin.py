from django.contrib import admin
from ConstructApp.models import Setting, ContactMessage



# Register your models here.

admin.site.register(Setting)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=['id','name','email','created_at','updated_at']

admin.site.register(ContactMessage, ContactMessageAdmin)


