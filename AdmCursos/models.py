from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.IntegerField()
    fecha_alta = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.apellido + ' ' + self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.IntegerField()
    fecha_alta = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.apellido + ' ' + self.nombre   

class Curso_Docente(models.Model):
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente_id = models.ForeignKey(Docente, on_delete=models.CASCADE)

class Curso_Alumno(models.Model):
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE)
