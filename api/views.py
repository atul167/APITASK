from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class SignUpAPIView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    def get(self,request):
        return Response({'Message':'This is get method of signup API'},status=status.HTTP_200_OK)

    def post(self,request):
        try:
            obj =  SignUpSerializer(data =  request.data)
            if obj.is_valid():
                obj.save()
                #return Response({'Message':'Successfully Signed up'},status = status.HTTP_200_OK)

            #return Response(obj.errors,status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something Failed due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)

class PersonalInfoView(generics.ListCreateAPIView):
    queryset=PersonalInfo.objects.all()
    serializer_class=PersonalInfoSerializer   

class OtpView(generics.ListCreateAPIView):
    queryset=SignUpOtp.objects.all()
    serializer_class=SignUpOtpSerializer    
