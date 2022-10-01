from django.urls import path
from . import loginView 
urlpatterns = [
    path('Login', loginView.Login),
]