from django.urls import path
from . import views

urlpatterns = [
    path('', views.avatar_character_list, name = 'characters'),
]