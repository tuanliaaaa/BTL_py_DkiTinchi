from types import prepare_class
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from Student.studentModels import Student
from Term.termModels import Term
from TermSubjectStudent.termSubjectStudentModels import TermSubjectStudent
from Subject.subjectModels import Subject
from Subject.subjectSerializer import SubjectSerializer
from Term.termSerializer import TermSerializer
from datetime import datetime
from rest_framework.decorators import APIView
from SubjectSign.roleRequestDecorate import RoleRequest,PotisionRequest
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from json import loads
import json
from sectionClass.sectionClassModels import sectionClass
from Major.majorModels import Major
from SubjectMajor.subjectMajormodels import SubjectMajor
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.parsers import JSONParser
from TermSubjectStudent.termSubjectStudentSerializer import TermSubjectStudentSerializer
# Create your views here.
class GetTermSubjectStudentNow(APIView):
    def get_student_by_account(self, account__pk):
        try:
            return Student.objects.get(account__pk=account__pk)
        except Student.DoesNotExist:
            raise Http404
    def get_term_by_now(self):
        try:
            return Term.objects.get(StartTimeSignTerm__lte=datetime.now(),EndTimeSignTerm__gte=datetime.now())
        except Term.DoesNotExist:
            raise Http404
    def get(self,request):
        terms = self.get_term_by_now()
        student = self.get_student_by_account(request.AccountID)
        termSubjectStudents= TermSubjectStudent.objects.filter(student=student,term=terms)
        subjects = [termSubjectStudent.subjectMajor.subject for termSubjectStudent in termSubjectStudents]
        subjectsJson = SubjectSerializer(subjects,many=True)
        return Response(subjectsJson.data,status=status.HTTP_200_OK)
    # @csrf_exempt
    def post(self,request):
        terms = self.get_term_by_now()
        student = self.get_student_by_account(request.AccountID)
        major = Major.objects.get(majorCode=student.studentCode[5:7])
        subjectMajor =SubjectMajor.objects.get(subject__SubjectCode=request.data['subjectCode'],major=major)
        termSubjectStudentNew = TermSubjectStudent(term=terms,student=student,subjectMajor=subjectMajor)
        termSubjectStudentNew.save()
        termSubjectStudentNewJson= TermSubjectStudentSerializer(termSubjectStudentNew)
        return Response(termSubjectStudentNewJson.data, status=201)

class TermSubjectStudentBysubjectCode(APIView):
    def get_student_by_account(self, account__pk):
        try:
            return Student.objects.get(account__pk=account__pk)
        except Student.DoesNotExist:
            raise Http404
    def get_term_by_now(self):
        try:
            return Term.objects.get(StartTimeSignTerm__lte=datetime.now(),EndTimeSignTerm__gte=datetime.now())
        except Term.DoesNotExist:
            raise Http404
    def delete(self,request,subjectCode):    
        terms = self.get_term_by_now()
        student = self.get_student_by_account(request.AccountID)
        major = Major.objects.get(majorCode=student.studentCode[5:7])
        subjectMajor = SubjectMajor.objects.get(subject__SubjectCode=subjectCode,major=major)
        try:
            termSubjectStudent = TermSubjectStudent.objects.get(term=terms,student=student,subjectMajor=subjectMajor)
            termSubjectStudent.delete()
        except:
            return Response({'massage':'Categorie Không Tồn Tại'},status=status.HTTP_404_NOT_FOUND)
        return Response({'massage':'Categorie đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
class GetTermSubjectStudentNear(APIView):
    def get_term_by_near(self):
        try:
            return Term.objects.all().order_by("-EndTimeSignTerm")[0]
        except Term.DoesNotExist:
            raise Http404
    def get_student_by_account(self, account__pk):
        try:
            return Student.objects.get(account__pk=account__pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self,request):
        terms = self.get_term_by_near()
        student = self.get_student_by_account(request.AccountID)
        termSubjectStudents= TermSubjectStudent.objects.filter(student=student,term=terms)
        subjects = [termSubjectStudent.subjectMajor.subject for termSubjectStudent in termSubjectStudents]
        subjectsJson = SubjectSerializer(subjects,many=True)
        return Response(subjectsJson.data,status=status.HTTP_200_OK)
class SubjectByTermNear(APIView):
    def get_term_by_near(self):
        try:
            return Term.objects.all().order_by("-EndTimeSignSubject")[0]
        except Term.DoesNotExist:
            raise Http404
    def get_student_by_account(self, account__pk):
        try:
            return Student.objects.get(account__pk=account__pk)
        except Student.DoesNotExist:
            raise Http404
    def get(self,request):
        terms = self.get_term_by_near()
        student = self.get_student_by_account(request.AccountID)
        termSubjectStudents= TermSubjectStudent.objects.filter(student=student,term=terms)
        subjects=[]
        for termSubjectStudent in termSubjectStudents:
            subject ={}
            subject['SubjectCode'] = termSubjectStudent.subjectMajor.subject.SubjectCode
            subject['SubjectName']=termSubjectStudent.subjectMajor.subject.SubjectName
            subject['MajorSubjectID'] =termSubjectStudent.subjectMajor.pk
            subjects.append(subject)    
        return Response(subjects,status=status.HTTP_200_OK)
class SubjectByTermNow(APIView):
    def get_term_by_now(self):
        try:
            return Term.objects.get(StartTimeSignSubject__lte=datetime.now(),EndTimeSignSubject__gte=datetime.now())
        except Term.DoesNotExist:
            raise Http404
    def get_student_by_account(self, account__pk):
        try:
            return Student.objects.get(account__pk=account__pk)
        except Student.DoesNotExist:
            raise Http404
    def get(self,request):
        terms = self.get_term_by_now()
        student = self.get_student_by_account(request.AccountID)
        termSubjectStudents= TermSubjectStudent.objects.filter(student=student,term=terms)
        subjects=[]
        for termSubjectStudent in termSubjectStudents:
            subject ={}
            subject['SubjectCode'] = termSubjectStudent.subjectMajor.subject.SubjectCode
            subject['SubjectName']=termSubjectStudent.subjectMajor.subject.SubjectName
            subject['MajorSubjectID'] =termSubjectStudent.subjectMajor.pk
            subjects.append(subject)    
        return Response(subjects,status=status.HTTP_200_OK)
class TermStudentSign(APIView):
    def get_student_by_account(self, account__pk):
        try:
            return Student.objects.get(account__pk=account__pk)
        except Student.DoesNotExist:
            raise Http404
    def get(self,request):
        student = self.get_student_by_account(request.AccountID)
        termStudentSigns =TermSubjectStudent.objects.values("term").filter(student=student).annotate(Count('id'))
        termsListID =[ Term.objects.get(pk=termStudentSign["term"]) for termStudentSign in termStudentSigns]
        termSerializer=TermSerializer(termsListID,many=True)
        return Response(termSerializer.data,status=status.HTTP_200_OK)
class TimeByTermID(APIView):
    def get(self,request,id):
        term = Term.objects.get(pk=id)
        termSerializer=TermSerializer(term)
        return Response(termSerializer.data,status=status.HTTP_200_OK)
        
