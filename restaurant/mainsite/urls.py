from django.urls import path
from .views import Home

app_name = 'mainsite'

urlpatterns = [
    path('', Home, name='Home'),
]