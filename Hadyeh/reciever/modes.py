from reciever.models import Mode 
from reciever.models import Keyboard as kb
from reciever.models import Message as msg

start_mode = Mode(name="start_mode",Type='static'
    ,messages=[
        msg(body="به به ازین طرفا؟ چه عجب؟ سلام علیکم!" ,Type='text'
        ,keyboard=kb(    [ [ (  'سلامی گرم بر شما' , '<move>->[name_request_0]' ) ] ]     )
        )
    ]
    
    )



