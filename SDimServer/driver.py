from sys import path 
from library import location , fos
loc = location()
slash = fos()
rl = [
    'Damasanj',
]
for q in rl :
    path.append (loc+slash+q+slash+'apps.py')

from apps import DamasanjConfig

 cv
