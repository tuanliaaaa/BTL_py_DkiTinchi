# from re import I
# from unicodedata import category
# from django.http import HttpResponse
# from rest_framework import status
# from django.http import Http404
# from rest_framework.response import Response
# from sectionClass.sectionClassModels import sectionClass
# from datetime import datetime,timedelta,timezone
# from rest_framework.decorators import APIView
# from django.utils.decorators import method_decorator
# from SubjectSign.roleRequestDecorate import RoleRequest
# from rest_framework.parsers import JSONParser
# from sectionClass.sectionClassSerializer import SectionClassSerializer
# from datetime import datetime
# class GetTermByNow(APIView):
#    # @method_decorator(RoleRequest(allowedRoles=['Admin',]))
#     def get(self,request):
#         print(datetime.now())
#         sectionClasss = sectionClass.objects.filter(>datetime.now())
#         sectionClassSerializer = SectionClassSerializer(sectionClasss,many=True)
#         return Response(sectionClassSerializer.data,status=status.HTTP_200_OK)
