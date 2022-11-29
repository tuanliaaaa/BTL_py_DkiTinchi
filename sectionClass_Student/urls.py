
from django.urls import path
from .sectionClassStudentViews import SectionClassStudentNow,SectionClassStudentByID,GetScheduleByTime
urlpatterns = [
    path('api/SectionClassStudentNow',SectionClassStudentNow.as_view()),
    path('api/SectionClassStudentByID/<int:id>',SectionClassStudentByID.as_view()),
    path('api/GetScheduleByTime/<int:id>',GetScheduleByTime.as_view()),
]