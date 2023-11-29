from rest_framework import serializers
from ensueño.models import*
from actividades_de_usuario.models import*


from django.contrib.auth import get_user_model


class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'       
         
        
class MenuDiarioSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(source='menu.img', read_only=True)
    nombre = serializers.CharField(source='menu.nombre', read_only=True)
    precio = serializers.DecimalField(source='menu.precio', max_digits=6, decimal_places=2, read_only=True)
    descripcion = serializers.CharField(source='menu.descripcion', read_only=True)
    estado = serializers.BooleanField()
    
    class Meta:
        model = MenuDiario
        fields = '__all__' 
        
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


        
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model =Reserva
        fields = '__all__'  
        
class TestimonioSerializer(serializers.ModelSerializer):
    class Meta:
        model =Testimonio
        fields = '__all__'  
        
class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Favorito
        fields = '__all__' 

class MenuCartaSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(source='menu.img', read_only=True)
    nombre = serializers.CharField(source='menu.nombre', read_only=True)
    precio = serializers.DecimalField(source='menu.precio', max_digits=6, decimal_places=2, read_only=True)
    descripcion = serializers.CharField(source='menu.descripcion', read_only=True)

    class Meta:
        model = MenuCarta
        fields = '__all__'   

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Pago
        fields = '__all__'

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model =Galeria
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)