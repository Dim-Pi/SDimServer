from django.apps import AppConfig
from json import loads

_settings = loads(open("SDimServer/settings.json",'r').read())


class SendingConfig (AppConfig):
    name = "Sending"


class Damasanj : 
    Sid  = _settings['token']
    Aid  = "1UGgWYRWoxeafE2VPZTzUZ-YFgheBOWeypJSddLi5Fyo-_qUGl_eAKOF9Jc"


