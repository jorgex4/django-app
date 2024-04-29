from django.urls import path
from . import views

urlpatterns = [
    path("Cliente", views.Cliente, name='cliente_list'),
    path("Transaccion", views.Transaccion, name='transactions'),
]