from django.urls import path
from . import views

urlpatterns = [
    path("Cliente", views.cliente_list, name='cliente_list'),
    path("Transaccion", views.Transaccion, name='transactions'),
]