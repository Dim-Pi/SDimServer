from Port.client import Client
from Damasanj.apps import DamasanjConfig as Dc 
token = Dc.Sid
bama = Client(token)

class dama :
    def send(data):
        if data['type'].lower() == 'text':
            bama.send_message(data)




