
from django.urls import path
from .CreditRegistrationViews import CreditRegistration
urlpatterns = [
    path('',CreditRegistration.as_view()),
]