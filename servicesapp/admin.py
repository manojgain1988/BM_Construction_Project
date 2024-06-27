from django.contrib import admin
from servicesapp.models import Service ,OurTeam


# Register your models here.
class Serviceadmin(admin.ModelAdmin):
    list_display=['id','title','created_at','updated_at','status']

class OurTeamAdmin(admin.ModelAdmin):
    list_display=['id','name','created_at','updated_at','status']
    
    
    
admin.site.register(Service, Serviceadmin)  
admin.site.register(OurTeam, OurTeamAdmin)