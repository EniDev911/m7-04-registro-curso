from .models import Curso, Direccion, Estudiante, Profesor
from django.db import IntegrityError

def crear_curso(codigo, nombre, version) -> Curso:
  return Curso.objects.create(
    codigo=codigo,
    nombre=nombre,
    version=version
  )

def crear_profesor(rut, nombre, apellido, creado_por) -> Profesor:
  return Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, creado_por=creado_por)

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por) -> Profesor:
  return Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, creado_por=creado_por)

def crear_direccion(calle: str, numero: str, comuna: str, ciudad: str, region: str, estudiante: Estudiante) -> Direccion:
  return Direccion.objects.create(calle=calle, numero=numero, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)

def obtiene_estudiante(estudiante):
  return Estudiante.objects.get(pk=estudiante.rut)

def obtiene_profesor(profesor):
  return Profesor.objects.get(pk=profesor.rut)

def agrega_profesor_a_curso(profesor: Profesor, curso: Curso):
  try:
    profesor.cursos.add(curso)
    print(f"Se agrego al profesor {profesor.nombre} al curso {curso.nombre}")
  except IntegrityError as e:
    print("Error:", e)
  except Exception as e:
    print("Excepción", e)

def agrega_cursos_a_estudiantes(estudiante: Estudiante, curso: Curso):
  try:
    estudiante.cursos.add(curso)
    print(f"Se agrego al estudiante {estudiante.nombre} al curso {curso.nombre}")
  except IntegrityError as e:
    print("Error:", e)
  except Exception as e:
    print("Excepción", e)  


def imprime_estudiante_cursos(estudiante: Estudiante):
  for curso in estudiante.cursos.all():
    print(curso)