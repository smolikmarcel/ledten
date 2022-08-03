from django.urls import path, re_path
from . import views

app_name = 'produkty'

urlpatterns = [
    path('', views.produkty, name='produkty'),
    path('<slug:code>', views.produkt_detail, name='detail'),
    #path('<slug:category>', views.produkty_f, name='produkty_f'),
]
