from django.urls import path
from . import views

app_name = 'jess_project'

urlpatterns = [
    path('', views.home, name='home'),
    path('kasir/', views.kasir, name='kasir'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('tambah-pesanan/', views.add_order, name='tambah-pesanan'),
]
