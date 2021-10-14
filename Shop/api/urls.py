from django.urls import include, path
from .views import *

app_name = 'Shop'

urlpatterns = [
    path('create/',ShopCreateAPIView.as_view(), name = 'create'),
    path('detail/<int:pk>/',ShopRetrieveAPIView.as_view(), name = 'detail'), 
    path('detail_list/',ShopListAPIView.as_view(), name = 'detail_list'),
    path('update/', ShopUpdateAPIView.as_view(), name = 'update'),
    path('detail_update/', ShopRetrieveUpdateAPIView.as_view(), name = 'update'),

]
