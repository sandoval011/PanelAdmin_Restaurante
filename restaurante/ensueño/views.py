from rest_framework import generics
from ensueño.models import*
from actividades_de_usuario.models import*
from rest_framework.generics import ListCreateAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.db import IntegrityError
from django.shortcuts import get_object_or_404


class AmbienteListCreateView(generics.ListCreateAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    
class AmbienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class EventoListCreateView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    

class MenuDiarioListCreateView(generics.ListCreateAPIView):
    queryset = MenuDiario.objects.all()
    serializer_class = MenuDiarioSerializer

class MenuDiarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuDiario.objects.all()
    serializer_class = MenuDiarioSerializer
    

class UsuarioListCreateView(ListCreateAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        token = self.request.query_params.get('token', None)
        if token:
            return Usuario.objects.filter(token=token)
        return Usuario.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            print(f"Request data: {request.data}")
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            usuario = serializer.save()
            return Response({'token': usuario.token}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'El usuario ya existe.'}, status=status.HTTP_400_BAD_REQUEST)
class UsuarioDetailView(RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
       
        token = self.kwargs.get('token', None)
        if token:
            return get_object_or_404(Usuario, token=token)
        return super().get_object()

class ReservaListCreateView(generics.ListCreateAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        nom_cliente_id = self.kwargs.get('nom_cliente') 

        if nom_cliente_id:
            return Reserva.objects.filter(nom_cliente=nom_cliente_id)
        else:
            return Reserva.objects.all()


class ReservaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer



class TestimonioListCreateView(generics.ListCreateAPIView):
    serializer_class = TestimonioSerializer

    def get_queryset(self):
        usuario_id = self.kwargs.get('usuario_id')

        if usuario_id:
            return Testimonio.objects.filter(usuario_id=usuario_id)
        else:
            return Testimonio.objects.all()

class TestimonioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonio.objects.all()
    serializer_class = TestimonioSerializer

    


class FavoritoListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoritoSerializer

    def get_queryset(self):
        usuario_id = self.kwargs.get('usuario_id')

        if usuario_id:
            return Favorito.objects.filter(usuario_id=usuario_id)
        else:
            return Favorito.objects.all()

class FavoritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer



class MenuCartaListCreateView(generics.ListCreateAPIView):
    queryset = MenuCarta.objects.all()
    serializer_class = MenuCartaSerializer   
     
class MenuCartaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuCarta.objects.all()
    serializer_class = MenuCartaSerializer
    
class PagoListCreateView(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer  
      
class PagoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    
class GaleriaListCreateView(generics.ListCreateAPIView):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer  
      
class GaleriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer


class MenuCartaByCategoriaView(ListCreateAPIView):
    queryset = MenuCarta.objects.all()
    serializer_class = MenuCartaSerializer

    def get_queryset(self):
        categoria_id = self.kwargs['categoria_id']
        return MenuCarta.objects.filter(menu__categoria=categoria_id)
    
from distutils.util import strtobool
class MenuDiarioListView(generics.ListAPIView):
    serializer_class = MenuDiarioSerializer

    def get_queryset(self):
        estado_param = self.kwargs.get('estado', None)
        if estado_param is not None:
            try:
                estado_value = bool(strtobool(estado_param))
            except ValueError:
                estado_value = False
            queryset = MenuDiario.objects.filter(estado=estado_value)
        else:
            queryset = MenuDiario.objects.all()
        return queryset

    

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = Usuario.objects.get(email=email)
            print(f"Usuario encontrado: {user}")
        except Usuario.DoesNotExist:
            print("Usuario no encontrado")
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.check_password(password):
            print("Contraseña válida")
            return Response({'token': str(user.token)})
        else:
            print(f"Contraseña incorrecta. Contraseña esperada: {user.password}, Contraseña proporcionada: {password}")
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
