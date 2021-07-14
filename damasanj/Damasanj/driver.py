
from django.views.decorators.csrf import csrf_exempt
from json import loads

try:
    from Damasanj.models import Feedback, MSG
    from Damasanj.scripts import NewUser ,ucomplete ,admin
    from Damasanj.library import fos
    from Damasanj.models import UIDs ,User ,idname ,script ,Massenger ,SFile

except :
    from SDimServer.Damasanj.models import Feedback, MSG
    from SDimServer.Damasanj.scripts import NewUser ,ucomplete ,admin
    from SDimServer.Damasanj.library import fos
    from SDimServer.Damasanj.models import UIDs ,User ,idname ,script ,Massenger ,SFile

class dict (dict):
    def rename(self,f,n):
        self[n] = self[f]
        del(self[f])

slash = fos()




def mdriver (request , id ,msg ,time ,File ,ype):
    return driver ( id ,msg ,time ,File ,ype ,'url')


@csrf_exempt
def redriver (request):
    
    r0 = loads(request.body)
    r = dict(r0 ['massage'])
    r['ret'] = 'request'
    r.rename('from','id')
    r.rename('type','ype')

    if r['type'] == 'FILE':
        r['FILE'] = SFile._give(r0['massenger'],**r['FILE'])

    return driver ( r0['massenger'],**r )
    



















def driver( massenger ,ret = 'request'  ,id='' ,body='' ,time=0 ,File=' ' ,ype='' ):
    msg = body
    scr = script.start()
    mas = Massenger._give(massenger)
    print ("\n\n\n\n(recive %s)   %s < %s >>>  %s\n" %(massenger,ype,idname(id),msg))
    
    if File == ' ':
        File = None 
    


    if id  not in  UIDs() : 
        scr.co("start0")    
        it = NewUser(ype ,id ,mas ,msg ,time ,File)
    else:



        it = User.objects.get(Sid=id)
        it.insertmsg ( MSG.new(body=msg,time=time,Type=ype,File=File,Format='input',CFormat='ot').Save())
        is_need_to_script = it.dodo()
        scr.co(it.mode)
        
        case = it.mode.name

        if is_need_to_script :
            match it.zone():
                case 'start' | 'sign':
                    ucomplete(it)
                case 'adm':
                    admin(it)





    rere = it.Do()

    print(scr.end())

    return rere
