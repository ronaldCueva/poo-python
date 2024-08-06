### OPEN/CLOSED PRINCIPLE ###

from abc import ABC, abstractmethod

"""
  ! El principio de abierto y cerrado (OCP)
  * "Abiertas para extensión pero cerradas para modificación"
  * Extensibilidad: se deben poder agregar nuevas funcionalidades o extensiones al sistema sin alterar el código existente
  * Inmutabilidad del código existente: una vez que una clase o módulo ha sido implementado y probado, no debería ser modificado
  * Uso de Abstracciones: esto mediante el uso de herencia, interfaces y patrones de diseño, sin romper partes actuales y probadas
"""

# Incorrecto
class Notifier:
  def __init__(self, user, message) -> None:
    self.user = user
    self.message = message

  def notify(self, user): # si se cambia el nombre y ya se implemento va a comenzar a fallar en todas partes que se implementó
    print(f"Enviando email a: {user.email}")

  def notify_sms(self, user):
    print(f"Enviando sms a: {user.sms}")

# Correcto
class Notifier(ABC):
  def __init__(self, user, message) -> None:
    self.user = user
    self.message = message

  @abstractmethod
  def notify(self):
    pass
# Permite la escabilidad por las clases, separa la funcionalidad
class NotifyEmail(Notifier):
  def __init__(self, user, message) -> None:
    super().__init__(user, message)

  def notify(self):
    return f"Enviando email a: {self.user.email}"

class NotifySMS(Notifier):
  def __init__(self, user, message) -> None:
    super().__init__(user, message)

  def notify(self):
    return f"Enviando sms a: {self.user.sms}"

class NotifyWhatsApp(Notifier):
  def __init__(self, user, message) -> None:
    super().__init__(user, message)

  def notify(self):
    return f"Enviando whatsapp a: {self.user.whatsapp}"
