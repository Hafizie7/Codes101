from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^display_SingleBed$', display_SingleBed, name='display_SingleBed'),
    url(r'^display_Double_bed$', display_Double_bed, name='display_Double_bed'),
    url(r'^display_Customer$', display_Customer, name='display_Customer'),
]
