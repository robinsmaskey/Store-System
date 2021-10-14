from django.urls import path
from .views import *

app_name = 'User'

urlpatterns = [
    path('signup/',SignupAPIView.as_view(), name = 'signup'),
    path('login/',LoginAPIView.as_view(), name = 'login'),
    path('password/change/',PasswordChangeAPIView.as_view(),name='pwd_change'),
    path('profile/detail/', ProfileView.as_view(), name='profile_retrieve'),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile_update'),
    path('profile/', ProfileDetailUpdateAPIView.as_view(), name='profile_retrieve_update'),



]