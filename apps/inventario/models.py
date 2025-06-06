from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    dni = models.CharField()
    correo = models.CharField()

    def __str__(self):
        return self.nombre
# Create your models here.
class Computadora(models.Model):
    marca= models.CharField()
    num_serie= models.CharField()
    descripcion= models.CharField()
    numero= models.CharField()

    def __str__(self):
        return self.numero
    
class Curso(models.Model):
    nombre = models.CharField()

    def __str__(self):
        return self.nombre
        
class Materia(models.Model):
    nombre = models.CharField()
    Curso= models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    fecha = models.CharField()
    Curso= models.ForeignKey(Curso, on_delete= models.CASCADE)
    Computadora = models.ForeignKey(Computadora, on_delete= models.CASCADE)
    Estudiante= models.ForeignKey(Estudiante, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.fecha}{self.num_comp}"           