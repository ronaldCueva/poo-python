### ABSTRACTION ###

"""
  La abstraccion es ocultar la logica interna al usuario
  y mostrarle solo la informacion esencial
"""
class Auto():
  def __init__(self) -> None:
    self._estado = "apagado"

  def encender(self):
    self._estado = "encendido"
    print("El auto esta encendido")

  def conducir(self):
    if self._estado == 'apagado':
      self.encender()
    print('Conduciendo...')

auto_1 = Auto()
"""
  Al llamar al metodo de conducir, esta aplicando logica
  interna que el usuario no esta viendo
"""
auto_1.conducir()
