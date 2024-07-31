### ABSTRACT CLASSES ###

"""
  * Las clases abstractas no pueden ser instanciadas
  * Pueden tener metodos abstractos o con implementacion
  * Los metodos abstractos no tienen logica interna
  * Las subclases que heredan de las clases abstractas tienen que implementar
    los metodos abstractos, o tambien se les considera como clase abstracta (1)
"""

from abc import ABC, abstractmethod

class Persona(ABC):
  def __init__(self, nombre, edad, sexo, actividad):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.actividad = actividad

  @abstractmethod
  def hacer_actividad(self):
    pass

  def presentarse(self):
    print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} anios")

class Estudiante(Persona):
  def __init__(self, nombre, edad, sexo, actividad):
    super().__init__(nombre, edad, sexo, actividad)

  def hacer_actividad(self):
    return f"Estoy estudiando {self.actividad}..."

class Trabajador(Persona):
  def __init__(self, nombre, edad, sexo, actividad):
    super().__init__(nombre, edad, sexo, actividad)

  def hacer_actividad(self):
    return f"Estoy trabajando en {self.actividad}..."

estudiante_1 = Estudiante("Ronald", 19, "masculino", "Programacion")
estudiante_1.presentarse()
print(estudiante_1.hacer_actividad())

trabajador_1 = Trabajador("Ayelen", 19, "Femenino", "Dibujo digital")
trabajador_1.presentarse()
print(trabajador_1.hacer_actividad())
