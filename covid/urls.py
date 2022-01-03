from django.urls import path
from covid.views import *

urlpatterns = [
    path('',world,name='world'),
    path('north_america/',n_america,name='n_america'),
    path('south_america/',s_america,name='s_america'),
    path('asia/',asia,name='asia'),
    path('europe/',europe,name='europe'),
    path('africa/',africa,name='africa'),
    path('oceania/',oceania,name='oceania'),
    path('comment/',comment,name='comment'),
]