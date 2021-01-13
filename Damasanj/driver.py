from Damasanj.library import fos
from Damasanj.models import UIDs 
from Damasanj.user import NewUser
slash = fos()

def driver(Type='text' ,id='0aa1' ,msg='' ,time=0 ,File=slash):
    if id  not in  UIDs() :     
        NewUser(Type ,id ,msg ,time ,File)
    else:
        pass







