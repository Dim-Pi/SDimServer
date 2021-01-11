from pymongo import MongoClient as MGClient

def FilesConnect ():
    connect =  MGClient('mongodb://localhost:27017')
    db      =  connect['SDimServer']
    return db 











