from character import Character
import re

list_characters = list()
option = 0

def validation(option):
  reg_num = r"^[1-4]$"
  just_one_number = re.match(reg_num, option)

  if not(just_one_number):
     print("\n! Seleccione una opcion valida")
     return False
  return True

def create_character():
  name = input("\nIngrese el nombre del personaje: ")
  power = input("Ingrese el poder del personaje: ")
  speed = input("Ingrese la velocidad del personaje: ")
  index = len(list_characters)

  return Character(name, float(power), float(speed), index)

def characters_listing(list):
  for i in list:
    print(i)

def merge_characters(index_a, index_b):
  if len(list_characters) < 2:
    print("\n! No hay suficientes personajes para fucionar" +
          "\n! Cree un personaje para comenzar a fucionar")
    return False
  if (index_a >= len(list_characters) or index_a < 0) or (index_b >= len(list_characters) or index_b < 0):
    print("\n! Ingrese un Nro. Personaje valido")
    return False
  if index_a == index_b:
    print("\n! No se pueden fucionar el mismo personaje")
    return False

  character_a = list_characters[index_a]
  character_b = list_characters[index_b]
  merge = character_a + character_b
  return merge

while option != '4':
  print("""
  Opciones de programa de personajes:
  1. Crear personaje
  2. Fusionar personaje
  3. Mostrar personaje
  4. Salir""")

  while True:
    option = input("\nSeleccione una opcion: ")
    if validation(option):
      break

  if option == '1':
    new_character = create_character()
    list_characters.append(new_character)
    print(f"\nPersonaje creado con exito! {new_character.show_info_basic()}")

  if option == '2':
    index_a = input("\nIngrese el primer Nro. Personaje: ")
    index_b = input("Ingrese el segundo Nro. Personaje: ")
    new_character = merge_characters(int(index_a), int(index_b))

    if not(new_character):
      continue
    else:
      print(f"\nPersonaje fusionado con exito! {new_character.show_info_basic()}")
      new_character.id_character = len(list_characters)
      list_characters.append(new_character)

  if option == '3':
    characters_listing(list_characters)
else:
  print("\nSaliendo del programa...")
