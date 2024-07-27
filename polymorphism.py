### POLYMORPHISM ###

"""
  En mi definicion lo que entendi:
  Polimorfismo permite ejecutar una funcion o un metodo que puede tener
  una logica diferente segun el objeto o quien lo esta ejecutando
"""

class Animal:
  def sonido(self, string):
    return string

class Gato(Animal):
  def sonido(self):
    return super().sonido("meoww")

class Perro(Animal):
  def sonido(self):
    return super().sonido("guau")

# Polimorfismo de funcion
perro_1 = Perro()
gato_1 = Gato()

print(perro_1.sonido())
print(gato_1.sonido())

# Polimorfismo de funcion
def ejecutar_sonido(obj: Animal):
  print(obj.sonido())

ejecutar_sonido(perro_1)
ejecutar_sonido(gato_1)
