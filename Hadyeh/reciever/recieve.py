from Hadyeh.Hadyeh.models import Message
from django.core.checks import messages
from reciever.models import User ,Messanger
from reciever.scripts import create_new_user


def resieve (request):
    messanger_name = request['messanger']
    messanger = Messanger.objects.filter(lambda s : s.name == messanger_name)
    msg = request['message']
    sign_data = msg['sign_data']
    msg = messanger.translate(msg)
    return driver(messanger,sign_data,msg)




def driver (messanger,sign_data,msg:Message):
    try:        user = User.objects.get(sign_data=sign_data)
    except:     user = None
    
    if not user :
        user = create_new_user (messanger=messanger,sign_data=sign_data)
    else:
        ...
    
    duties(user)
    user.route(msg.body)
        





def duties (user:User):
    
    match user.mode.name :
        case _ :
            user.execute()


    

