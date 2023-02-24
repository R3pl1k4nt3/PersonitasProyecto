from django.db import models

# Create your models here.

class Unidad(models.Model):
    unidad = models.CharField(max_length=255)


class Departamento(models.Model):
  
    departamento = models.CharField(max_length=255)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

class Negociado(models.Model):

    negociado = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
class Persona(models.Model):
    EMPLEOS = [
        ("General", "General"),
        ("Coronel", "Coronel"),
        ("Teniente Coronel", "Teniente Coronel"),
        ("Comandante", "Comandante"),
        ("Capitán", "Capitán"),
        ("Teniente","Teniente"),
        ("Subteniente","Subteniente"),
        ("Brigada", "Brigada"),
        ("Sargento 1º", "Sargento 1º"),
        ("Sargento", "Sargento"),
        ("Cabo Mayor", "Cabo Mayor"),
        ("Cabo 1º", "Cabo 1º"),
        ("Cabo", "Cabo"),
        ("Guardia Civil", "Guardia Civil"),
    ]

    empleo = models.CharField(max_length=255, choices=EMPLEOS)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    fecha_incorporacion = models.DateField()
    fotografia = models.ImageField(null=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Usuario(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)