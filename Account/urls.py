from django.urls import path
from .tokenViews import TokenApi
urlpatterns = [
    path('api/Token',TokenApi.as_view(),name="TokenApi"),
]
