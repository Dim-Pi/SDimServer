from Damasanj.models import User ,MSG
from Damasanj.views import start


def NewUser(Type ,id ,msg ,time ,File):
    ms = MSG(body=msg,time=time,File=File,Type=Type,id=id)
    ms.save()
    it = User(Sid=id,lastmsg=ms)
    it.save()
    it.do(start.start0)
