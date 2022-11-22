from re import I
from unicodedata import category
from django.http import HttpResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from Term.termModels import Term
from Term.termSerializer import TermSerializer
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from SubjectSign.roleRequestDecorate import RoleRequest
from rest_framework.parsers import JSONParser
from datetime import datetime
class GetTermByNow(APIView):
   # @method_decorator(RoleRequest(allowedRoles=['Admin',]))
    def get(self,request):
        terms = Term.objects.filter(StartTimeSignTerm__lte=datetime.now(),EndTimeSignTerm__gte=datetime.now())| Term.objects.filter(StartTimeSignSubject__lte=datetime.now(),EndTimeSignSubject__gte=datetime.now())
        termSerializer = TermSerializer(terms,many=True)
        return Response(termSerializer.data,status=status.HTTP_200_OK)
