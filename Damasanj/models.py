try:
    from sys import maxsize, path
    from django.contrib.postgres.fields import HStoreField , ArrayField
    from django.core import exceptions 
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

    try:
        from SDimServer.Damasanj.library import FilesConnect as Fldb
        from SDimServer.Damasanj.library import fos ,musub ,mongo ,brand ,List ,jDump
        from SDimServer.Port.send import dama
        from SDimServer.Damasanj.apps import DamasanjConfig
    except:
        from Damasanj.library import FilesConnect as Fldb
        from Damasanj.library import fos ,musub ,mongo ,brand ,List ,jDump
        from Port.send import dama
        from Damasanj.apps import DamasanjConfig

    from random import randint
    from os  import  mkdir 
    from sys import  argv
    import base64
    import bson
    from bson.binary import Binary
    slash = fos()
    location = slash.join(argv[0].split(slash)[:-1])
    Aid = DamasanjConfig.Aid
except:
    exit()




def givefun(fun):
    global FeedFuncs
    FeedFuncs = fun










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
       

        with open(loc ,'rb') as fin :
            f = Binary(fin.read())
            self.image = f
            self.save()
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






class Option(model):
    name    = dchar ('نام اصلی',max_length=8,primary_key=True,default='stu')
    Fname   = dstr  ('نام فرعی',default=' بررسی و شرکت در فراسنج ها')

    def __str__ (self):
        return self.name

    def Save(self):
        self.save()
        return self
    
    def sync(self):
        return self





class Role(model):
    class Meta:
        verbose_name='نقش'
        verbose_name_plural=' نقش ها '


    name            =  dchar('نام مسئولیت',max_length=150,primary_key=True)
    Fname           =  dchar('نام فارسی',max_length=150,default=None)
    options         =  dchar('دسترسی',max_length=1,default='e')
    optionsave      =  dstr (default='e')



    def __str__(self):
        return str(self.Fname)


    def Save(self):
        e = []
        for q in self.options:
            e.append (q.name)
        self.optionsave = jDump(e)
        self.options = ' '
        self.save()
        self.sync()       
        return self


    def sync(self):
        self.options = []
        for q in loads(self.optionsave):
            self.options.append(Option.objects.get(name=q))
        self.optionsn = []
        for q in self.options :
            self.optionsn.append(q.name)
         
        return self








class Lesson(model):

    class Meta :
        verbose_name='درس'
        verbose_name_plural='درس ها'



    dadmin   =  dclass('User',on_delete=dont,verbose_name='سرگروه',default=None)
    name     =  dchar('نام درس',max_length=20)
    Ename    =  dchar('نام لاتین',max_length=20,primary_key=True)
    topic    =  dstr(default='')                #alaki (json.list)
    topics   =  dstr(default=None)              #for_save


    def __str__ (self):
        return self.name


    def Save(self):
        self.topics = dumps(self.topic,separators=(',', ':'))
        self.topic = ''

        try:
            Role.objects.get (name='admin.%s' %self.Ename).name
        except:
            Role(name='admin.%s' %self.Ename).Save()

        self.save()
        self.sync()

        return self


    def sync(self):
        self.topic = loads(self.topics)









class sekey(model):

    ykey = dbyte()

    def create (self):
        e = brand()
        x = bytes(str(e),'utf-8')
        self.ykey = bytes(sha256(x).hexdigest(),'utf-8')
        self.Save()
        return x

    def sign (self,x):
        if type(x) == str :
            x = bytes(x,'utf-8')
        return bytes(sha256(x).hexdigest(),'utf-8') == self.ykey

    def Save (self):
        self.save()
        return self











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
    mode            =    dclass ('Feedback',on_delete=dont,default=None)
    mode2           =    dchar  (max_length=10,default='0')
    lmods           =    dstr   ('ماد قبلی',default='')    #for_save
    lmod            =    dchar  (max_length=1,default='')   #alaki
    nmod            =    dchar  (max_length=1,default='0')  #alahi
    nmods           =    dstr   (default='')                #for_save
    lastmsg         =    dclass ('MSG',on_delete=dont,default=None)
    lkeyb           =    dstr   (default='')                #alaki
    lkeybs          =    dstr   (default=None)              #for_save
    do              =    dboo   (default=True)
    signkey         =    dclass ('sekey',on_delete=dont,default=None)
    sign            =    dboo   (default=False)
    sign2           =    dboo   (default=False)
    









    def __str__ (self):
        return "%s  %s"%(self.Sname,self.Bname)




    def Save(self):
        self.lkeybs = dumps(self.lkeyb,separators=(',', ':'))
        self.lkeyb = ''
        self.nmods = jDump(self.nmod)
        self.nmod  = '0'
        try:
            self.lmods = self.lmod.name
        except:
            self.lmods = ''
        self.lmod = ''
        self.save()
        self.sync()
        return self
    



    def sync(self):
        try:
            self.lmod = Feedback.objects.filter(name=self.lmods)
        except :
            self.lmod = ''
        self.nmod = loads(self.nmods)
        self.lkeyb = self.mode.keyb()
    




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
        dama.send(data,str(self))






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
        self.nmod = self.mode.bmods
        self.do = True




    def jan(self,lmd):
        janlist = List([
           'زرشک','چی شده؟','چی میگی؟','بیا برو حال ندارم','بادمجون','گلابی','.....','شمبلیله','dfhali!!!','فعلا حوصله خدمات دهی به شما را نداریم \n با تشکر'
       ])

         
        mg = MSG.new(body=janlist.randl(),keyb=self.lkeyb,Type='TEXT').Save()
        self.send_msg (mg)






    def again(self,lmd):
        pass



    def startkey (self):
        self.signkey = sekey()
        x = self.signkey.create()
        self.Save()
        return  x.decode('utf-8')



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
                nm = self.lastmsg.body[1:].split('.')[0]
        except:
            nm = 'main'
        lmd = self.mode
        self.lmod = lmd

        self.sync()
        self.mode.sync()

        if type(self.nmod) == dict:
            ddic = self.nmod
        else:
            ddic = self.mode.nmd(self)

        

        try :
            self.sode ( Feedback.objects.get(name=ddic[nm]) )
        except :
            try:
                self.sode ( Feedback.objects.get(name=ddic['main']) )
            except:
                pass
        self.nmod = self.mode.bmods

        boofun = self.node[:2] == '//' or ddic[nm][:2] == '//' 

        nfu = '//jan'

        if boofun :
            
            if self.node[:2] == '//':
                nfu = self.node
            elif ddic[nm][:2] == '//':
                nfu = ddic[nm]
        
            self.Fdo (lmd,F=nfu)
            self.sode(lmd)
            self.Save()
            return False
        
        self.Save()
        return True



    def Fdo(self,lmd,F=None):
        if F == None:
            F = self.node


        
        fl = {
            '//jan':self.jan ,
            '//again':self.again,
            '//dont':lambda x : None
        }

        try:
            self.do = False
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


    def insertmsg (self,msg):
        try:
            self.dellast()
            self.lastmsg = msg
            return True
        except :
            return False



    def dellast(self):
        try:
            self.lastmsg.delete()
        except:
            pass



    def Do (self,w=None):


        if self.do :
            if w == None :
                w = self.mode

            w.sync()

            if w.TYPE == 'dynamic':
                ms0 ,md0 = w.do (self)
                self.nmod = md0
                msgs = ms0
            else:
                msgs = w.msg
                
            
            for q0 in msgs :
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








def idname (Sid):
    try:
        return str(User.objects.get(Sid=Sid))
    except:
        return 'NEW'








class Admin(model):
    Sid = dstr(primary_key=True)

    def send(self,data):
        if data['keyboard'] == None or type(data['keyboard']) == str:
            del(data['keyboard'])
        dama.send(data,'admin')

    def send_msg(self,fd):

        fd.sync()

        for ms0 in fd.msg :
            try :
                ms =  fd.msg[ms0]
            except :
                ms = ms0
            ms.sync()
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
    CFormat     =  dchar ('ساخت',max_length=2,default='in',choices=[('in','ساخت سرور'),('db','از طرف دیتابیس'),('ot','سمت کاربر')])



    def __str__ (self):
        return self.body

    def new (body='',Type='TEXT',keyb=None,Sid=None,time=None,File=None,Format='output',CFormat='in'):
        i = MSG()
        i.body = body
        i.Type = Type
        i.keyb = keyb
        i.Sid  = Sid
        i.time = time
        i.File = File
        i.Format = Format
        i.keysave = dumps(i.keyb,separators=(',', ':'))
        i.CFormat = CFormat
        try:
            MSG.objects.get(rid = i.CreateID()).delete()
        except:
            pass

        return i.Save()


    def CreateID(self):
        if self.Format == 'output':
            st = '051  ' + str(self.body) + '  ' + str(self.keysave) + '  ' + str(self.File)  + '  86'  
        else:
            st = str(brand())
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

    TYPE        =  dchar('نوع',max_length=15,choices=[('دینامیک','dynamic'),('استاتیک','static')],default='static')
    name        =  dchar('نام',max_length=25,primary_key=True)
    msgid       =  dstr (default=None)              #for_save
    bmodsa      =  dstr (default=None)              #for_save
    F           =  dchar(max_length=100,default=None)
    msg         =  dstr ()
    bmods       =  dstr ()
    CFormat     =  dchar ('ساخت',max_length=2,default='in',choices=[('in','ساخت سرور'),('db','از طرف دیتابیس')])



    def Save(self):
        self.bmodsa = dumps(self.bmods,separators=(',', ':'))
        lis = list()
        for q0 in self.msg:
            try :
                q = self.msg[q0]
            except:
                q = q0
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


    
    def newD(name='' ,TYPE='dynamic' ,F=False):
        
        try:
            rere = Feedback.objects.get(name=name)    
        except:
            rere = Feedback(name = name , TYPE=TYPE)
        
        if F:
            rere.F = F
        
        return rere



    def Fync(self ,F):
        self.F = F
        self.Save()


    def keyb(self):
        
        self.sync()
        if self.TYPE == 'static':
            msgs = self.msg
        else:
            msgs = self.do[0]

        return msgs[len(msgs)-1].keyb
    
    
    def do(self,us):
        if self.TYPE == 'dynamic':
            return FeedFuncs[self.F](us)



    def idget(nam):
        try :
            return Feedback.objects.get(name=nam)
        except exceptions as e:
            return e


    def nmd(self,use):
        if self.TYPE == 'dynamic':
            return self.do(use) [1]
        elif self.TYPE == 'static':
            return self.bmods