"""ridepoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

#test commit code changes, test

from django.contrib import admin
from django.urls import path, include
from feed import urls
from feed import views as feed_views
from riders import views as rider_views
from django.contrib.auth import views as authentication_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('feed', include('feed.urls')),
    path('riders', include('riders.urls')),
    path('admin/', admin.site.urls),
    path('register/', rider_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='riders/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='riders/logout.html'), name='logout'),


]
