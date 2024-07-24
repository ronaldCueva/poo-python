class Animal:
  def accion(self):
    print("animal esta comiendo")

class Mamifero(Animal):
  def accion(self):
    print("El animal esta amamantando")

class Ave(Animal):
  def accion(self):
    print("El animal esta volando")

class Murcielago(Ave, Mamifero):
  def accion(self):
    return super().accion()

murcielago = Murcielago()
murcielago.accion()
