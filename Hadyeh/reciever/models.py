import re
from django.core.checks import messages
from Hadyeh.models import *
base_user = User


from django.db.models.fields import SmallIntegerField
import threading
import time


try:
    from django.db import models


    model    =  models.Model
    dint     =  models.IntegerField
    dstr     =  models.TextField
    dchar    =  models.CharField
    dboo     =  models.BooleanField
    dclass   =  models.ForeignKey
    dtime    =  models.TimeField
    ddate    =  models.DateField
    ddati    =  models.DateTimeField
    dbyte    =  models.BinaryField
    dimage   =  models.BinaryField
    dfloat   =  models.FloatField
    djson    =  models.ManyToManyField
    resume   =  models.CASCADE
    protect  =  models.PROTECT
    dont     =  models.DO_NOTHING




except:
    print("\n install packages !!! \n")
    exit()


class Rec_User (model ,base_user):
    
    Full_name           =     dstr     ('نام کامل',primary_key=True)
    Fake_name           =     dstr     ('نام مستعار',primary_key=True)
    mode                =     djson    ('Mode',default=None)
    mode_argamons       =     djson    ()
    sign_data           =     djson    (primary_key=True)
    messanger           =     dstr     ('Messanger',default=None)




User = Rec_User


