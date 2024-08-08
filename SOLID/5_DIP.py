### DEPENDENCY INVERSION PRINCIPLE ###

from abc import ABC, abstractmethod

"""
  ! Principio de Inversión de Dependencias (DIP)
  * Inversión de dependencias: los modulos de alto y bajo nivel, deben depender de las abstracciones, con clases base o interfaces
  * Módulos de alto y bajo nivel:
    - Módulo de alto nivel: aquellos que contienen lógica de negocio o aplicaciones especificas
    - Módulo de bajo nivel: detalles de implementación, como servicios externos o clases
  * Desacoplamiento: cada modulo se vuelve independientes entre si, la modificacion de cada uno no debe afectar a los modulos de alto nivel
  * Reutilizacion de codigo: los modulos de bajo nivel, al depender de abstracciones, se pueden reutilizar en diferentes contextos y aplicaciones
  * Testeabilidad: al separar las dependencias, realizar pruebas unitarias y de integración
"""

# Incorrecto
class EmailNotificador():
  def enviar_email(self, mensaje):
    print(f"\"{mensaje}\"")
    print("Enviando email...")

# Tenemos una clase superior que esta fuertemente ligada a la clase EmailNotificador
class ServicioNotficador():
  def __init__(self) -> None:
    self.email_notificador = EmailNotificador()

  def notificar(self, mensaje):
    print("Notficando de servicio")
    self.email_notificador.enviar_email("SE COMPLETO EL REGISTRO")

# Correcto
# Toda clase depende de la interfaz y sus contratos, permitiendo cumplir con los otros principios
class Notifier(ABC):
  @abstractmethod
  def send(self, message_send:str) -> str:
    pass

class IEmailNotifier(Notifier):
  def send(self, message_send:str):
    print(f"Utilizando servicio de la nube...\nConectando con cliente...\n\"{message_send}\"")
    return "Email enviado"

class ISMSNotifier(Notifier):
  def send(self, message_send:str):
    print(f"\"{message_send}\"\nEnviando mensaje...")
    return "Mensaje enviado"

class IFaxNotifier(Notifier):
  def send(self, message_send:str):
    print(f"\"{message_send}\"\nEnviando fax...")
    return "Fax enviado"

# La clase solo depende de la interfaz, las clases que le pasen deben ser de esta misma interfaz, asegurandose que cumplan con el mismo metodo
class NotificationService:
  def __init__(self, type: Notifier) -> None:
    self.type_notification = type

  def notify(self, message_send:str):
    print("Notificando al cliente...")
    print(self.type_notification.send(message_send))

notify_service = NotificationService(IFaxNotifier())
notify_service.notify("SE REGISTRO CORRECTAMENTE EL USUARIO")


corporation_notify = NotificationService(ISMSNotifier())
corporation_notify.notify("REUNION EN LA CON EL CORPORATIVO MANANA")
