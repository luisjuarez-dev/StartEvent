"""Data Transfer Objects para eventos académicos.

Contiene las clases DTO utilizadas para transferir información sobre
eventos académicos entre capas de la aplicación
"""

from dataclasses import dataclass


@dataclass
class MostrarEventoDto:
    """DTO para mostrar la información de evento académico.

    Attributes:
        nombre (str): nombre del evento.
        edicion (int): número de edición del evento.
        ruta_logotipo (str): ruta del archivo del logotipo del evento.

    """

    nombre: str
    edicion: int
    ruta_logotipo: str


@dataclass
class BuscarEventosUsuarioDto:
    """DTO para la búsqueda de eventos de un usuario.

    Attributes:
        id_usuario (int): identificador único del usuario.

    """

    id_usuario: int
