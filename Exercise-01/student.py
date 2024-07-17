class Student:
  def __init__(self, name, age, grade) -> None:
    self.name = name
    self.age = age
    self.grade = grade

  def studing(self):
    print(f"{self.name} esta estudiando...")

  def __str__(self) -> str:
    return f"""DATOS DEL ESTUDIANTE:\n
    Nombre: {self.name}
    Edad: {self.age}
    Grado: {self.grade}
  """
