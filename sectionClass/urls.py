
from django.urls import path
from sectionClass.sectionClassviews import SectionClassApi
urlpatterns = [
    path('api/SectionClassApi/<int:id>',SectionClassApi.as_view()),
]