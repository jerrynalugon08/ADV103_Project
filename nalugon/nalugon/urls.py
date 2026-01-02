"""
URL configuration for nalugon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from myapp.views import home
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('', views.home, name='home'),
path('gallery1/', views.gallery1, name='gallery1'),
path('gallery2/', views.gallery2, name='gallery2'),
path('gallery3/', views.gallery3, name='gallery3'),
path('gallery4/', views.gallery4, name='gallery4'),
path('about/', views.about, name='about'),

]

        







