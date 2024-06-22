from django.shortcuts import render
from.models import Setting
from BmApp. models import ConstructionCategory, ConstructionProject
# Create your views here.

def Home(request):
    setting = Setting.objects.get(id=1)
    sliding_image = ConstructionProject.objects.all().order_by('-id')[:4]
    
    context={
        'setting': setting,
        'sliding_image': sliding_image
    }
    return render(request,'homebase.html', context)