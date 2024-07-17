"""
  Crear una clase Estudiante que tenga los atributos:
  - Nombre
  - Edad
  - Grado
  Además, agregar un metodo a la clase Estudiante que sea "estudiar()" que
  imprima en pantalla: "El estudiante (Estudiante.Nombre) esta estudiando.
  Que permita una interaccion con el usuario, y que este cree una instancia
  de la clase Estudiante brindando los atributos de la clase.
  El usuario al escribir "estudiar" (no case sensitive), utiliza el metodo
  "estudiar()"
"""
from student import Student as Estudiante

print("Ingresando un estudiante...")
name = input("Nombre del estudiante: ")
age= input("Edad del estudiante: ")
grade = input("Grado del estudiante: ")

student = Estudiante(name, age, grade)
print(f"\n{student}")
studing = input("")
while studing.lower() != "estudiar":
  studing = input("")
else:
  student.studing()

