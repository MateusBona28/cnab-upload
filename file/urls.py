from django.urls import path
from .views import uploader

urlpatterns = [
    path('', uploader, name='uploader')
]