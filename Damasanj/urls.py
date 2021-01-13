from django.urls import path
from Damasanj import views

from Damasanj.driver import driver

urlpatterns = [
    path('Fr/',views.fr),
    path('massage/<str:Type>/<str:id>/<str:msg>/<int:time>/<str:File>/',driver)

]











