from django.shortcuts import render
# Create your views here
from .models import Cliente, Transaccion


def Clientes(request):
    Cliente = Cliente.objects.all()
    return render(request, 'finance/cliente_list.html', {'Lista de Clientes': cliente})


def transactions(request):
    transactions = Transaccion.objects.all()
    return render(request, 'finance/transacciones.html', {'Transacciones': transaccion})

