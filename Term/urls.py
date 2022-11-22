
from django.urls import path
from Term.termViews import GetTermByNow
urlpatterns = [
    path('api/GetTermByNow',GetTermByNow.as_view()),
]