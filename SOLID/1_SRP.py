### SINGLE RESPONSIBILITY PRINCIPLE ###

"""
  ! Principio de Responsabilidad Única (SRP)
  * Cada componente o clase del sistema debe desempeñar una única responsabilidad
    o tarea especifica
  * Modularidad: esto permite que los módulos sean independientes entre sí,
    facilitando su reutilización y prueba de manera aislada
  * Cohesión: se refiere a qué tan estrechamente relacionadas y enfocadas está las
    responsabilidades de un módulo con su proposito principal
  * Garantiza que los cambios futuros en el código solo afexten a una parte del
    sistema, en lugar de propagarse a multiples componentes
"""

# Incorrecto
class Car():
  def __init__(self) -> None:
    self.position = 0
    self.__fuel = 100

  def move_car(self, distance):
    if self.fuel >= distance / 2:
      self.position = distance
      self.fuel -= distance / 2
    else:
      print("No hay suficiente combustible")

  def current_position(self):
    print("Estoy en:", self.position)

  """
    Se puede subdividir la funcionalidad en diferentes clases y no sobrecargar todo
    en una misma clase
  """
  @property
  def fuel(self):
    return self.__fuel

  @fuel.setter
  def fuel(self, amount):
    self.__fuel = amount

print("--- Incorrecto ---")
car_1 = Car()
car_1.move_car(100)
car_1.current_position()
car_1.move_car(100)
car_1.current_position()
car_1.move_car(20)
car_1.current_position()

# Correcto

"""
  Separamos la funcionalidad del tanque del combustible con la del carro en general
  El tanque de combustible maneja su propia logica interna, pero esta estrachamente
  relacionada con el carro
"""

class Tank():
  def __init__(self):
    self.__fuel = 100

  def fuel(self):
    return self.__fuel

  def add_fuel(self, amount):
    self.__fuel += amount

  def consume_fuel(self, amount):
    self.__fuel -= amount

  def show_fuel(self):
    print(f"Tienes {self.__fuel} de combustible")

class Car():
  def __init__(self, tank) -> None:
    self.position = 0
    self.tank = tank

  def move(self, distance):
    if self.tank.fuel() >= distance / 2:
      self.position = distance
      self.tank.consume_fuel(distance / 2)
      print("Has movido el auto exitosamente")
    else:
      self.tank.show_fuel()
      print("No hay suficiente combustible")

  def current_position(self):
    print("Estoy en:", self.position)

print("\n--- Correcto ---")
tank_1 = Tank()
car_2 = Car(tank_1)
car_2.move(20)
car_2.current_position()
car_2.move(40)
car_2.current_position()
car_2.move(60)
car_2.current_position()
car_2.move(100)
car_2.current_position()
