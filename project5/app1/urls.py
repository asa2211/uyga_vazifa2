from django.urls import path
from .views import get_name, get_name2

urlpatterns = [
    path('', get_name),
    path('2/', get_name2)
]
