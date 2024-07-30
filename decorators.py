### DECORATORS ###

"""
  Los decoradores son funciones que recibiran otras funciones
  (como funciones de orden superior), pero puede ejecutar logica
  antes o despues de ejecutar la funcion
"""
def decorator(function):
    def function_decorator():
        print("hola antes de la funcion")
        function()

    return function_decorator

def greeting():
  print("Saludo, jaja te salude")

func_modify = decorator(greeting)
func_modify() # Retorna la funcion greeting pero con la modificacion

@decorator
def farewell():
  print("adios :C, jaja mentira quien te va a extranar")

farewell()
