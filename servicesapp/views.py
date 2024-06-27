from django.shortcuts import render,get_object_or_404
from servicesapp.models import Service,OurTeam
from ConstructApp.models import Setting

# Create your views here.

def ServicesView(request):
    services=Service.objects.all()
    setting = get_object_or_404(Setting, id=1)
    context={
        'setting':setting,
        'services':services,
    }
    return render(request,'service.html',context)



def TeamView(request):
    team=OurTeam.objects.all()
    setting = get_object_or_404(Setting, id=1)
    context={
        'setting':setting,
        'team':team,
    }
    return render(request,'teams.html',context)