from sys import path
from Sending.client import Client
from Damasanj.apps import DamasanjConfig as Dc 
token = Dc.Sid
bama = Client(token)

class dama :
    def send(data,rname):
        if data['type'].lower() == 'text':
        
            sendp(data['body'],rname,'TEXT')

            bama.send_message(data)


def sendp(d,r,t):
    print ("(send %s)    <%s>>>  %s" %(t,r,d.splitlines()[0]))    
    for q in d.splitlines():
        sp = ' '*len("(send %s)    <%s>>>  %s" %(t,r,d.splitlines()[0]))
        print ("%s%s" %(sp,q))
    print ('\n\n\n\n')