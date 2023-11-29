from django.urls import path
from .views import *
from .dashboard import*

urlpatterns = [
    path('ambientes/', AmbienteListCreateView.as_view(), name='Lista-Ambiente-Create'),
    path('ambientes/ <int:pk>/', AmbienteDetailView.as_view(), name='Ambiente-Detalle'),
    path('categorias', CategoriaListCreateView.as_view(), name='Lista-Categoria-Create'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='Categoria-Detalle'),
    path('menus/', MenuListCreateView.as_view(), name='Lista-Menu-Create'),
    path('menus/<int:pk>/', MenuDetailView.as_view(), name='Detalle-Menu'),
    path('eventos/', EventoListCreateView.as_view(), name='Lista-Evento-Create'),
    path('eventos/<int:pk>/', EventoDetailView.as_view(), name='Detalle-Evento'),
    path('menudiario/', MenuDiarioListCreateView.as_view(), name='Lista-Menudiario-Create'),
    path('menudiario/<int:pk>/', MenuDiarioDetailView.as_view(), name='Detalle-Menudiario'),
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/detalle/token=<str:token>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('reservas/nom_cliente/<int:nom_cliente>/', ReservaListCreateView.as_view(), name='reserva-list-create'),
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detail'),
    path('reservas/', ReservaListCreateView.as_view(), name='reserva-list'),
    
    path('testimonios/usuario/<int:usuario_id>/', TestimonioListCreateView.as_view(), name='testimonio-list-create'),
    path('testimonios/<int:pk>/', TestimonioDetailView.as_view(), name='testimonio-detail'),
    path('testimonios/', TestimonioListCreateView.as_view(), name='testimonio-list'),
    
    path('favoritos/usuario/<int:usuario_id>/', FavoritoListCreateView.as_view(), name='favorito-list-create'),
    path('favoritos/<int:pk>/', FavoritoDetailView.as_view(), name='favorito-detail'),
    path('favoritos/', FavoritoListCreateView.as_view(), name='favorito-list'),
    
    path('menuCarta/', MenuCartaListCreateView.as_view(), name='Lista-MenuCarta-Create'),
    path('menuCarta/<int:pk>/', MenuCartaDetailView.as_view(), name='Detalle-MenuCarta'),
    path('pagos/', PagoListCreateView.as_view(), name='Lista-Pago-Create'),
    path('pagos/<int:pk>/', PagoDetailView.as_view(), name='Detalle-Pago'),
    path('galerias/', GaleriaListCreateView.as_view(), name='Lista-Galeria-Create'),
    path('galerias/<int:pk>/', GaleriaDetailView.as_view(), name='Detalle-Galeria'),
    path('menuCarta/categoria/<int:categoria_id>/', MenuCartaByCategoriaView.as_view(), name='menu-carta-categoria'),
    path('menudiario/estado/<str:estado>/', MenuDiarioListView.as_view(), name='menu-diario-list'),
    path('pagina-personalizada/', MyCustomDashboard.as_view(), name='pagina_personalizada'),
    path('login/', LoginView.as_view(), name='login'),
]