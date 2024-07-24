class Persona:
  def __init__(self, nombre, edad) -> None:
    self.nombre = nombre
    self.edad = edad

  def mostrar_datos(self):
    print(f"Nombre: {self.nombre}\nEdad: {self.edad}")

class Estudiante(Persona):
  def __init__(self, nombre, edad, grado) -> None:
    super().__init__(nombre, edad)
    self.grado = grado

  def informacion_estudiante(self):
    print(f"Grado: {self.grado}")

student = Estudiante("Ronald", 19, 5)

student.mostrar_datos()
student.informacion_estudiante()
