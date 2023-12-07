
from django.shortcuts import render, redirect
from django.views import View
from ensueño.models import*
from django.db.models import Count
from django.db.models.functions import TruncMonth
from actividades_de_usuario.models import*
from django.http import JsonResponse

class MyCustomDashboard(View):
    template_name = 'admin/dashboard/custom_dashboard.html'

    def get(self, request, *args, **kwargs):
        total_reservas = Reserva.objects.count()
        total_usuarios = Usuario.objects.count()
        total_testimonios = Testimonio.objects.count()

        ambientes = Ambiente.objects.all()
        data_ambientes = [{'label': ambiente.nom_ambiente, 'data': ambiente.reserva_set.count()} for ambiente in ambientes]

        data_mesas_por_ambiente = [ambiente.total_mesas for ambiente in ambientes]
        labels_mesas_por_ambiente = [ambiente.nom_ambiente for ambiente in ambientes]

        categorias = Categoria.objects.all()
        data_categorias = [{'label': categoria.nombre, 'data': categoria.menu_set.count()} for categoria in categorias]

        eventos = Evento.objects.all()
        data_eventos = [{'label': evento.nombre, 'data': evento.reserva_set.count()} for evento in eventos]
        
        reservas_por_mes = Reserva.objects.annotate(
            month=TruncMonth('fecha_reserva')
        ).values('month').annotate(count=Count('id_reserva')).order_by('month')

        labels_reservas_por_mes = [entry['month'].strftime('%B %Y') for entry in reservas_por_mes]
        data_reservas_por_mes = [entry['count'] for entry in reservas_por_mes]
        
    
        context = {
            'total_reservas': total_reservas,
            'total_usuarios': total_usuarios,
            'total_testimonios': total_testimonios,
            'data_ambientes': data_ambientes,
            'data_categorias': data_categorias,
            'data_eventos': data_eventos,
            'categorias': categorias, 
            'data_mesas_por_ambiente': data_mesas_por_ambiente,
            'labels_mesas_por_ambiente': labels_mesas_por_ambiente, 
            'labels_reservas_por_mes': labels_reservas_por_mes,
            'data_reservas_por_mes': data_reservas_por_mes,
        }
        return render(request, self.template_name, context)
    
    def my_custom_chart_widget(self):
        chart_data = {
            "labels": ["Categoría 1", "Categoría 2", "Categoría 3"],
            "data": [Categoria.objects.get(id=1).platos.count(),
                     Categoria.objects.get(id=2).platos.count(),
                     Categoria.objects.get(id=3).platos.count()]
        }
        return chart_data
    