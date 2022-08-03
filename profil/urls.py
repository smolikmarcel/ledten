from django.urls import path, re_path
from . import views

app_name = 'profil'

urlpatterns = [
    path('prihlaseni', views.prihlaseni, name='prihlaseni'),
    path('registrace', views.registrace, name='registrace'),
    path('odhlasit', views.odhlasit, name='odhlasit'),
    path('<slug:user>', views.profil, name='profil'),
    path('<slug:user>/objednavky', views.objednavky, name='objednavky'),
    path('<slug:user>/recenze', views.recenze, name='recenze'),
    path('<slug:user>/nastaveni', views.nastaveni, name='nastaveni'),
]
