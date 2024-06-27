from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.Aboutus, name='about'),
    path('project/', views.Allprojects, name='project'),
    path('project/<int:id>/', views.Singleproject, name='singleproject'),
] 