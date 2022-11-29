
from django.urls import path
from Term.termViews import GetSignSubjectByNow
urlpatterns = [
    path('api/GetSignSubjectByNow',GetSignSubjectByNow.as_view()),

]