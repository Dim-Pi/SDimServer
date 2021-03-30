from django.apps import AppConfig
from json import loads
_settings = loads(open("SDimServer/settings.json",'r').read())

class DamasanjConfig(AppConfig):
    name = 'Damasanj'
    Sid  = _settings['token']
    Aid  = "1UGgWYRWoxeafE2VPZTzUZ-YFgheBOWeypJSddLi5Fyo-_qUGl_eAKOF9Jc" 
    Adid = ["1UGgWYRWoxeafE2VPZTzUZ-YFgheBOWeypJSddLi5Fyo-_qUGl_eAKOF9Jc","1uxTbAgywOEtM3SfU5YtuXA6Hf115TOPj9ku6p9vMlw5xfSLRpET16N8SnQ"]
