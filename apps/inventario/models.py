from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    dni = models.CharField()
    correo = models.CharField()

    def __str__(self):
        return self.nombre
# Create your models here.
class computadora(models.Model):
    marca= models.CharField()
    num_serie= models.CharField()
    descripcion= models.CharField()
    numero= models.CharField()

    def __str__(self):
        return self.numero
    
class curso(models.Model):
    nombre = models.CharField()

    def __str__(self):
        return self.nombre
        
class materia(models.Model):
    nombre = models.CharField()

    def __str__(self):
        return self.nombre

class prestamo(models.Model):
    fecha = models.CharField()
    nombre_est= models.CharField()
    materia= models.CharField()
    curso= models.CharField()
    num_comp= models.CharField()

    def __str__(self):
        return f"{self.fecha}{self.num_comp}"           