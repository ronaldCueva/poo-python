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

class Emplado(Persona):
  def __init__(self, name, age, nacionality, job, salary) -> None:
    """
      El metodo super en python permite utilizar el metodo de la
      clase padre.
      Una clase que hereda las propiedades de una clase padre va
      que tener los mismos parametros que el metodo que hereda
    """
    super().__init__(name, age, nacionality)
    self.job = job
    self.salary = salary

  def work(self):
    return f"{self.name} esta trabajando como {self.job}..."

empleado_1 = Emplado("Ronald", 19, "peruano", "programador", 10000)
persona_1 = Persona("Ayelen", 19, "peruana")

print(empleado_1.speak())
print(empleado_1.work())
print(persona_1.speak())

