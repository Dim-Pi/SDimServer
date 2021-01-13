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
from Damasanj.library import fos
from Sending.send import dama
from os  import  mkdir 
from sys import  argv
import base64
import bson
from bson.binary import Binary
slash = fos()
location = slash.join(argv[0].split(slash)[:-1])




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
    class Meta :
        verbose_name='تصویر'
        verbose_name_plural='تصویرها'

        
    loc       =  dchar('شناسه',primary_key=True,default='example: math mosallasat 1 Q1',max_length=120) 
    image     =  dbyte()
    ftype     =  dchar('Type',max_length=7)




    def insert (self,loc):
        db          =   Fldb()
        cow         =   db['Damasanj_image']
        

        with open(loc ,'rb') as fin :
            f = Binary(fin.read())
            cow.insert ({'loc':self.loc,'image':f})
            self.image = f
            return self

    
    

    def imageloc (self):
        File = self.image
        fileloc = "%s%s%s%s" %(location ,slash ,self.loc ,self.ftype)
        with open(fileloc , 'wb+') as f :
            f.write(File)
            f.close()
            return fileloc
    
    def __str__(self):
        return self.loc








class Role(model):
    class Meta:
        verbose_name='نقش'
        verbose_name_plural=' نقش ها '


    name = dchar('نام مسئولیت',max_length=150,primary_key=True)

    def __str__(self):
        return self.name


stu = Role.objects.get(name='رئیس خودش')





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
    class Meta :
        verbose_name='فرهنگی'
        verbose_name_plural = 'فرهنگی'


    Sname           =    dchar  ('نام',max_length=220,default=None)
    Bname           =    dchar  ('نام خانوادگی',max_length=220,default=None)
    stuid           =    dchar  ('کد کلاسی',max_length= 18 ,default=None)
    role            =    dclass ('Role',on_delete=dont ,default=stu ,verbose_name='نقش')
    Sid             =    dchar  ('id سروش',max_length=225 ,default=None  ,primary_key=True)
    model           =    dchar  (max_length=  6 ,default='0')
    mode            =    dclass ('Feedback',on_delete=resume,default=None)
    lastmsg         =    dclass ('MSG',on_delete=dont,default=None)
    lkeyb           =    dlist  (dlist(ddict()),default=None)

    def __str__ (self):
        return "%s  %s"%(self.Sname,self.Bname)


    def accesskeys(self):
        if self.lkeyb == None:
            return None
        li = list()
        for q0 in list(self.lkeyb) :
            for q in q0:
                li.append (q['command'])

        return li

    def send (self,data):
        dama.send(data)

    def send_msg (self,ms):
        if ms.Type.lower() == 'text' :
            data = {'body':ms.body,'keyboard':ms.keyb,'type':ms.Type,'to':self.id}
        self.send (data)
    
    def Do (self,w):
        
        self.send_msg(w.msg)    
        self.mode = w.name
        self.lkeyb = w.msg.keyb



    
def UIDs ():
    li = list()
    for q in User.objects.all():
        li.append(q.Sid)

    return li




class MSG(model) :
    id     =  dchar ('id سروش',max_length=225 ,default=None)
    body   =  dstr  ()
    time   =  dint  (default=None)
    Type   =  dchar (max_length=20)
    File   =  dstr  ()
    keyb   =  dlist(dlist(ddict),default=None)


class door (model):
    class Meta:
        verbose_name='دور'
        verbose_name_plural='دور ها'


    door       =  dclass('Dor',on_delete=resume)
    body       =  dclass('User',on_delete=resume)
    Progress   =  dint()
    def __str__(self):
        return '%s : %s' %(self.body,self.door)








class Dor(model):

    class Meta:
        verbose_name='فراسنج'
        verbose_name_plural='فراسنج ها'


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

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'

    name     =   dchar(max_length=60,primary_key=True,default='Ques')
    image    =   dclass('Image',on_delete=resume)
    text     =   dstr()
    lesson   =   dclass("Lesson",on_delete=protect)

    def __str__(self):
        return "%s: %s" %(str(self.lesson),self.text)





















































































class Feedback (model):
    class Meta:
        verbose_name="بازخورد"
        verbose_name_plural="بازخورد ها"

    name   =  dchar('نام',max_length=25,primary_key=True)
    msg    =  dclass('MSG',on_delete=dont)
    bmods  =  dlist(dchar(max_length=25),verbose_name='بعدی ها')


