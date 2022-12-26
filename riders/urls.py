from riders import views
from django.urls import path


urlpatterns = [
    path('', views.riders, name='riders'),
]

