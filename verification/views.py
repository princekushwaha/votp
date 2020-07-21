from django.shortcuts import render
# from rest_framework.generics import 
from rest_framework.generics import CreateAPIView
from .models import TOTPModel
from .serializers import GenerateOTPSerializer
from .serializers import VerifyOTPSerializer
from rest_framework.response import Response
from .send_sms import send_sms

# Create your views here.



class GenerateOTPView(CreateAPIView):

        serializer_class = GenerateOTPSerializer

        def create(self, request, *args, **kwargs):
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user, exp_time, msg, status = self.perform_create(serializer)
                data = {
                        'phone' : user,
                        'expire_within(in seconds)' : exp_time,
                        'message' : msg, 
                }
                headers = self.get_success_headers(serializer.data)
                return Response(data, status=status, headers=headers)


        def perform_create(self,serializer):
                return serializer.save()

class VerifyOTPView(CreateAPIView):
        serializer_class = VerifyOTPSerializer

        def create(self, request, *args, **kwargs):
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user, otp, msg, status = self.perform_create(serializer)
                data = {
                        'phone' : user,
                        'otp' : otp,
                        'message' : msg, 
                }
                headers = self.get_success_headers(serializer.data)
                return Response(data, status=status, headers=headers)


        def perform_create(self,serializer):
                return serializer.save()





       
                 


            




        