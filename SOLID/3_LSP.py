### LISKOV'S SUBSTITUTION PRINCIPLE ###

from abc import ABC, abstractmethod

"""
  ! Principio de subsitición de Liskov (LSP)
  * Reemplazo sin afectar la corrección: las implementaciones de una subclase, deben ser reemplazables por las superclase de las que se heredan, sin afectar el programa
  * Contrato de la superclase: los métodos definidos en la superclase establecen un contrato. Cada subclase debe adherirse a este contrato, fuera de sus metodos propios
  * Violaciones del LSP:
    - Retornando un objeto imcopatible por el método de la superclase
    - Lanzando una excepción no lanzada por el método de la superclase
    - Cambiando la semántica o introduciendo efectos secundarios a los métodos del contrato
"""

# Incorrecto


class Bird:
  def fly(self):
    return f"El ave esta volando"

class Pigeon(Bird):
  def fly(self):
    return super().fly()

class Kiwi(Bird):
  def fly(self):
    raise Exception("no puedo volar :c")

def try_fly(bird = Bird):
  print(bird.fly())

try_fly(Pigeon())
# try_fly(Kiwi()) # Exception: no puedo volar :c

class Ave:
  def moverse(self):
    return f"me movi de lugar!"

class PalomaAve(Ave):
  def moverse(self):
    return "estoy volando"

class KiwiAve(Ave):
  def moverse(self):
    return "estoy caminando"

def try_move(ave = Ave):
  print(ave.moverse())

try_move(PalomaAve())
try_move(KiwiAve())
