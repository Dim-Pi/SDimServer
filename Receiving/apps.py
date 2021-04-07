from json import loads
try: _settings = loads(open("SDimServer/settings.json",'r').read())
except: _settings = loads(open("SDimServer/SDimServer/settings.json",'r').read())

try: 
    from django.apps import AppConfig
except: 
    print ('er\n')
    class  AppConfig : ...

class ReceivingConfig (AppConfig):
    name = "Receiving"


class Damasanj : 
    Sid  = _settings['token']
    Aid  = "1UGgWYRWoxeafE2VPZTzUZ-YFgheBOWeypJSddLi5Fyo-_qUGl_eAKOF9Jc"


