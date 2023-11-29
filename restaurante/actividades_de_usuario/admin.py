from django.contrib import admin
from .models import *
from .tables import *
from .forms import *

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id_usuario', 'nombre', 'apellido', 'password', 'email']
    table = UsuarioTable
    form = UsuarioForm

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id_reserva', 'nom_cliente','ambiente', 'evento','num_personas','fecha_evento', 'fecha_reserva','estado']
    list_filter = ['nom_cliente','ambiente'] 
    form = ReservaForm

    actions = ['aceptar_reservas', 'cancelar_reservas']

    def aceptar_reservas(self, request, queryset):
        queryset.update(estado='aceptada')

    def cancelar_reservas(self, request, queryset):
        queryset.update(estado='cancelada')

    aceptar_reservas.short_description = "Aceptar reservas seleccionadas"
    cancelar_reservas.short_description = "Cancelar reservas seleccionadas"

@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ['id_testimonio','usuario','testimonio','fecha_publicacion','estado']
    table = TestimonioTable
    list_filter = ['usuario']

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ['id_favorito','favorito','usuario']
    list_filter = ['favorito']
    list_filter = ['usuario']
    table = FavoritoTable

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['id_pago','codigo_pago','nombre_cliente','monto','descripcion','metodo_de_pago','fecha_y_hora','estado_pago']
    list_filter = ['nombre_cliente','metodo_de_pago']
    table = PagoTable


