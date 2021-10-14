from django.urls import path, include
from .views import *

app_name = 'Item'

urlpatterns = [
    path('create/',ItemCreateAPIView.as_view(), name = 'add_item'),
    path('view/',ItemListAPIView.as_view(), name = 'list_item'),
]