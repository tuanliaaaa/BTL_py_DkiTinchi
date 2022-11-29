from django.shortcuts import render
from django.views import View
# Create your views here.

class SubjecttRegistration(View):    
    def get(self,request):
        return render(request,"subjectRegistration.html")
class CreditRegistration(View):    
    def get(self,request):
        return render(request,"creditRegistration.html")
class Schedule(View):
    def get(self,request):
        return render(request,"schedule.html")