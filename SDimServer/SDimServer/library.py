from pymongo import MongoClient as MGClient
from platform import system as si
from sys import argv 



def FilesConnect ():
    connect =  MGClient('mongodb://localhost:27017')
    db      =  connect['SDimServer']
    return db 

def fos ():
    ba = {'Windows':'\\','Linux':r'/'}
    b = ba[si()]
    return b



def location():
    slash = fos()
    return slash.join(argv[0].split(slash)[:-1])






