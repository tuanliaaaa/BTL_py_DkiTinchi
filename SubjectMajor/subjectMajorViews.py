
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from .subjectMajormodels import SubjectMajor
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.parsers import JSONParser
class SubjectMajorInformationByToken(APIView):
    def get(self,request):
        pass
