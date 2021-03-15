from django.db import models
from multiprocessing import Process
try:
    
    def fos ():
        from platform import system as si
        ba = {'Windows':'\\','Linux':r'/'}
        b = ba[si()]
        return b

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
    slash    =  fos()
except: exit()






from time import sleep

class node (model):
    id     =  dint(primary_key=True)
    tocken =  dstr()

    def __init__ (id,tocken):
        self.id = id
        self.tocken = tocken

    def new(id,tocken) :

        
        with open('Sending%snode%s.py'%(slash,id),'w+') as F:
        
            data = '''
from sys import path
from client import Client

tocken = "%s"

bot = Client(tocken)
bot.RETRY_DELAY = 1

import socket

s = socket.socket()
port = 804%s
ip = socket.gethostbyname(socket.gethostname())
s.bind((ip, port))
s.listen()

from json impor loads

while True:
    c ,addr = s.accept()
    co = c.recv(1024).decode()
    global code
    try: code = loads(co)
    except:
        if co == 'ok':
            c.send('ok'.encode())
        c.close()
        del c,code

    c.close()
    del c

    B = lambda x : code["TYPE"] == x
 
    if B('TEXT'):
        try: 
            bot.send_message(code)
            del code
            return True

        except: 
            del code
            return False

        ''' %(tocken,id)




        
        
        
        
            F.write(data)
            F.close()
            sleep(0.1)
            Node =  node()
    











