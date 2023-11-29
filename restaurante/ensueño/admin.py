from os import path
from django.contrib import admin
from django.contrib.sessions.models import Session
from django.utils.safestring import mark_safe
from .models import *
from .tables import *
from .dashboard import*
from django.contrib.admin import AdminSite
from .views import*


@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'id_ambiente', 'nom_ambiente', 'total_mesas', 'estado']
    table = AmbienteTable

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="60" height="60" />')

    display_image.short_description = 'Image'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'id_categoria', 'nombre', 'estado']
    table = CategoriaTable

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="60" height="60" />')

    display_image.short_description = 'Image'

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'id_menu', 'nombre', 'precio', 'descripcion', 'categoria', 'estado']
    list_filter = ['categoria']
    table = MenuTable

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="60" height="60" />')

    display_image.short_description = 'Image'

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id_evento', 'nombre']
    table = EventoTable


@admin.register(MenuDiario)
class MenuDiarioAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'id_menuDiario', 'menu', 'precio', 'descripcion','estado']
    table = MenuDiarioTable

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.menu.img.url}" width="60" height="60" />')

    display_image.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        existe_menu_diario = MenuDiario.objects.filter(menu=obj.menu).exclude(id_menuDiario=obj.id_menuDiario).exists()

        if existe_menu_diario:
            message = 'No sé insertó el menú, por que ya ha sido añadido como Menú Diario.'
            self.message_user(request, message, level='ERROR')
        else:
            super().save_model(request, obj, form, change)

@admin.register(MenuCarta)
class MenuCartaAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'id_menuCarta', 'menu', 'precio', 'descripcion','estado']
    table = MenuDiarioTable

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.menu.img.url}" width="60" height="60" />')

    display_image.short_description = 'Image'

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ['id_metodoPago', 'metodo_pago']
    table = MetodoPagoTable

@admin.register(Galeria)
class Galeria(admin.ModelAdmin):
    list_display = ['display_image','id_galeria','tipo']
    table = GaleriaTable
    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="60" height="60" />')
    display_image.short_description = 'Image'