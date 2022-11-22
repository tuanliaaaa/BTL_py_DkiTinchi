
from rest_framework import status
from rest_framework.response import Response
from SubjectSign.roleRequestDecorate import RoleRequest
from SubjectSign.settings import SECRET_KEY
import jwt
from Student.studentModels import Student
from .accountModels import Account
from datetime import datetime, timedelta, timezone
from rest_framework.decorators import APIView
from django.views.decorators.csrf import csrf_exempt
from AccountGroup.accountGroupModels import AccountGroup
from Group.groupModels import Group
from Student.studentSerializer import StudentSerializer
from django.utils.decorators import method_decorator
class TokenApi(APIView):    
    @csrf_exempt
    #@method_decorator(RoleRequest(allowedRoles=['NomalUser',]))
    def post(self,request):
        exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        accountRequestToken =request.data     
        if 'username' not in accountRequestToken or not accountRequestToken['username']:
            return Response({"message":"Vui lòng nhập UserName"},status=status.HTTP_400_BAD_REQUEST)
        if 'password' not in accountRequestToken or not accountRequestToken['password']:
            return Response({"message":"Vui lòng nhập Password"},status=status.HTTP_400_BAD_REQUEST)
        try:
            account= Account.objects.get(username=accountRequestToken['username'],password=accountRequestToken['password'])
        except:      
            return Response({"message":"User này không tồn tại"},status=status.HTTP_404_NOT_FOUND)
        groups=[]
        groupUsers=AccountGroup.objects.filter(account=account)
        for gruopUser in groupUsers:
            groups.append(gruopUser.group.groupName)
        try:
            students = Student.objects.filter(account=account)[0]
            student = {"id": students.pk,"studentCode": students.studentCode,"email": students.email,"account":students.account.pk,"fullName":students.fullName}
        except:
            student = ""
        payLoad = {'AccountID':account.pk,"username":account.username,"Group":groups,"exp":exp,"student":student}
        jwtData = jwt.encode(payLoad,SECRET_KEY,) 
        
        payLoad=jwt.decode(jwtData, SECRET_KEY, algorithms=["HS256"])
        print(payLoad)
        jwtUser={"access":jwtData}
        return Response(jwtUser,status=status.HTTP_200_OK)
