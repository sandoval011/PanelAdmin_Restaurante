import django_tables2 as tables
from .models import*


class AmbienteTable(tables.Table):
    class Meta: 
        model = Ambiente

class CategoriaTable(tables.Table):
    class Meta: 
        model = Categoria


class MenuTable(tables.Table):
    class Meta: 
        model = Menu

class EventoTable(tables.Table):
    class Meta:
        model = Evento
        

class MenuDiarioTable(tables.Table):
    class Meta:
        model = MenuDiario
        
class MenuCartaTable(tables.Table):
    class Meta:
        model = MenuCarta

class MetodoPagoTable(tables.Table):
    class Meta:
        model = MetodoPago

class GaleriaTable(tables.Table):
    class Meta:
        model = Galeria