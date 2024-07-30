### PROPERTIES ###

"""
  El decorador de @properties, se usa para declarar los metodos
  getter, setter & delete de una clase
"""

class Person:
  def __init__(self, name: str, surname: str, age: int, dni: int) -> None:
    self.name = name
    self.surname = surname
    self.age = age
    self.__dni = dni

  # el '@property' sirve para declarar una propiedad de una variable privada
  @property
  def dni(self):
    return self.__dni

  # '@[nombre de propiedad].setter' sirve para declarar el setter de la propiedad
  @dni.setter
  def dni(self, new_dni):
    self.__dni = new_dni

  @dni.deleter
  def dni_delete(self):
    del self.__dni

person_1 = Person("Ronald", "Cueva", 19, 12345678)

# Se puede acceder a todos los atributos de la clase que son publicos
print(person_1.name)
print(person_1.surname)
print(person_1.age)
print(person_1.dni) # para acceder al dni, se utiliza la propiedad 'dni'

# la propiedad dni funcionara como atributo por el setter
person_1.dni = 23654987
print(person_1.dni)

# y se puede borrar ahora el atributo con el del, utilidad no se, pero se puede
del person_1.dni_delete
# print(person_1.dni) # AttributeError: 'Person' object has no attribute '_Person__dni'
