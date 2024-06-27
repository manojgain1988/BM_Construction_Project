from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from.models import Setting,ContactForm,ContactMessage
from BmApp. models import ConstructionCategory, ConstructionProject
# Create your views here.



def Home(request):
    setting = get_object_or_404(Setting, id=1)
    sliding_image = ConstructionProject.objects.all().order_by('-id')[:4]
    
    context={
        'setting': setting,
        'sliding_image': sliding_image
    }
    return render(request,'homebase.html', context)



def Contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data=ContactMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Profiles Details Update')
            return redirect('contact')
        
    form=ContactForm()
    setting = Setting.objects.get(id=1)
    context={
        'form':form,
        'setting': setting,
        }
    return render(request,'contactMessage.html',context)



def Allprojects(request):
    setting = get_object_or_404(Setting, id=1)
    projects = ConstructionProject.objects.all()
    context={
        'setting': setting,
        'projects': projects,
    }
    return render(request,'project.html',context)
    



def Singleproject(request,id):
    setting = get_object_or_404(Setting, id=1)
    singlepro = get_object_or_404(ConstructionProject, id=id)
    context={
        'setting': setting,
        'singlepro': singlepro,
    }
    return render(request,'singleproject.html',context)
    


def Aboutus(request):
    setting = get_object_or_404(Setting, id=1)
    context={
        'setting': setting,       
    }
    return render(request,'about.html',context)
    