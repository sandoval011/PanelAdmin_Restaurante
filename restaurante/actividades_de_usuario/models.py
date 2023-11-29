from django.db import models
from ensueño.models import*


from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def get_email(self):
            return self.email

    def get_password(self):
        return self.password
    
    def check_password(self, raw_password):
        return raw_password == self.password

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name_plural = "Usuarios"


@receiver(post_save, sender=Usuario)
def crear_token(sender, instance, created, **kwargs):
    if created and instance.token is None:
        instance.token = uuid.uuid4()
        instance.save()
   
class Reserva(models.Model):
    id_reserva =models.AutoField(primary_key=True)
    nom_cliente= models.ForeignKey(Usuario,on_delete=models.CASCADE) 
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    num_personas=models.IntegerField()
    fecha_evento = models.DateTimeField('Fecha del evento')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('cancelada', 'Cancelada')],
        default='pendiente'
    )

    def __str__(self):
        return str(self.nom_cliente)
    
    class Meta:
            verbose_name_plural = "Reservas"
            
    
class Testimonio(models.Model):
    id_testimonio = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    testimonio = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField('Fecha de Publicación')
    estado = models.BooleanField(default=True) 

    def __str__(self):
            return self.testimonio
    class Meta:
            verbose_name_plural = "Testimonios"

class Favorito(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    favorito = models.ForeignKey(Menu,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.favorito)
    
    class Meta:
            verbose_name_plural = "Favoritos"


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    codigo_pago = models.CharField(max_length=20)
    nombre_cliente= models.ForeignKey(Usuario,on_delete=models.CASCADE) 
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    metodo_de_pago= models.ForeignKey(MetodoPago,on_delete=models.CASCADE) 
    fecha_y_hora = models.DateTimeField()
    estado_pago = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('cancelado', 'Cancelado')],
        default='pendiente'
    )

    def __str__(self):
            return self.codigo_pago
    
    class Meta:
            verbose_name_plural = "Pagos"