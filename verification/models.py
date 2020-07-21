from django.db import models
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.models import Device
from django_otp.oath import totp as TOTP
import time
from django_otp.util import random_hex

# Create your models here.

class TOTPModel(models.Model):

    
    phone = models.CharField(max_length = 10,  help_text="phone number")
    key = models.CharField(max_length=80, help_text="A hex-encoded secret key of up to 40 bytes.")
    step = models.PositiveSmallIntegerField(default=60, help_text="The time step in seconds.")
    t0 = models.BigIntegerField(default=0, help_text="The Unix time at which to begin counting steps.")
    digits = models.PositiveSmallIntegerField(choices=[(6, 6), (8, 8)], default=6, help_text="The number of digits to expect in a token.")
    tolerance = models.PositiveSmallIntegerField(default=1, help_text="The number of time steps in the past or future to allow.")
    drift = models.SmallIntegerField(default=0, help_text="The number of time steps the prover is known to deviate from our clock.")
    last_t = models.BigIntegerField(default=-1, help_text="The t value of the latest verified token. The next token must be at a higher time step.")
    
    def __str__(self):
        return key;

    def verify_is_allowed(self):
        pass
        

    def verify_token(self):
        
        pass
    
    def token_expired(self):
        if time.time() - self.t0 > self.step:
            return True
        else: 
            return False

    def generate_token(self):
        print(self.key)
        self.t0 = time.time()
        self.key = random_hex(20)
        totp = TOTP(key = bytearray(self.key, 'utf-8'))
        self.last_t = totp
        return self.last_t
    
    def setMobile(self, phone):

        self.phone = phone

    def __str__(self):
        return self.phone


    


