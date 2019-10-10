from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# GET /mana # Returns a list of mana
# GET /mana/<id> # Returns information for a specific mana
# GET /mana?search= # Search mana
# POST /mana # Create a new mana
# PUT /mana/<id> # Completely modifies a specific mana
# PATCH /mana/<id> # Partially updates a specific mana
# DELETE /mana/<id> # Remove a specific mana
router.register(r'list', views.ManaViewSet, basename='mana')
router.register(r'subscribe', views.SubscribedManaViewSet, basename='subscribed_mana')

urlpatterns = [
    path('', include(router.urls)),
]

