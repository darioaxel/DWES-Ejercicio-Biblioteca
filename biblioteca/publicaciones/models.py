from django.db import models

# Create your models here.
class Unidad(models.Model):
    ESTADOS_UNIDAD = [
        ('nueva', 'Nueva'),
        ('usada', 'Usada'),
        ('deteriorada', 'Deteriorada'),
        ('retirar', 'A retirar'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_UNIDAD)
    def __str__(self):
        return self.titulo

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=300)
    fecha_nacimiento = models.DateField()
 
    def __str__(self):
        return self.nombre
    
class Publicacion(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    editorial = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(auto_now_add=True)
    TIPO_PUBLICACION = [
        ('libro', 'Libro'),
        ('articulo', 'Articulo')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_PUBLICACION)

    unidad = models.ManyToManyField(Unidad, related_name='publicaciones')
    autor = models.ManyToManyField(Autor, related_name='publicaciones')

    def __str__(self):
        return f"{self.titulo} - {self.ISBN}"