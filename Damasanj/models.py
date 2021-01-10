from django.contrib.postgres.fields import HStoreField , ArrayField
from django.db import models
model = models.Model
dint = models.IntegerField
dstr = models.TextField
dchar = models.CharField
dclass = models.ForeignKey
ddict = HStoreField
dlist = ArrayField



class user(model):
    Sname = dchar(max_length=220)
    Bname = dchar(max_length=220)
    stuid = dchar(max_length= 18  ,primary_key=True)
    Sid   = dchar(max_length=200)
    model = dchar(max_length=  6  ,choices=[['dmn','dmn'],['Bdmn','Bdmn'],['stu','stu']])
    mode  = dchar(max_length= 25)
    

    def __init__ (self,Sid):
        self.Sid = Sid



class 













