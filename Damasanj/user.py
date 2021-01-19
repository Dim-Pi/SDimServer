from Damasanj.models import Lesson
from Damasanj.models import User ,Role ,MSG ,DoAdmin
from Damasanj.views import start ,keyv
def NewUser(Type ,Sid ,msg ,time ,File):
    ms = MSG(body=msg,time=time,File=File,Type=Type,Sid=id)
    ms.Save()
    it = User(Sid=Sid,lastmsg=ms,mode=start.start0)
    it.Save()
    
    return it

def ucomplete(it):

    it.do = True
    
    if it.node == 'start02':
        it.Sname = it.lastmsg.body
        it.Save()
 
    elif it.node == 'start1' :
        it.Bname = it.lastmsg.body
        it.Save()

    elif it.node == 'sign0_0':

        it.role = Role(name='leader')
        it.sign = False
        DoAdmin (keyv (it.startkey(),str(it),' مدیر پایه ای '))

    
    elif it.node == 'sign1_0':

        if it.signin() :
            it.sign = True
        else :
            it.jan()
 
    elif it.node == 'sign1_1':
        
        it.role = Role.objects.get(Ename='admin.%s' %it.lastmsg.body[2:])
        it.sign = False
        DoAdmin (keyv (it.startkey(),str(it),' سرگروهی %s ' %it.role.name ))


    elif it.node == 'sign2_1':

        if it.signin() :
            it.sign = True
            e = it.role.Ename
            l = Lesson.objects.get(Ename=e[6:])
            l.dadmin = it
        else :
            it.jan()
    


