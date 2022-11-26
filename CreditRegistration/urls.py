
from django.urls import path
from .CreditRegistrationViews import SubjecttRegistration,CreditRegistration
urlpatterns = [
    path('subject',SubjecttRegistration.as_view()),
    path('credit',CreditRegistration.as_view()),
]