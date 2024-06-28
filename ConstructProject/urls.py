
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ConstructApp.urls')),
    path('bm/', include('BmApp.urls')), 
    path('services/', include('servicesapp.urls')), 
    path('bookstore/', include('BookStoreApp.urls')), 
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)