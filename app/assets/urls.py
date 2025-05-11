from django.urls import path
from . import views

app_name = 'assets'

urlpatterns = [
    path('', views.home, name='home'),
] 