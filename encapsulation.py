### ENCAPSULATION ###

## Clases - curso de python by Mouredev

class Person:
  def __init__(self, name: str, surname: str, age: int) -> None:
    """
      Los modificadores de acceso son convenciones de
      nomenclatura con guiones bajos (_), esto para
      indicar el nivel de acceso de los atributos.
      El Protected en python, como solo es
      nomenclatura, si se puede acceder, pero es mala
      practica.
    """
    self.name = name # Publico (Public)
    self._surname = surname # Protegido (Protected)
    self.__age = age # Privado (Private)
    self.full_name = f"{name} {surname}"

  def person_presentation(self):
    print(f"Hola, mi nombre es {self.name} {self._surname} y tengo {self.__age} anios")

  def pasar_tiempo(self):
    edad_antes = self.__age
    self.__sumar_edad(2)
    print(f"""Paso 2 anios...
          ahora soy mas viejo, tengo {self.__age} anios...
          antes tenia {edad_antes}""")

  """
    Un metodo privado no se puede usar cuando se crea un objeto,
    solo como logica interna dentro de la clase
  """
  def __sumar_edad(self, anio):
    self.__age = self.__age + anio

persona_1 = Person("Ronald", "Cueva", 19)
persona_1.person_presentation()
persona_1.pasar_tiempo()
persona_1.person_presentation()
# persona_1.pasar_tiempo()
# persona_1.person_presentation()
# persona_1.pasar_tiempo()
# persona_1.person_presentation()
# persona_1.pasar_tiempo()
# persona_1.person_presentation()
# persona_1.pasar_tiempo()
# persona_1.person_presentation()

# persona_1.__sumar_edad(5) # Da error porque es un metodo PRIVADO
