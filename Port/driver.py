from sys import path 
from client import Client
from apps import Damasanj as d
from requests import get ,post
from time import sleep
from json import dumps


HEADER = {'Content-Type': 'Application/json', 'Accept': 'Application/json'}
to = d.Sid
da = Client(to)
da.RETRY_DELAY = 2

for msg in da.get_messages():
    if msg['type'].lower() == 'text':
        urls = 'http://127.0.0.1:8000/Damasanj/message/%s/%s/%s/%s/%s/'%(msg['type'],msg['from'],msg['body'],msg['time'],' ')
        
        e = 1
        sle = 0
        tt = 0
        while e == 1 and tt <= 10  :
            #break
            try:
                post_data = dumps(msg, separators=(',', ':'))
                print ('http://127.0.0.1:8000/Damasanj/message/request/',msg)
                r = post('http://127.0.0.1:8000/Damasanj/message/request/',post_data,headers=HEADER)
                
                sle = 0
                
                if r.status_code == 403 :
                    bytes(b'','utf-8')
                print ('to good\n')
                e = 0
                tt = 0
            except:
                print ('not good\n')
                try:
                    print(urls)
                    get(urls)
                    print('to do')
                    e = 0
                    sle = 0
                    tt = 0
                except:
                    sle += 0.25
                    print ('noooooo!')
                    sleep (sle)
                    tt += 1
                    continue
                    

