from django.http import HttpResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from.sectionClass_StudentModels import sectionClassStudent
from .sectionClassStudentSerializer import SectionClassStudentSerializer
from SubjectSign.roleRequestDecorate import RoleRequest, PotisionRequest
from rest_framework.parsers import JSONParser
from Term.termModels import Term
from Student.studentModels import Student
from sectionClass.sectionClassModels import sectionClass
class SectionClassStudentNow(APIView):
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
    def get_sectionclass_by_id(self, pk):
        try:
            return sectionClass.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    def get(self,request):
        terms = self.get_term_by_now()
        student = self.get_student_by_account(request.AccountID)
        sectionClassStudents = sectionClassStudent.objects.filter(studentID=student,sectionClassID__term=terms)
        sectionClassStudentserializer=[]
        for sectionClasssStudent in sectionClassStudents:
            print(sectionClasssStudent.__dict__)
            sectionClassStudentJson={}
            sectionClassStudentJson["id"]=sectionClasssStudent.pk
            sectionClassStudentJson["classSection"]=sectionClasssStudent.sectionClassID.pk
            sectionClassStudentJson["SubjectCode"]=sectionClasssStudent.sectionClassID.subjectMajor.subject.SubjectCode
            sectionClassStudentJson["SubjectName"]=sectionClasssStudent.sectionClassID.subjectMajor.subject.SubjectName
            sectionClassStudentserializer.append(sectionClassStudentJson)
        return Response(sectionClassStudentserializer,status=status.HTTP_200_OK)
    def post(self,request):
        try:
            self.get_term_by_now()
        except:
            return Response({"message":"Không có quyền sửa"},status=status.HTTP_404_NOT_FOUND)
        student = self.get_student_by_account(request.AccountID)
        sectionClassRequest =sectionClass.objects.get(pk=request.data["id"])
        if sectionClassRequest.quanlityReal>= sectionClassRequest.quanlity:
            return Response({"message":"Lớp đã đầy"},status=status.HTTP_404_NOT_FOUND)
        if sectionClassStudent.objects.filter(sectionClassID=sectionClassRequest,studentID=student):
            return Response({"message":"Môn đã được đăng kí"},status=status.HTTP_404_NOT_FOUND)
        lessonListRequest =sectionClassRequest.dayLessonList
        sectionClassStudents=sectionClassStudent.objects.filter(studentID=student)
        lessons =[ sectionsClassStudent.sectionClassID.dayLessonList for sectionsClassStudent in sectionClassStudents]
        lessonList=[]
        lessonListRequests=[]
        for lesson in lessons:
            a=lesson.split(" ")
            for i in a:
                b=i[:-2]
                for z in range(1,int(i[-2])+1):
                    lessonList.append(b+str(z)+")")
        lessons=lessonListRequest.split(" ")
        for lesson in lessons:
            a=lesson.split(" ")
            for i in a:
                b=i[:-2]
                for z in range(1,int(i[-2])+1):
                    lessonListRequests.append(b+str(z)+")")
        for i in lessonListRequests:
            if i in lessonList:
                return Response({"message":"Trùng Lịch học"},status=status.HTTP_404_NOT_FOUND)
        sectionClassStudentNew =sectionClassStudent(studentID=student,sectionClassID=sectionClassRequest)
        sectionClassStudentNew.save()
        sectionClassStudentSerializer=SectionClassStudentSerializer(sectionClassStudentNew)
        return Response(sectionClassStudentSerializer.data,status=status.HTTP_201_CREATED)
class SectionClassStudentByID(APIView):
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
    def get_sectionclass_by_id(self, pk):
        try:
            return sectionClass.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    def delete(self,request,id):
        try:
            self.get_term_by_now()
        except:
            return Response({"message":"Không có quyền sửa"},status=status.HTTP_404_NOT_FOUND)
        student = self.get_student_by_account(request.AccountID)
        sectionClasss=sectionClass.objects.get(pk=id)
        sectionClassStudentDelete =sectionClassStudent.objects.get(studentID=student,sectionClassID=sectionClasss)
        sectionClassStudentDelete.delete()
        return Response({"mesage":"đã xóa thành công"},status=status.HTTP_204_NO_CONTENT)
