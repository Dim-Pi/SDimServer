from sys import path                 #driving for damasanj!! 
from client import Client
from apps import Damasanj as d
from requests import get ,post
from time import sleep
from json import dumps

time_out = 0.01
HEADER = {'Content-Type': 'Application/json', 'Accept': 'Application/json'}
to = d.Sid
da = Client(to)
da.RETRY_DELAY = 2


_allow_types = [
    'start',
    'text',
    'file'
]
















for msg in da.get_messages():
    if msg['type'].lower() in _allow_types:


        if msg['type'] == 'FILE':
            F = {
                "Sid"    : msg['fileId']    ,
                "url"    : msg['fileUrl']   ,
                "name"   : msg['fileName']  ,
                "size"   : msg['fileSize']  ,
                "ftype"  : msg['fileType']  ,
            }

            del  msg['fileId']    ,msg['fileUrl']   ,msg['fileName']  ,msg['fileSize']  ,msg['fileType']
        
            msg['FILE'] = F








        urls = 'http://127.0.0.1:8000/Damasanj/message/%s/%s/%s/%s/%s/'%(msg['type'],msg['from'],msg['body'],msg['time'],' ')
        
        e = 1
        sle = 0
        tt = 0




        fmsg = {'massenger':'soroush+',"massage":msg}
        post_data = dumps(fmsg, separators=(',', ':'))    



        while e == 1 and tt <= 10  :
            #break
            try :
                print ('http://127.0.0.1:8000/Damasanj/message/request/',msg)
                r = post('http://127.0.0.1:8000/Damasanj/message/request/',post_data,headers=HEADER)
                
                sle = 0
                
                if r.status_code == 403 :
                    raise 
                
                e = 0
                tt = 0
            except Exception as er: 
                if str(er.args[0]) == "HTTPConnectionPool(host='127.0.0.1', port=8000): Read timed out. (read timeout=%s)"%(time_out): 
                    e ,tt = 0 ,0 
                    print ('to good\n')
                else: 
                    tt += 1
                    sleep(0.1)
                continue
                



