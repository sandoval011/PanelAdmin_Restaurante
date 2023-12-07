from django.urls import path
from . import views

urlpatterns = [
    path('aceptar_reserva/<int:reserva_id>/', views.aceptar_reserva, name='aceptar_reserva'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
]
