from sectionClass.sectionClassModels import sectionClass
from unicodedata import category
from django.http import HttpResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from SubjectSign.roleRequestDecorate import RoleRequest
from rest_framework.parsers import JSONParser
from sectionClass.sectionClassSerializer import SectionClassSerializer
from datetime import datetime
class SectionClassApi(APIView):
   # @method_decorator(RoleRequest(allowedRoles=['Admin',]))
    def get(self,request,id):
        sectionClasss = sectionClass.objects.filter(subjectMajor__pk=id)
        sectionClassList=[]
        for sectionClas in sectionClasss:
            sectionClassDetail={}
            sectionClassDetail["id"]=sectionClas.pk
            sectionClassDetail["quanlity"] =sectionClas.quanlity
            sectionClassDetail["quanlityReal"]=sectionClas.quanlityReal
            sectionClassDetail["dayDefault"]=sectionClas.dayDefault
            sectionClassDetail["dayLessonList"]=sectionClas.dayLessonList
            sectionClassDetail["Teacher"]=sectionClas.teacherID.fullName
            sectionClassDetail["subjectName"]=sectionClas.subjectMajor.subject.SubjectName
            sectionClassDetail["subjectCode"]=sectionClas.subjectMajor.subject.SubjectCode
            sectionClassList.append(sectionClassDetail)
        return Response(sectionClassList,status=status.HTTP_200_OK)
