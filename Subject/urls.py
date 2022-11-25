
from django.urls import path
from .subjectViews import GetSubjectByTermNow,GetSubjectBySubjectCode
urlpatterns = [
    path('api/GetSubjectByTermNow',GetSubjectByTermNow.as_view()),
    path('api/GetSubjectBySubjectCode/<str:subjectCode>',GetSubjectBySubjectCode.as_view()),
]