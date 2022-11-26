
from django.urls import path
from .termSubjectStudentViews import GetTermSubjectStudentNow,TermSubjectStudentBysubjectCode,GetTermSubjectStudentNear,SubjectByTermNear,SubjectByTermNow  
urlpatterns = [
    path('api/GetTermSubjectStudentNow',GetTermSubjectStudentNow.as_view()),
    path('api/GetTermSubjectStudentNear',GetTermSubjectStudentNear.as_view()),
    path('api/SubjectByTermNear',SubjectByTermNear.as_view()),
    path('api/SubjectByTermNow',SubjectByTermNow.as_view()),
    path('api/TermSubjectStudentBysubjectCode/<str:subjectCode>',TermSubjectStudentBysubjectCode.as_view()),
]