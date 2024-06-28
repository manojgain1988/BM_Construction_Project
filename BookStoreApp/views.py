from django.shortcuts import render, get_object_or_404
from ConstructApp.models import Setting

# Create your views here.
def AllBook(request):
    setting = get_object_or_404(Setting, id=1)
    context={
        'setting': setting,
    }
    return render(request,'book.html',context)