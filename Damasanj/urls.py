from django.urls import path
from Damasanj import views

from Damasanj.driver import mdriver,redriver

urlpatterns = [
    path('Fr/',views.fr),
    path('message/<str:ype>/<str:id>/<str:msg>/<int:time>/<str:File>/',mdriver),
    path('message/request/',redriver)

]











