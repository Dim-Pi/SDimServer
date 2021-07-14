from django.apps import AppConfig
from json import loads

_settings = loads(open("SDimServer/settings.json",'r').read())


class PortConfig (AppConfig):
    name = "Port"


class Damasanj : 
    Sid  = _settings['token']
    Aid  = "1UGgWYRWoxeafE2VPZTzUZ-YFgheBOWeypJSddLi5Fyo-_qUGl_eAKOF9Jc"


