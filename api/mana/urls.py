from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_mana_list, name='post_mana_list'),
]