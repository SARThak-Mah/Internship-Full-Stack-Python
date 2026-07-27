from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('getform/', views.getform, name='getform'),
    path('data/', views.data, name='data'),
    path('myapp/', include('myapp.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
