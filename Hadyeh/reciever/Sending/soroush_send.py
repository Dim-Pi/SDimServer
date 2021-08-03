from sys import path
from Sending.client import Client
from Damasanj.apps import DamasanjConfig as Dc 
token = Dc.Sid
bama = Client(token)

class dama :
    
    
    def send(rname,**data):
        if data['type'].lower() == 'text':
        
            sendp(data['body'],rname,'TEXT')

            bama.send_message(data)
    


    def upload_file(**data):
        try:
            F = data['file']
        except:
            raise "file don't found!!\n"
        
        file = bama.upload_file(F)
        if file[0]:
            return False
        else :
            return (file[1] ,'')
    



    def download_file(**info):

        try:  url = info['url']
        except:  return ["url don't found" ,False]

        try:  download_path = info['download_path']
        except:  return ["download_path don't found" ,False]


        return bama.download_file(url ,download_path)

        


def sendp(d,r,t):
    print ("(send %s)    <%s>>>  %s" %(t,r,d.splitlines()[0]))    
    for q in d.splitlines():
        sp = ' '*len("(send %s)    <%s>>>  %s" %(t,r,d.splitlines()[0]))
        print ("%s%s" %(sp,q))
    print ('\n\n\n\n')  