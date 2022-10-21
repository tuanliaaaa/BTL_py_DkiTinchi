\
from rest_framework import status
from rest_framework.response import Response

from SubjectSign.settings import SECRET_KEY
import jwt
from .accountModels import Account
from datetime import datetime, timedelta, timezone
from rest_framework.decorators import APIView
from django.views.decorators.csrf import csrf_exempt


class TokenApi(APIView):
    @csrf_exempt
    def post(self, request):
        exp = datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        accountRequestToken = request.data
        if 'username' not in accountRequestToken or not accountRequestToken['username']:
            return Response({"message": "Vui lòng nhập UserName"}, status=status.HTTP_400_BAD_REQUEST)
        if 'password' not in accountRequestToken or not accountRequestToken['password']:
            return Response({"message": "Vui lòng nhập Password"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            account = Account.objects.get(username=accountRequestToken['username'], password=accountRequestToken['password'])
        except:
            return Response({"message": "User này không tồn tại"}, status=status.HTTP_404_NOT_FOUND)
        payLoad = {'UserID': account.pk, "UserName": account.username, "exp": exp}
        jwtData = jwt.encode(payLoad, SECRET_KEY,)
        jwtUser = {"access": jwtData}
        return Response(jwtUser, status=status.HTTP_200_OK)
