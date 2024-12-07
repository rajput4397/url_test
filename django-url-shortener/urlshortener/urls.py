"""
URL configuration for urlshortener project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.contrib import admin
# from django.urls import path
# from shortener import views  # Import views from the shortener app

# urlshortener/urls.py

from django.urls import path
from shortener import views
from django.contrib import admin
# from .views import redirect_to_original

urlpatterns = [
    path('', views.home, name='home'),  # Home page (Main page with buttons)
    path('shorten/', views.shorten_url, name='shorten_url'),  # Shorten URL page
    path('visit/', views.visit_url, name='visit_url'), 
    path('admin/', admin.site.urls), # Visit URL page
    path('enquire/', views.enquire, name='enquire'), 
    path('check-url/', views.check_url, name='check_url'),
    path('redirect/<str:tiny_url>/', views.redirect_to_original, name='redirect_to_original'),
    path('enquire_url/<str:tiny_url>/',views.enquire_url,name='enquire_url'),
]


