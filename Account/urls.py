from django.urls import path
from .tokenViews import TokenApi
from .accountTemplateView import Login
urlpatterns = [
    path('api/Token',TokenApi.as_view(),name="TokenApi"),
    path('Login',Login.as_view()),
]
