from django.views.decorators.csrf import csrf_exempt
from json import loads

try :
    from SDimServer.Damasanj.models import Feedback, MSG
    from SDimServer.Damasanj.scripts import NewUser ,ucomplete ,admin
    from SDimServer.Damasanj.library import fos
    from SDimServer.Damasanj.models import UIDs ,User ,idname ,script
except:
    from Damasanj.models import Feedback, MSG
    from Damasanj.scripts import NewUser ,ucomplete ,admin
    from Damasanj.library import fos
    from Damasanj.models import UIDs ,User ,idname ,script



slash = fos()




def mdriver (request , id ,msg ,time ,File ,ype):
    return driver ( id ,msg ,time ,File ,ype ,'url')


@csrf_exempt
def redriver (request):
    r0 = loads(request.body)
    r = r0 ['massage']
    r['ret'] = 'request'
    return driver ( r0['massenger'],**r )




















def driver( massenger ,ret = 'request'  ,id='' ,msg='' ,time=0 ,File=' ' ,ype='' ):
    scr = script.start()
    print ("\n\n\n\n(recive %s)   %s < %s >>>  %s\n" %(ret,ype,idname(id),msg))
    
    if File == ' ':
        File = None 


    if id  not in  UIDs() : 
        scr.co("start0")    
        it = NewUser(ype ,id ,msg ,time ,File)
    else:



        it = User.objects.get(Sid=id)
        it.insertmsg ( MSG.new(body=msg,time=time,Type=ype,File=File,Format='input',CFormat='ot').Save())
        res = it.dodo()
        scr.co(it.mode)
        
        case = it.mode.name


        if it.mode.name[:5] == 'start' or it.mode.name[:4] == 'sign':
            if res :
                ucomplete(it)
        elif case[:3] == 'adm':
            if res :
                admin(it)





    rere = it.Do()

    print(scr.end())

    return rere