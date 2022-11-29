
from django.urls import path
from .sectionClassStudentViews import SectionClassStudentNow,SectionClassStudentByID
urlpatterns = [
    path('api/SectionClassStudentNow',SectionClassStudentNow.as_view()),
    path('api/SectionClassStudentByID/<int:id>',SectionClassStudentByID.as_view()),

]