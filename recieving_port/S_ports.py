from gevent import monkey
from gevent.pool import Pool


class S_port :
    def __init__ (self,token,django_address,allow_types=['start','text','file']):
        self.token = token
        self.bot_address = django_address
        self.allow_types = allow_types

    def send_message_to_bot (self,msg):

        import requests
        import json


        if msg['type'].lower() in self.allow_types:
        
            if msg['type'] == "FILE":
                
                F = {
                    "Sid"    : msg['fileId']    ,
                    "url"    : msg['fileUrl']   ,
                    "name"   : msg['fileName']  ,
                    "size"   : msg['fileSize']  ,
                    "ftype"  : msg['fileType']  ,
                }
                
                del  msg['fileId']    ,msg['fileUrl']   ,msg['fileName']  ,msg['fileSize']  ,msg['fileType']
                msg['FILE'] = F
    
            post_data = {"masseger":"soroush+","massage":msg}

            post_data = json.dumps(post_data, separators=(',', ':'))

            r = requests.post(self.bot_address,post_data)

            if r.status_code == 403 :
                raise
        
        else:
            raise


    def run (self):
        from sys import path
        from S_client import Client as S_client

        send_headers = {'Content-Type': 'Application/json', 'Accept': 'Application/json'}
        bot = S_client(self.token)
        bot.RETRY_DELAY = 2

        monkey.patch_all(GEVENT_SUPPORT=True)
        pool = Pool(3)

        for msg in bot.get_messages():
            pool.spawn(
                self.send_message_to_bot,
                msg
                )






bots = [
    S_port("vQRiN3MmLC5blbDhwX7VWkdf-q2K9aK3zr_blt3t4liEooZqMu2PSFbZ3nfwprzpFJG1YH5hy5RgbJdKeIbxqqmqtrSF7H7LutUjvuF9Wc7TeoV6JypVu0Mgi5wkVUQVX6eVKgtSBHZ_kiVj" ,'http://127.0.0.1:8000/Damasanj/message/request/',allow_types=['text','start','file'])
]

        
        




