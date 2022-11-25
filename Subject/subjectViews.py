from django.http import HttpResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from Subject.subjectModels import Subject
from Subject.subjectSerializer import SubjectSerializer
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from Student.studentModels import Student
from django.utils.decorators import method_decorator
from SubjectSign.roleRequestDecorate import RoleRequest, PotisionRequest
from rest_framework.parsers import JSONParser
from SubjectMajor.subjectMajormodels import SubjectMajor
from datetime import datetime
class GetSubjectByTermNow(APIView):
    def get_student_by_account(self, account__pk):
        try:
            return Student.objects.get(account__pk=account__pk)
        except Student.DoesNotExist:
            raise Http404
    # @method_decorator(PotisionRequest(allowedPositions=['Student',]))
    def get(self,request):
        student = self.get_student_by_account(request.AccountID)
        studentCode = student.studentCode
        year=(datetime.now().year-2000-int(studentCode[1:3]))*2
        if(datetime.now().month>8):
            year+=1
        subjectMajors = SubjectMajor.objects.filter(major__majorCode=studentCode[5:7], startTerm = year)
        subjects =[subjectMajor.subject for subjectMajor in subjectMajors]
        subjectSerializer = SubjectSerializer(subjects,many=True)
        return Response(subjectSerializer.data,status=status.HTTP_200_OK)
class GetSubjectBySubjectCode(APIView):
    def get(self,request,subjectCode):
        subjects = Subject.objects.filter(SubjectCode=subjectCode)
        subjectSerializer = SubjectSerializer(subjects,many=True)
        return Response(subjectSerializer.data,status=status.HTTP_200_OK)