from rest_auth.registration.views import VerifyEmailView
from django.urls import include, path, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'accounts-rest/registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'accounts-rest/registration/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
]

# https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html

# /rest-auth/login/ (POST)
# /rest-auth/logout/ (POST)
# /rest-auth/password/reset/ (POST)
# /rest-auth/password/reset/confirm/ (POST)
# /rest-auth/password/change/ (POST)
# /rest-auth/user/ (GET, PUT, PATCH)

# /rest-auth/registration/ (POST)
# /rest-auth/registration/verify-email/ (POST)
