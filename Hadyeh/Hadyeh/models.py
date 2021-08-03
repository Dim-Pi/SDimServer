import re 
from django.core.checks import messages

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


class User:
    


    def Save(self):
        self.mode = str(self.mode)
        self.messanger = str(self.messanger)
        self.save()


    def sync(self):
        self.mode       = Mode.objects.get     (lambda s : s.name == str(self.mode))
        self.messanger  = Messanger.objects.get(lambda s : s.name == str(self.messanger))



    def change_mode (self,new_mode):
        self.mode = new_mode
        


    def send_message(self,message):
        
        trys = 0
        while trys <= 3 :
            try:
                return self.messanger.send_message(self,message)
            except:
                time.sleep(1)
                trys += 1
        raise


    def route (self,msg):
        if re.match("<move>->[.+]",msg) :
            new_mode = re.find("<move>->[(.+)]",msg)[0]
            self.change_mode (new_mode)


        



    def execute (self,*modes):
        
        if len(modes) == 0 :
            modes = (self.mode,) 

        for mode in modes:
            for msg in mode.messages :
                send_msg_thread = threading.Thread(target=self.send_message,args=(msg,))
                send_msg_thread.start()

            self.change_mode(mode)




class Keyboard :
    def __init__ (self,keys):
        self.keys = keys






class objects(list) :
    
    
    def filter (self,*keys) :
        returnal = objects(self)
        for obj in self :
            for key in keys :
                if not key(obj) :
                    returnal.remove(obj)
                    break

        return returnal

    def get (self,*keys):
        ars = self.filter(*keys)
        if len(ars) == 1:
            raise
        return ars[0]




class Mode :
    objects = objects([])

    def __init__ (self,name='',Type='static',messages=[],keyboard=None):
        self.name = name 
        self.type = Type
        self.messages = messages
        if keyboard == None :
            try :
                self.keyboard = messages[-1].keyboard
            except :
                self.keyboard = None
        else:
            self.keyboard = keyboard
        
        
        Mode.objects.append(self)



    def __str__ (self):
        return self.name



class Message :
    objects = objects([])

    def __init__ (self,*args,Type='text',body='',keyboard=None):
        self.Type = Type
        
        try : self.body = args[0]
        except: self.body = body

        self.keyboard = keyboard

        Message.objects.append(self)




class Messanger :
    objects = objects([])


    def __init__ (self,name,driver):
        self.name = name
        self.driver = driver
        Messanger.objects.append(self)
    

    def send_message(self,user,message):
        self.driver.send_message(user.sign_data,message)


    def translate (self,msg):
        return self.driver.translate(msg)

    def __str__ (self):
        return self.name



class Keyboard :
    def __init__ (self,keys):
        self.keys = keys






class objects(list) :
    
    
    def filter (self,*keys) :
        returnal = objects(self)
        for obj in self :
            for key in keys :
                if not key(obj) :
                    returnal.remove(obj)
                    break

        return returnal

    def get (self,*keys):
        ars = self.filter(*keys)
        if len(ars) == 1:
            raise
        return ars[0]




class Mode :
    objects = objects([])

    def __init__ (self,name='',Type='static',messages=[],keyboard=None):
        self.name = name 
        self.type = Type
        self.messages = messages
        if keyboard == None :
            try :
                self.keyboard = messages[-1].keyboard
            except :
                self.keyboard = None
        else:
            self.keyboard = keyboard
        
        
        Mode.objects.append(self)



    def __str__ (self):
        return self.name



class Message :
    objects = objects([])

    def __init__ (self,*args,Type='text',body='',keyboard=None):
        self.Type = Type
        
        try : self.body = args[0]
        except: self.body = body

        self.keyboard = keyboard

        Message.objects.append(self)




class Messanger :
    objects = objects([])


    def __init__ (self,name,driver):
        self.name = name
        self.driver = driver
        Messanger.objects.append(self)
    

    def send_message(self,user,message):
        self.driver.send_message(user.sign_data,message)


    def translate (self,msg):
        return self.driver.translate(msg)

    def __str__ (self):
        return self.name
