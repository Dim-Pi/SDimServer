from pymongo import MongoClient as MGClient
from platform import system as si
from random import randint
from sys import argv 
from re import sub


def FilesConnect ():
    connect =  MGClient('mongodb://localhost:27017')
    db      =  connect['SDimServer']
    return db 



def mongo ():
    connect =  MGClient('mongodb://localhost:27017')
    db      =  connect['SDimServer']
    return db 





def fos ():
    from platform import system as si
    ba = {'Windows':'\\','Linux':r'/'}
    b = ba[si()]
    return b


def brand():
    return int(randint(1,100000000000000000000000000000000000000000)*randint(1,100000000000000000000000000000000000000000)*randint(1,100000000000000000000000000000000000000000))


def location():
    slash = fos()
    return slash.join(argv[0].split(slash)[:-1])


def musub (tex,dic):
    
    for q0 in dic:
        q = dic[q0]
        tex = sub(q0,q,tex)
    
    return tex



def jDump (js):
    from json import dumps
    return dumps(js,separators=(',', ':'))




class List (list):
    def randl (self):
        from random import randint
        return self[randint(0,len(self)-1)]