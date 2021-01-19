from sys import path
from django.contrib.postgres.fields import HStoreField , ArrayField 
from django.db import models
from django.http import HttpResponse as Re 
from json import dumps ,loads
from hashlib import sha256
model    =  models.Model
dint     =  models.IntegerField
dstr     =  models.TextField
dchar    =  models.CharField
dboo     =  models.BooleanField
dclass   =  models.ForeignKey
ddict    =  HStoreField
dlist    =  ArrayField
dtime    =  models.TimeField
ddate    =  models.DateField
ddati    =  models.DateTimeField
dbyte    =  models.BinaryField
dimage   =  models.BinaryField
resume   =  models.CASCADE
protect  =  models.PROTECT
dont     =  models.DO_NOTHING
from Damasanj.library import FilesConnect as Fldb
from Damasanj.library import fos ,musub ,mongo ,brand
from Port.send import dama
from Damasanj.apps import DamasanjConfig
from os  import  mkdir 
from sys import  argv
import base64
import bson
from bson.binary import Binary
slash = fos()
location = slash.join(argv[0].split(slash)[:-1])
Aid = DamasanjConfig.Aid



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
    image     =  dbyte(default=None)
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








class Lesson(model):

    class Meta :
        verbose_name='درس'
        verbose_name_plural='درس ها'
        


    dadmin   =  dclass('User',on_delete=dont,verbose_name='سرگروه',default=None)
    name     =  dchar('نام درس',max_length=20)
    Ename    =  dchar('نام لاتین',max_length=20,primary_key=True)
    topic    =  dstr(default='')                #alaki
    topics   =  dstr(default=None)              #for_save


    def __str__ (self):
        return self.name


    def Save(self):
        self.topics = dumps(self.topic,separators=(',', ':'))
        self.topic = ''
        self.save()
        self.sync()

    def sync(self):
        self.topic = loads(self.topics)







class sekey(model):

    xkey = dbyte()

    def create (self):
        e = randint(100,10000000000)
        self.xkey = bytes(str(e),'utf-8')
         
        return bytes(sha256(self.xkey).hexdigest(),'utf-8')

    def sign (self,pas):
        if type(pas) == str :
            pas = bytes(pas,'utf-8')
        return bytes(sha256(self.xkey).hexdigest(),'utf-8') == pas 











class User(model):

    class Meta :
        verbose_name='فرهنگی'
        verbose_name_plural = 'فرهنگی'


    
    Sname           =    dchar  ('نام',max_length=220,default='نام')
    Bname           =    dchar  ('نام خانوادگی',max_length=220,default='نام')
    stuid           =    dchar  ('کد کلاسی',max_length= 18 ,default='None')
    role            =    dclass ('Role',on_delete=dont ,default=None ,verbose_name='نقش')
    Sid             =    dstr   ('id سروش' ,primary_key=True,default='')
    node            =    dchar  (max_length=  20 ,default='0')
    mode            =    dclass ('Feedback',on_delete=resume,default=None)
    lastmsg         =    dclass ('MSG',on_delete=dont,default=None)
    lkeyb           =    dstr   (default='')                #alaki
    lkeybs          =    dstr   (default=None)              #for_save
    do              =    dboo   (default=True)
    signkey         =    dclass ('sekey',on_delete=dont,default=None)
    sign            =    dboo   (default=False)
    spas            =    dbyte  (default=None)









    def __str__ (self):
        return "%s  %s"%(self.Sname,self.Bname)




    def Save(self):
        self.lkeybs = dumps(self.lkeyb,separators=(',', ':'))
        self.lkeyb = ''
        self.save()
        self.sync()
        return self
    



    def sync(self):
        self.lkeyb = loads(self.lkeybs)
    




    def accesskeys(self):
        if self.lkeyb == None:
            return None
        li = list()
        for q0 in list(self.lkeyb) :
            for q in q0:
                li.append (q['command'])

        return li





    def send (self,data):
        if type(data['keyboard']) == str:
            del(data['keyboard'])
        dama.send(data)






    def send_msg (self,ms):
        rlis = {
            '(<sname>)':self.Sname,
            '(<bname>)':self.Bname,
            '(<fname>)': "%s %s" %(self.Sname,self.Bname),
            
        }


        if ms.Type.lower() == 'text' :
            data = {'body':ms.body,'keyboard':ms.keyb,'type':ms.Type,'to':self.Sid}

        data['body'] = musub(data['body'],rlis)
        self.send (data)





    def sode (self,w):

        self.mode  = w
        self.node  = w.name
        self.do = True




    def jan(self,lmd):
        pass




    def again(self,lmd):
        pass



    def startkey (self):
        self.signkey = sekey()
        self.spas = self.signkey.create()
        return  self.spas


    def signin   (self,key=None):
        if key == None:
            key = self.lastmsg.body

         
            
        return self.signkey.sign(key)
        



    def dodo (self):

        nm = ''
        try:
            if self.lastmsg.body[0] != '/':
                nm = 'main'
            elif self.lastmsg.body[:2] == '//' :
                nm = self.lastmsg.body[1:]
        except:
            nm = 'main'
        lmd = self.mode

        self.sync()
        self.mode.sync()

        try :
            self.sode ( Feedback.objects.get(name=self.mode.bmods[nm]) )
        except :
            self.sode ( Feedback.objects.get(name=self.mode.bmods['main']) )



        if self.node[:2] == '//' :
        
            self.Fdo (lmd)
            self.sode(lmd)
        
        self.Save()



    def Fdo(self,lmd,F=None):
        if F == None:
            F = self.node


        
        fl = {
            '//jan':self.jan ,
            '//again':self.again
        }

        try:
            fl[F] (lmd)
        except:
            pass


    def Dowithoutsave (self,w,keyb=False):
        
        if True :
            
            for q0 in w.msg :
                q = w.msg[q0]
                self.send_msg(q)
                if keyb :
                    self.lkeyb = w.msg.keyb
        


    def Do (self,w=None):
        if self.do :
            if w == None :
                w = self.mode

            w.sync()
            for q0 in w.msg :
                try:
                    q = w.msg[q0]
                except:
                    q = q0
                q.sync()
                self.send_msg(q)
                self.lkeyb = q.keyb        
        
            self.mode  = w
            self.node  = w.name
            self.do    = False
            self.Save()
            return Re('202')








class Admin(model):
    Sid = dstr(primary_key=True)

    def send(self,data):
        dama.send(data)

    def send_msg(self,fd):

        for ms0 in fd.msg :
            try :
                ms =  fd.msg[ms0]
            except :
                ms = ms0
            if ms.Type.lower() == 'text' :
                data = {'body':ms.body,'keyboard':ms.keyb,'type':ms.Type,'to':self.Sid}

            self.send (data)
    
    def Save (self):
        self.save()
        return self

    













def DoAdmin (w,keyb=False):
    for sel in Admin.objects.all() :
        if True :
            
            
                
            sel.send_msg(w)
            



for q in DamasanjConfig.Adid :
    Admin (Sid=q).Save()




def gadmin ():
    return User.objects.get (Sid=Aid)

    
def UIDs ():
    li = list()
    for q in User.objects.all():
        li.append(q.Sid)

    return li



















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
    topicsave  =   dstr (default=None)              #for_save
    topic      =   dstr (default='')                #alaki
    qtion      =   dstr (default='')                #alaki
    qtionid    =   dstr (default=None)              #for_save
    toool      =   dint()
    name       =   dchar(max_length=50,primary_key=True,default='name')

    def __str__ (self):
        return "%s: ( %s )" %(str(self.lesson)   , ','.join(self.topic)  )

    def Save(self):
        lis = list()
        for q0 in self.qtion:
            q = self.qtion[q0]
            lis.append(str(q.name))
        self.qtionid  = dumps(lis,separators=(',', ':'))
        self.topicsave = dumps(self.topic,separators=(',', ':'))
        self.topic = ''
        self.qtion = ''
        self.save()
        self.sync()

    def sync(self):
        li = loads(self.qtionid)
        lis = list()
        for q in li :
            lis.append(Question.objects.get(name=q))
        
        self.qtion = lis
        self.topic = loads(self.topicsave)















































































class MSG(model):
    body        =  dstr  ()
    Type        =  dchar (max_length=20)
    keysave     =  dstr (default=None)              #for_save
    Sid         =  dchar ('id سروش',max_length=225 ,default=None)
    time        =  dint  (default=None) 
    File        =  dstr  (default=None)
    keyb        =  dstr  (default='')
    rid         =  dstr  (primary_key=True,default='0')
    Format      =  dchar ('نوع',max_length=10,choices=[('input','ورودی'),('output','خروجی')],default='output')



    def __str__ (self):
        return self.body

    def new (body='',Type='TEXT',keyb=None,Sid=None,time=None,File=None,Format='output'):
        i = MSG()
        i.body = body
        i.Type = Type
        i.keyb = keyb
        i.Sid  = Sid
        i.time = time
        i.File = File
        i.Format = Format
        i.keysave = dumps(i.keyb,separators=(',', ':'))
        try:
            MSG.objects.get(rid = i.CreateID()).time
            return MSG.objects.get(rid = i.CreateID())
        except:
            return i.Save()



    def CreateID(self):
        if self.Format == 'output':
            st = '051  ' + str(self.body) + '  ' + str(self.keysave) + '  ' + str(self.File)  + '  86'  
        else:
            st = brand()
        return sha256(bytes(st,'utf-8')).hexdigest()



    def Save(self):
        self.keysave = dumps(self.keyb,separators=(',', ':'))
        self.keyb = ''
        if self.rid == '0':
            ri = self.CreateID()
            self.rid = ri
        
        self.save()
        self.sync()
        return self


    def sync(self):
        self.keyb = loads(self.keysave)











class Feedback (model):
    class Meta:
        verbose_name="بازخورد"
        verbose_name_plural="بازخورد ها"

    TYPE   =  dchar('نوع',max_length=15,choices=[('عادی','nodef'),('غیر عادی','ondef')],default='nodef')
    name   =  dchar('نام',max_length=25,primary_key=True)
    msgid  =  dstr (default=None)              #for_save
    bmodsa =  dstr (default=None)              #for_save
    msg    =  dstr ()
    bmods  =  dstr ()
    
    def Save(self):
        self.bmodsa = dumps(self.bmods,separators=(',', ':'))
        lis = list()
        for q0 in self.msg:
            q = self.msg[q0]
            lis.append(str(q.rid))
        self.msgid  = dumps(lis,separators=(',', ':'))
        self.msg = ''
        self.bmods = ''
        self.save()
        self.sync()
        return self
    
    
    def sync(self):
        self.bmods = loads(self.bmodsa)
        li = loads(self.msgid)
        lis = list()
        for q in li :
            lis.append(MSG.objects.get(rid=q))
        self.msg = lis






