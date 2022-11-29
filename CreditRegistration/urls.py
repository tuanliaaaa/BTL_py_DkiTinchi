
from django.urls import path
from .CreditRegistrationViews import SubjecttRegistration,CreditRegistration,Schedule
urlpatterns = [
    path('subject',SubjecttRegistration.as_view()),
    path('credit',CreditRegistration.as_view()),
    path('schedule',Schedule.as_view()),
]