### INTERFACE SEGREGATION PRINCIPLE ###

from abc import ABC, abstractmethod

"""
  ! Principio de segregación de interfaces
  * Se enfoca en crear interfaces para subdividir tareas en cada interfaz
  * Evita que clases tengan métodos inecesarios
  * Define interfaces con funcionalidades especificas y cohesivas, mejorando la modularidad y flexibilidad para diferentes contextos
"""

# Incorrecto
class ImprentaInterface(ABC):

  @abstractmethod
  def blanco_negro(self):
    pass

  @abstractmethod
  def color(self):
    pass

  @abstractmethod
  def scanear(self):
    pass

  @abstractmethod
  def enviar_fax(self):
    pass

class ImpresoraSimple(ImprentaInterface):
  def blanco_negro(self):
    return super().blanco_negro()

  def color(self):
    return super().color()
  """ no se usan todos los metodos por el tipo de impresora, tiene carga de funcionalidades inecesarias """
  def scanear(self):
    pass

  def enviar_fax(self):
    pass

# Correcto

class PrintBWInterface(ABC):
  @abstractmethod()
  def print_BW(self):
    pass

class PrintColorInterface(ABC):
  @abstractmethod()
  def print_color(self):
    pass

class ScannerInterface(ABC):
  @abstractmethod()
  def scanner(self):
    pass

class FaxInterface(ABC):
  @abstractmethod()
  def send_fax(self):
    pass

class SimplePrinter(PrintBWInterface, PrintColorInterface):
  """
    Solo usa las interfaces con los metodos que necesita, no tiene la sobrecarga de
    metodos inecesarios
  """
  def print_BW(self):
    return super().print_BW()

  def print_color(self):
    return super().print_color()

class CorporatePrinter(PrintBWInterface, PrintColorInterface, ScannerInterface, FaxInterface):
  """
    Puede implementar mas interfaces con funcionalidades especificas, modularizando
    cada funcionalidad que tiene
  """
  def print_BW(self):
    return super().print_BW()

  def print_color(self):
    return super().print_color()

  def scanner(self):
    return super().scanner()

  def send_fax(self):
    return super().send_fax()
