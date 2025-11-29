from django.urls import path
from . import views

urlpatterns = [
    path('', views.ana_sayfa, name='ana_sayfa'),
    path('siparis/', views.siparis_olustur, name='siparis_olustur'),
    path('iletisim/', views.iletisim_gonder, name='iletisim_gonder'),
]
