from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import TOTPModel
from rest_framework import status
import time
from .send_sms import send_sms



class GenerateOTPSerializer(Serializer):

    user = serializers.CharField(max_length = 10)
    

    def generate_token(self):
        
        available_token = TOTPModel.objects.filter(phone = self.validated_data['user'])
      
            
        expired = True
        if available_token.exists():
            available_token = TOTPModel.objects.get(phone = self.validated_data['user'])
            expired = available_token.token_expired()
            print(expired)

        if expired:
            available_token.delete()
            token = TOTPModel()
            token.setMobile(phone = self.validated_data['user'])
            token.generate_token()
            token.save()
            body = 'Your Verification OTP is: ' + str(token.last_t) + "      \nThis OTP will expire within " + str(token.step) + " seconds\n\nFrom TEAM GABRU"
            send_sms(body = body,to = self.data['user'])
            return (self.data['user'], token.step, "OTP sent successfully", status.HTTP_201_CREATED)

        else:
            return (self.data['user'], available_token.step -( time.time() - available_token.t0), "OTP Already Sent", status.HTTP_226_IM_USED)



    def save(self):
       return self.generate_token()
     
class VerifyOTPSerializer(Serializer):

    user = serializers.CharField(max_length = 10)
    token = serializers.CharField()

    def verify_otp(self):

        searched_token = TOTPModel.objects.filter(phone = self.validated_data['user'], last_t = self.validated_data['token'])
        verified = True
        if searched_token.exists():
            searched_token = TOTPModel.objects.get(phone = self.validated_data['user'], last_t = self.validated_data['token'])
            if searched_token.token_expired():
                return (self.data['user'], self.validated_data['token'], "Invalid OTP", status.HTTP_404_NOT_FOUND)
            else:
                return (self.data['user'], self.validated_data['token'], "OTP Succesfully Validated", status.HTTP_202_ACCEPTED)
        else:
            return (self.data['user'], self.validated_data['token'], "Invalid OTP", status.HTTP_404_NOT_FOUND)


    def save(self):
        return self.verify_otp()


            
        



    

