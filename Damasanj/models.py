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
ddate    =  models.DateField
ddati    =  models.DateTimeField
resume   =  models.CASCADE
dimage   =  models.BinaryField
dont     =  models.DO_NOTHING
dbyte    =  models.BinaryField
from Damasanj.library import FilesConnect as Fldb
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


class Image(model):

    loc    = dstr(primary_key=True,default='m0') 
    image  = dbyte()


    def insert (self,loc):
        db = Fldb()
        cow = db['Damasanj_image']
        with open(loc ,'rb') as fin :
            f = Binary(fin.read())
            cow.insert ({'loc':self.loc,'image':f})
            self.image = f
            return self

    
    

    def imageloc (self):
        db = Fldb()
        cow = db['Damasanj_image']
        File = cow.find_one({'loc':self.loc})
        fileloc = '%s\\%s.jpg'%(location,self.loc)
        with open(fileloc , 'wb+') as f :
            f.write(File)
            f.close()
            return fileloc




class Lesson(model):

    class Meta :
        verbose_name='درس'
        verbose_name_plural='درس ها'
        


    dadmin   =  dclass('user',on_delete=dont,verbose_name='سرگروه')
    name     =  dchar('نام درس',max_length=20,primary_key=True)
    topics   =  dlist(dchar(max_length=100),verbose_name='موضوعات')


    def __str__ (self):
        return self.name





class User(model):
    Sname           =    dchar ('نام',max_length=220)
    Bname           =    dchar ('نام خانوادگی',max_length=220)
    stuid           =    dchar ('کد کلاسی',max_length= 18  ,primary_key=True)
    role            =    dclass('Role',on_delete=dont,default=None,verbose_name='نقش')
    Sid             =    dchar ('id سروش',max_length=225 ,default=None)
    model           =    dchar (max_length=  6 ,default='0')
    mode            =    dchar (max_length= 25 ,default='0')

    def __str__ (self):
        return "%s  %s"%(self.Sname,self.Bname)






class door (model):
    class Meta:
        verbose_name='نقش'
        verbose_name_plural='نقش ها'


    door       =  dclass('Dor',on_delete=resume)
    body       =  dclass('User',on_delete=resume)
    Progress   =  dint()
    def __str__(self):
        return '%s : %s' %(self.body,self.door)












class Role(model):
    name = dchar('نام مسئولیت',max_length=150,primary_key=True)

    def __str__(self):
        return self.name







class Dor(model):

    lesson     =   dclass('Lesson',on_delete=protect)
    admin      =   dclass('user',on_delete=protect)
    strart     =   ddati()
    finish     =   ddati()
    topic      =   dlist(dstr())
    qtion      =   ddict()
    toool      =   dint()
    name       =   dchar(max_length=50,primary_key=True,default='name')

    def __str__ (self):
        return "%s: ( %s )" %(str(self.lesson)   , ','.join(self.topic)  )





class Question(model):
    name     =   dchar(max_length=60,primary_key=True,default='Ques')
    image    =   dclass('Image',on_delete=resume)
    text     =   dstr()
    lesson   =   dclass("Lesson",on_delete=protect)

    def __str__(self):
        return "%s: %s" %(str(self.lesson),self.text)

