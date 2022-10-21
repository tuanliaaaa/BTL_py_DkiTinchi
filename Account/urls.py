from django.urls import path
from .accountViews import TokenApi
urlpatterns = [
    path('api/Token',TokenApi.as_view(),name="TokenApi"),
]
