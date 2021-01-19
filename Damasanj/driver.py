import requests
from Damasanj.models import Feedback, MSG
from Damasanj.user import NewUser ,ucomplete
from Damasanj.library import fos
from Damasanj.models import UIDs ,User
from django.views.decorators.csrf import csrf_exempt
from json import loads
slash = fos()


def mdriver (request , id ,msg ,time ,File ,ype):
    return driver ( id ,msg ,time ,File ,ype)


@csrf_exempt
def redriver (request):
    r = loads(request.body)
    return driver ( r.get('from') ,r.get('body') ,r.get('time') ,r.get('File',' ') ,r.get('type'))




















def driver(   id ,msg ,time ,File ,ype):
    print (ype,id,msg,time,File,'\n\n\n\n')
    if File == ' ':
        File = None 


    if id  not in  UIDs() :     
        it = NewUser(ype ,id ,msg ,time ,File)
    else:



        it = User.objects.get(Sid=id)
        it.lastmsg = MSG.new(body=msg,time=time,Type=ype,File=File,Format='input').Save()
        it.dodo()
        it.Save()

        if it.mode.name[:5] == 'start' or it.mode.name[:4] == 'sign':
            ucomplete(it)


    return it.Do()