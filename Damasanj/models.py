

def apend(sef,loc,mo):
    w = mo
    e = None
    for q in range (loc,len(sef)):
        e  =  sef [q]
        sef[q]  = w
        w = e
    sef.append(w)
    return sef

try:
    from sys import maxsize, path
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
    dtime    =  models.TimeField
    ddate    =  models.DateField
    ddati    =  models.DateTimeField
    dbyte    =  models.BinaryField
    dimage   =  models.BinaryField
    dfloat   =  models.FloatField
    resume   =  models.CASCADE
    protect  =  models.PROTECT
    dont     =  models.DO_NOTHING

    
    try:
        from Damasanj.library import FilesConnect as Fldb
        from Damasanj.library import fos ,musub ,mongo ,brand ,List ,jDump
        from Sending.send import dama
        from Damasanj.init import main as init
        from Damasanj.apps import DamasanjConfig
    except:   
        from SDimServer.Damasanj.library import FilesConnect as Fldb
        from SDimServer.Damasanj.library import fos ,musub ,mongo ,brand ,List ,jDump
        from SDimServer.sending.send import dama
        from SDimServer.Damasanj.apps import DamasanjConfig
        from SDimServer.Damasanj.init import main as init


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
    print('\ninstall packages!!!\n')
    exit()










class dict(dict):
    def rename(self,c1,c2):
        try:
            self[c2] = self[c1]
            del self[c1]
            return self
        except:
            raise '\ndict on nown!\n\n'


class model2 :
    def _try(self): return self






def givefun(fun):
    global FeedFuncs
    FeedFuncs = fun



def _soroush_plus_send(name,**info):
    dama.send(name,**info)






global _sender
_sender = {
    "_soroush+_sender" : _soroush_plus_send
}
class Massenger(model):
    name   = dstr(primary_key=True)
    sender = dstr()



    def send(self,name,**info):
        try: sender = _sender [self.sender]
        except: sender = __import__ (self.sender)

        return sender(name,**info)


    def SELF (self):
        return self



    def Save(self):
        self.save()
        return self


    def _give(*k,**key): return Massenger.add(*k,**key)


    def add (nm,**info):
        try: return Massenger.objects.get(name=nm).SELF()
        except: return Massenger(name=nm,**info).Save() 
        







class SFile(model):
    class Meta :
        verbose_name='تصویر'
        verbose_name_plural='تصویرها'

    Sid       =  dstr (primary_key=True,default=None)
    url       =  dstr(default='')
    name      =  dstr (default='')
    ftype     =  dchar('Type',max_length=7,default=None)
    size      =  dint(default=1)


    def new(**info):
        info = dict(info)
        if 'fileName'in list(info):
            info.rename('fileName' ,'name')
        if 'name' in list(info) and 'ftype' not in list(info):
            info['ftype'] = info['name'].split('.')[-1] 

        return SFile(**info).Save()


    def Save(self):
        self.save()
        self.sync()
        return self

    def sycn(self): ...

    def __str__(self):
        return self.name






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


    def _try (self): 
        return self


    def _give (*name,**info):
        try: info['name'] = name[0]
        except:...
        try: return Option.objects.get(**info)._try()
        except: return Option(**info).Save()






class Role(model,model2):
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
        if self.options != 'e':
            for q in self.options:
                e.append (q.name)
        else:
            self.options = [Option._give('stu')]
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


    def _give(**info):
        try: return Role.objects.get(**info)._try()
        except: return Role(**info).Save()











class Lesson(model):

    class Meta :
        verbose_name='درس'
        verbose_name_plural='درس ها'



    dadmin        =  dclass('User',on_delete=dont,verbose_name='سرگروه',default=None)
    name          =  dchar('نام درس',max_length=20)
    Ename         =  dchar('نام لاتین',max_length=20,primary_key=True)
    small_name    =  dstr('اسم مخفف',default='mth')
    topic         =  dstr(default='')                #alaki (json.list)
    topics        =  dstr(default=None)              #for_save


    def __str__ (self):
        return self.name

    def add (nm,**info):
        try:
            try: return Lesson.objects.get(Ename=nm).Save()
            except: return Lesson(Ename=nm,**info).Save()
        except: return False


    def Save(self):
        self.topics = dumps(self.topic,separators=(',', ':'))
        self.topic = ''

        try:
            Role.objects.get (name='admin.%s' %self.Ename).name
        except:
            Role(name='admin.%s' %self.Ename,options=[Option._give('adm.%s'%self.small_name),Option._give('stu')]).Save()

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
    massenger       =    dclass (Massenger,on_delete=dont,default=None)
    developing_dor  =    dclass ('Dor',on_delete=dont,default=None)
    









    def __str__ (self):
        return "%s %s"%(self.Sname,self.Bname)




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
        self.mode.sync()
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
        try:
            if type(data['keyboard']) == str:
                del(data['keyboard'])
        except:
            pass
        self.massenger.send(str(self),**data)






    def send_msg (self,ms):
        rlis = {
            '(<sname>)'         :   self.Sname                  ,
            '(<bname>)'         :   self.Bname                  ,
            '(<fname>)'         :   self.Sname+' '+self.Bname   ,
            '(<farasanj.name>)' :   self.developing_dor.name    ,
            
        }


        if ms.Type.lower() == 'text' :
            data = {'body':ms.body,'keyboard':ms.keyb,'type':ms.Type,'to':self.Sid}

        data['body'] = musub(data['body'],rlis)
        self.send (data)





    def sode (self,w):
        if type(w)==str:
            if len(w.split('.')) == 1: m = w
            elif len(w.split('.')) == 2:
                m=w.split('.')[0]
                self.mode2 =  w.split('.')[1]
            w = Feedback.objects.get(name=m)

        else: w = w

        self.mode  = w
        self.node  = w.name
        self.nmod = self.mode.bmods
        self.do = True
        self.Save()




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
        

    def Back(self):
        self.mode ,self.lmod = self.lmod ,self.mode
        try:
            self.Save()
            return True
        except: return False



    def dodo (self):

        nm = ''
        try:
            if self.lastmsg.body[0] != '/':
                nm = 'main'
            elif self.lastmsg.body[:2] == '//' :
                if len(self.lastmsg.body[1:].split('.')) == 1: nm = self.lastmsg.body[1:].split('.')[0]
                elif len(self.lastmsg.body[1:].split('.')) == 2: 
                    nm = self.lastmsg.body[1:].split('.')[0]
                    nm0 = self.lastmsg.body[1:]
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
            try: self.sode ( Feedback.objects.get(name=ddic[nm]) )
            except: self.sode (ddic[ nm0 ])
        except:
            try:
                self.sode ( Feedback.objects.get(name=ddic['main']) )
            except: ...
                
        self.mode.sync()
        self.nmod = self.mode.get_next_modes()

        try: boofun = self.node[:2] == '//' or ddic[nm][:2] == '//' 
        except : boofun = False
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
            global lus
            lus = self
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
                    q = msgs[q0]
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
    Sid  = dstr  (primary_key=True)
    Self = dclass(User,on_delete=resume)
    

    def send(self,data):
        if data['keyboard'] == None or type(data['keyboard']) == str:
            del(data['keyboard'])
        self.Self.send(data)



    def send_msg(self,fd):

        fd.sync()

        for ms0 in fd.msg :
            try :
                ms =  fd.msg[ms0]
            except :
                ms = ms0
            ms.sync()
            if ms.Type.lower() == 'text' :
                data = {'body':ms.body,'keyboard':ms.keyb,'type':ms.Type,'to':self.Self.Sid}

            self.send (data)
    



    def Save (self):
        self.save()
        return self

    
    def _try(self): return self



    def _give(Sid):
        
        try:    u = User.objects.get(Sid=Sid)
        except: return False
        
        try:    return Admin.objects.get(Self=u,Sid=Sid)._try()
        except: return Admin(Self=u,Sid=Sid).Save()










def DoAdmin (w,keyb=False):
    for sel in Admin.objects.all() :
        if True :
            
            
                
            sel.send_msg(w)
            






def gadmin ():
    return User.objects.get (Sid=Aid)


    
def UIDs ():
    li = list()
    for q in User.objects.all():
        li.append(q.Sid)

    return li























class door (model):
    class Meta:
        verbose_name='دور'
        verbose_name_plural='دور ها'


    door       =  dclass('Dor',on_delete=resume)
    body       =  dclass('User',on_delete=resume)
    Progress   =  dint()
    def __str__(self):
        return '%s : %s' %(self.body,self.door)








class Dor(model,model2):

    class Meta:
        verbose_name='فراسنج'
        verbose_name_plural='فراسنج ها'


    lesson     =   dclass('Lesson',on_delete=protect)
    admin      =   dclass('user',on_delete=protect)
    start      =   ddati()
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

    def _give_new_only (**info):
        try: 
            if Dor.objects.get(**info)._try(): return False
        except:
            return Dor(**info).Save()





























































class MSG(model):
    body        =  dstr   ()
    Type        =  dchar  (max_length=20)
    keysave     =  dstr   (default=None)              #for_save
    Sid         =  dchar  ('id سروش',max_length=225 ,default=None)
    time        =  dint   (default=None) 
    File        =  dclass ('SFile',on_delete=resume)
    keyb        =  dstr   (default='')
    rid         =  dstr   (primary_key=True,default='0')
    Format      =  dchar  ('نوع',max_length=10,choices=[('input','ورودی'),('output','خروجی')],default='output')
    CFormat     =  dchar  ('ساخت',max_length=2,default='in',choices=[('in','ساخت سرور'),('db','از طرف دیتابیس'),('ot','سمت کاربر')])



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





    def get_next_modes(self):
        self.sync()
        if self.TYPE == "static": return self.bmods
        elif self.TYPE == "dynamic": return self.do(lus)[1]

    
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
            msgs = self.do(lus)[0]
        try: return msgs[len(msgs)-1].keyb
        except: return []
    



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




























from time import time
class script(model):
    mode = dclass('Feedback',on_delete=dont,default=None)
    stime = dfloat(default=0)
    etime = dfloat(default=0)
    time  = dfloat(default=0)

    def Save(self):
        self.save()
        return self

    def start(mod=None):
        n = script(stime=time())
        if mod != None : n.co(mod)
        return n.Save()

    def co(self,mod):
        if type(mod) == str : mod = Feedback.objects.get(name=mod)
        self.mode = mod
        return self.Save()
    
    def end(self):
        self.etime = time()
        self.time = self.etime - self.stime
        self.Save()
        return  "\n [[ did <%s> at '%s' ]] \n"%(self.mode.name,self.time)

















class Question(model):

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'

    msg       =   dchar  (max_length=1 ,default='')
    msg_save  =   dstr   (default='default' ,primary_key=True)
    lesson    =   dclass ("Lesson" ,on_delete=protect)

    def __str__(self):
        return "%s: %s" %(str(self.lesson),self.text)



    def Save (self):
        msg_save = []
        for q in self.msg :
            msg_save.append(q.rid)
        self.msg_save = jDump(msg_save)
        self.msg = ''
        self.save()
        self.sync()
        return self



    def sync(self):
        self.msg = []
        for q in loads(self.msg_save):
            self.msg.append(MSG.objects.get(rid=q))
        self.msg_save = ''
        return self


























init(
    Lesson     =  Lesson     ,
    User       =  User       ,
    Massenger  =  Massenger  ,
    Admin      =  Admin      ,
    Role       =  Role       ,
    Option     =  Option     ,
    )






