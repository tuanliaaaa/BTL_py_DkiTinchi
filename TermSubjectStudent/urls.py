
from django.urls import path
from .termSubjectStudentViews import GetTermSubjectStudentNow,TermSubjectStudentBysubjectCode,GetTermSubjectStudentNear
urlpatterns = [
    path('api/GetTermSubjectStudentNow',GetTermSubjectStudentNow.as_view()),
    path('api/GetTermSubjectStudentNear',GetTermSubjectStudentNear.as_view()),
    path('api/TermSubjectStudentBysubjectCode/<str:subjectCode>',TermSubjectStudentBysubjectCode.as_view()),
]