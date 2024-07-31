### DUNDER METHODS ###

"""
  Son metodos para las clases en python, definiran como interactuar la clase
"""

class Person():
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def __str__(self) -> str:
    return f"name: {self.name}, age: {self.age}"

  def __add__(a, b):
    new_name = f"{a.name} {b.name}"
    new_age = a.age + b.age
    return Person(new_name, new_age)

person_1 = Person("Ronald", 19)
print(person_1)

person_2 = Person("Ayelen", 19)
person_3 = person_1 + person_2
print(person_3)
