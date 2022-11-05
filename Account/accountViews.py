# from types import prepare_class
# from django.http import HttpResponse, JsonResponse
# from rest_framework import status
# from rest_framework.response import Response
# from .userModel import User
# from rest_framework.decorators import APIView
# from .roleRequestDecorator import RoleRequest
# from rest_framework.decorators import api_view
# from django.utils.decorators import method_decorator
# from .userSerializer import UserSerializer
# from json import loads
# from django.views.decorators.csrf import csrf_exempt
# from django.http import Http404
# from rest_framework.parsers import JSONParser
# class UserInformationByToken(APIView):
#     # @method_decorator(RoleRequest(allowedRoles=['admin',]))
#     def get(self,request):
#         try:
#             user= User.objects.get(pk=request.userID)
#         except:
#             return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
#         userSerializer = UserSerializer(user)
#         return Response(userSerializer.data,status=status.HTTP_200_OK)