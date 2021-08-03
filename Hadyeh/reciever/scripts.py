from reciever.models import User , Messanger
import reciever.modes as modes





def create_new_user (messanger=None,sign_data=None):

    if not messanger and sign_data:
        raise

    user = User(sign_data=sign_data)
    user.mode = modes.start_mode
    user.messanger = messanger
    user.Save()
    return user


    