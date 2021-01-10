from sys import path
from django.contrib.postgres.fields import HStoreField , ArrayField
from django.db import models
model    =  models.Model
dint     =  models.IntegerField
dstr     =  models.TextField
dchar    =  models.CharField
dclass   =  models.ForeignKey
ddict    =  HStoreField
dlist    =  ArrayField
protect  =  models.PROTECT
dtime    =  models.TimeField
resume   =  models.CASCADE
dimage   =  models.BinaryField
from library import FilesConnect as Fldb
from os  import  mkdir 
from sys import  argv
import base64
import bson
from bson.binary import Binary
location = argv[0]





def apend(sef,loc,mo):
    w = mo
    e = None
    for q in range (loc,len(sef)):
        e  =  sef [q]
        sef[q]  = w
        w = e
    sef.append(w)
    return sef


class image(model):

    name = dstr(primary_key=True)
    def __init__ (self,loc):
        self.loc = loc 


    
    

    def imageloc (self):
        db = Fldb()
        cow = db['damaimage']
        File = cow.find_one({'loc':self.loc})
        fileloc = '%s\\%s.jpg'%(location,self.loc)
        with open(fileloc , 'wb+') as f :
            f.write(File)
            f.close()
            return fileloc


def insert (loc,name):
    db = Fldb()
    cow = db['damaimage']
    with open(loc ,'rb') as fin :
        f = Binary(fin.read())
        cow.insert ({'loc':name,'image':f}) 
        return image(name)


class Lesson(model):
    dadmin   =  dclass('user',on_delete=protect)
    name     =  dchar(max_length=20,primary_key=True)
    topics   =  dlist(dstr())

    def __str__ (self):
        return self.name
    


class User(model):
    Sname = dchar(max_length=220)
    Bname = dchar(max_length=220)
    stuid = dchar(max_length= 18  ,primary_key=True)
    Sid   = dchar(max_length=200)
    model = dchar(max_length=  6  ,choices=[['dmn','dmn'],['Bdmn','Bdmn'],['stu','stu']])
    mode  = dchar(max_length= 25)
    

    def __init__ (self,Sid):
        self.Sid = Sid



class Dor(model):

    lesson     =   dclass('Lesson',on_delete=protect)
    admin      =   dclass('user',on_delete=protect)
    strart     =   dtime()
    finish     =   dtime()
    topic      =   dlist(dstr())
    qtion      =   ddict()
    toool      =   dint()
    name       =   dchar(max_length=50,primary_key=True)

    def __str__ (self):
        return "%s: ( %s )" %(str(self.lesson)   , ','.join(self.topic)  )





class Question(model):
    name     =   dchar(max_length=60,primary_key=True)
    image    =   dimage(blank=True)
    text     =   dstr()
    lesson   =   dclass("Lesson",on_delete=protect)

    def __str__(self):
        return "%s: %s" %(str(self.lesson),self.text)

