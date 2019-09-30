from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_episode_list, name='post_episode_list'),
]