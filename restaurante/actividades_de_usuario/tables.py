import django_tables2 as tables
from .models import*

class UsuarioTable(tables.Table):
    class Meta: 
        model = Usuario

class ReservaTable(tables.Table):
    class Meta:
        model = Reserva


class TestimonioTable(tables.Table):
    class Meta:
        model = Testimonio


class FavoritoTable(tables.Table):
    class Meta:
        model = Favorito

class PagoTable(tables.Table):
    class Meta:
        model = Pago