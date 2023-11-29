from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Reserva

def aceptar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.estado = 'aceptada'
    reserva.save()
    return HttpResponse('Reserva aceptada')

def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.estado = 'cancelada'
    reserva.save()
    return HttpResponse('Reserva cancelada')
