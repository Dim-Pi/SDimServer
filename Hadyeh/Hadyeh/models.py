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
    resume   =  models.CASCADE
    protect  =  models.PROTECT
    dont     =  models.DO_NOTHING




except:
    print("\n install packages !!! \n")
    quit()


class User (model):
    
    M_name              =     dstr     ('نام مستعار',primary_key=True)
    mode                =     dclass   ('mode')



class mode (model):

    name   =   dstr  (primary_key=True)
    url    =   dstr  (primary_key=True)
    

