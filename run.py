from sys import path ,argv
from Port.library import fos , musub
from subprocess import call as do
from platform import system as si
from re import sub
from manage import main





def fos ():
    ba = {'Windows':'\\','Linux':r'/'}
    b = ba[si()]
    return b



def musub (tex,dic):
    
    for q0 in dic:
        q = dic[q0]
        tex = sub(q0,q,tex)
    
    return tex



















s = fos()

def syssub(dic):
    from platform import system
    di = {}
    for q0 in dic:
        q1 = dic[q0]
        try: di[q0] = q1[system()]
        except: di[q0] = q1
    
    return di


manpas = argv[0].split(s)
manpas.pop()
manpas.append('manage.py')
manpas = s.join(manpas)




ppas = argv[0].split(s)
ppas.pop()
ppas = s.join(ppas)



_procces_info ={
    r'(\\)':{'Windows':'\\\\'  ,'Linux':'/'},
    '(//)':{'Windows':'\\\\'  ,'Linux':'/' } ,
    '(su)':{'Windows':''    ,'Linux':'sudo'} ,
}

procces_info = syssub(_procces_info)



procces =[
    'su python3 "%s//port//Damasanj_driver.py"'%ppas,
    "su python3 manage.py runserver",
]



def Do (scr): 
    from subprocess import call as do    
    print ('\n\n\n\n\n\n\n\n\n',musub(scr ,procces_info),'\n\n\n\n\n\n\n\n')
    do ( musub(scr ,procces_info) )

def O (y): return(y)


Do(procces[0])


input()















