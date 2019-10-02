from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

# /rest-auth/login/ (POST)
# /rest-auth/logout/ (POST)
# /rest-auth/password/reset/ (POST)
# /rest-auth/password/reset/confirm/ (POST)
# /rest-auth/password/change/ (POST)
# /rest-auth/user/ (GET, PUT, PATCH)