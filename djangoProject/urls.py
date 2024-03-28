"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from djangoProject import settings
from dz6app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dz6app/', include('dz6app.urls', namespace='dz6app')),
    path('', views.my_page, name='my_page'),
    path('success/', views.save_success, name='save-success'),
    path('__debug__/', include("debug_toolbar.urls")),
    path('template/', views.total_in_template, name='template'),
    path('subscribe/', views.subscribe, name='subscribe'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)