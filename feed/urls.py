from feed import views
from django.urls import path


urlpatterns = [
    path('', views.feed, name='feed'),
]

