"""Data Transfer Objects para notificaciones a usuarios.

Contiene las clases DTO utilizadas para transferir información sobre
notificaciones entre capas de la aplicación
"""

from dataclasses import dataclass


@dataclass
class NotificacionDto:
    """DTO para mostrar la información de notificación.

    Attributes:
        titulo (str): título de la notificación.
        descripcion (str): mensaje detallado de la notificación.

    """

    titulo: str
    descripcion: str
