from django.db import models

# Create your models here.

class Ambiente(models.Model):
    img = models.ImageField()
    id_ambiente = models.AutoField(primary_key=True)
    nom_ambiente = models.CharField(max_length=60)
    total_mesas = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)  
    
    def __str__(self):
            return self.nom_ambiente
    class Meta:
        verbose_name_plural = "Ambientes"
    

class Categoria(models.Model):
    img = models.ImageField()
    id_categoria = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=60)
    estado = models.BooleanField(default=True) 
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorias"
    
    
class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=60)  
    
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name_plural = "Eventos"

        
    
from django.db import models

        
class Menu(models.Model):
    img = models.ImageField()
    id_menu =models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    precio =models.DecimalField(max_digits=6,decimal_places=2)
    descripcion = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)  
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Menus"
    

class MenuDiario(models.Model):
    id_menuDiario = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menus_diarios', limit_choices_to={'estado': True})
    estado = models.BooleanField(default=True) 
    
    def img(self):
        return self.menu.img

    def precio(self):
        return self.menu.precio

    def descripcion(self):
        return self.menu.descripcion

    def _str_(self):
        return str(self.menu)

    class Meta:
        verbose_name_plural = "Menus Diarios"

class MenuCarta(models.Model):
    id_menuCarta = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menus_carta', limit_choices_to={'estado': True})
    estado = models.BooleanField(default=True)

    def display_image(self):
        return self.menu.img

    def precio(self):
        return self.menu.precio

    def descripcion(self):
        return self.menu.descripcion

    def __str__(self):
        return str(self.menu)

    class Meta:
        verbose_name_plural = "Menus a la Carta"

class MetodoPago(models.Model):
    id_metodoPago = models.AutoField(primary_key=True)
    metodo_pago= models.CharField(max_length=50) 
    
    def __str__(self):
            return self.metodo_pago
    
    class Meta:
            verbose_name_plural = "Métodos de Pago"


class Galeria(models.Model):
    id_galeria = models.AutoField(primary_key=True)
    img = models.ImageField()
    tipo = models.CharField(
        max_length=20,
        choices=[('ambiente', 'Ambiente'), ('menu', 'Menu')],
        default='ambiente'
    )
    def _str_(self):
            return str(self.img)
    
    class Meta:
            verbose_name_plural = "Galería de Imágenes"

