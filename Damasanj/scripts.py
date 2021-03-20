
try:
    from SDimServer.Damasanj.models import Lesson
    from SDimServer.Damasanj.models import User ,Role ,MSG ,DoAdmin ,Feedback
    from SDimServer.Damasanj.views import start ,keyv
except:
    from Damasanj.models import Lesson
    from Damasanj.models import User ,Role ,MSG ,DoAdmin ,Feedback
    from Damasanj.views import start ,keyv


ig = Feedback.idget



def NewUser(Type ,masen ,Sid ,msg ,time ,File):
    ms = MSG(body=msg,time=time,File=File,Type=Type,Sid=id)
    ms.Save()
    it = User(Sid=Sid,massenger=masen,lastmsg=ms,mode=start.start0)
    it.Save()
    
    return it




def ucomplete(it):

    it.do = True
    case = it.node

    if case == 'start02':
        it.Sname = it.lastmsg.body.strip()
        it.Save()
 
    elif case == 'start1' :
        it.Bname = it.lastmsg.body.strip()
        it.Save()

    elif case == 'sign0_0':

        it.role = Role(name='leader')
        it.sign = False
        DoAdmin (keyv (it.startkey(),str(it),' مدیر پایه ای '))

    
    elif case == 'sign1_0':

        if it.signin() :
            it.sign = True
        else :
            it.jan()
 
    elif case == 'sign1_1':
        
        it.role = Role.objects.get(name='admin.%s' %it.lastmsg.body[2:])
        it.sign = False
        DoAdmin (keyv (it.startkey(),str(it),' %s ' %it.role.Fname ))


    elif case == 'sign2_1':

        if it.signin() :
            it.sign = True
            e = it.role.name
            l = Lesson.objects.get(Ename=e[6:])
            l.dadmin = it
            l.Save()
            it.sign2 = False
            it.sode(ig('adm_start0'))
        else :
            it.do = False
            it.jan()
            it.sode(ig('sign2_1'))
    
        it.Save()




















def admin (it):

    it.do = True
    lmsg = it.lastmsg.body
    
    try:   case = it.node.split('.')[0]    
    except:case = it.node.split('.')[0]
    try:   coma = it.lastmsg.body.split('.')[1]
    except:coma = None

    
    B = lambda n :  case == n 


    if B('adm_start0'):
        it.mode2 = coma
        it.Save()












