### CLASS ###
class Celular:
  # Constructor -> metodo que siempre se ejecuta al instanciar la clase
  def __init__(self, marca, modelo, camara) -> None:
    # Atributos de instancia
    self.marca = marca
    self.modelo = modelo
    self.camara = camara

  # Metodo -> funcion de una clase
  def llamar(self):
    print(f"Llmando desde un {self.modelo}")

## Objeto -> Instancia de un objeto
celular_1 = Celular('Samsung', "S23", "48Mp")
celular_2 = Celular('Apple', "Iphone 15 pro", "48Mp")

print(celular_1.modelo)
celular_2.llamar()
