class Character():
  def __init__(self, name, power, speed, id_character = None) -> None:
    self.name = name
    self.power = power
    self.speed = speed
    self.__id_character = id_character

  def show_info_basic(self) -> str:
    return f"""
    Nombre: {self.name}
    Poder: {self.power}
    Velocidad: {self.speed}"""

  @property
  def id_character(self):
    return self.__id_character

  @id_character.setter
  def id_character(self, id):
    self.__id_character = id

  def __str__(self) -> str:
    return f"""
    Nro. Personaje: {self.__id_character}
    Nombre: {self.name}
    Poder: {self.power}
    Velocidad: {self.speed}"""

  def __add__(a, b):
    name_a = a.name
    name_b = b.name
    if len(a.name) > 3:
      name_a = a.name[0:3]
    if len(b.name) > 3:
      name_b = b.name[-3:]

    new_name_character = name_a + name_b
    new_power_character = ((a.power + b.power)/2) ** 1.35
    new_speed_character = ((a.speed + b.speed)/2) ** 1.35
    return Character(new_name_character, new_power_character, new_speed_character)
