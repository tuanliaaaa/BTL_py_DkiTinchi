from SubjectSign.settings import SECRET_KEY
from Student.studentModels import Student
from Account.accountModels import Account
import jwt
from rest_framework.response import Response
from rest_framework import status
import json
from django.http.response import HttpResponse
class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):   
        if 'Authorization' in request.headers:
            jwtTokenSplit=request.headers['Authorization'].split(' ')
            jwtTokenPayload = jwtTokenSplit[1]
            try:
                payLoad=jwt.decode(jwtTokenPayload, SECRET_KEY, algorithms=["HS256"])
                request.AccountID=payLoad['AccountID']
                request.Position=payLoad['Position']
                request.Group=payLoad['Group']
            except:
                return HttpResponse('{"message":"Token đã hết hạn"}',status =status.HTTP_403_FORBIDDEN)
        response = self.get_response(request)
        return response