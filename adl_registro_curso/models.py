from django.db import models
from django.core.exceptions import ValidationError

class Estudiante(models.Model):
  rut = models.CharField(max_length=9, primary_key=True)
  nombre = models.CharField(max_length=50, null=False, blank=False)
  apellido = models.CharField(max_length=50, null=False, blank=False)
  fecha_nac = models.DateField(null=False)
  activo = models.BooleanField(default=False)
  creacion_registo = models.DateField(auto_now_add=True)
  modificacion_registro = models.DateField(auto_now=True)
  creado_por = models.CharField(max_length=50)
  cursos = models.ManyToManyField("Curso", null=False, blank=False, related_name="estudiantes")

  def __str__(self):
    return f"[{self.rut}]: {self.nombre} {self.apellido}"

class Direccion(models.Model):
  calle = models.CharField(max_length=50, null=False)
  numero = models.CharField(max_length=10, null=False)
  dpto = models.CharField(max_length=10)
  comuna = models.CharField(max_length=50, null=False)
  ciudad = models.CharField(max_length=50, null=False)
  region = models.CharField(max_length=50, null=False)
  estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)


class Profesor(models.Model):
  rut = models.CharField(max_length=9, primary_key=True)
  nombre = models.CharField(max_length=50, null=False, blank=False)
  apellido = models.CharField(max_length=50, null=False, blank=False)  
  activo = models.BooleanField(default=False)
  creacion_registo = models.DateField(auto_now_add=True)
  modificacion_registro = models.DateField(auto_now=True)
  cursos = models.ManyToManyField("Curso", null=False, blank=False, related_name="profesores")
  creado_por = models.CharField(max_length=50)

  def clean(self):
    if len(self.rut) > 9 or len(self.rut) < 9:
      raise ValidationError("Rut no es válido, debe tener 9 caracteres") 

  def save(self, *args, **kwargs):
    self.clean()
    super().save(*args, kwargs)

  def __str__(self):
    return f"[{self.rut}]: {self.nombre} {self.apellido}"

class Curso(models.Model):
  codigo = models.CharField(max_length=10, primary_key=True)
  nombre = models.CharField(max_length=50, null=False)
  version = models.IntegerField()

  def __str__(self):
    return f"[{self.codigo}]: {self.nombre}"

