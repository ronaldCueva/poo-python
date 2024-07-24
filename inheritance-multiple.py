### INHERITANCE ###

"""
  Herencia permite que una clase herede Atributos y metodos de una
  clase padre. Permite reutilizar codigo y tener un mejor control
"""

class Persona:
  def __init__(self, name, age, nacionality) -> None:
    self.name = name
    self.age = age
    self.nacionality = nacionality

  def speak(self):
    return f"{self.name} esta hablando..."

class Artista:
  def __init__(self, skill):
    self.skill = skill

  def show_skill(self):
    return f"Mi habilidad es {self.skill}"

class EmpladoArtista(Persona, Artista):
  def __init__(self, name, age, nacionality, skill, job, salary) -> None:
    """
      En python se tiene que llamar a los 2 constructores si se trabaja
      con herencia multiple
    """
    Persona.__init__(self, name, age, nacionality)
    Artista.__init__(self, skill)
    self.job = job
    self.salary = salary

  def work(self):
    return f"{self.name} esta trabajando como {self.job}..."

  """
    Con el super nos aseguramos que el metodo que esta llamando sea de la
    clase padre, pero lo va a estar llamando desde la clase EmpleadoArtista
  """
  def show_skill(self):
    return super().show_skill()

  # def show_skill(self):
  #   return f"No tengo una habilidad, {super().show_skill()}"

empleado_1 = EmpladoArtista("Ronald", 19, "peruano", "dormir", "programador", 10000)

print(empleado_1.speak())
print(empleado_1.work())
print(empleado_1.show_skill())

