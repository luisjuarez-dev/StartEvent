"""Data Transfer Objects para información de personas académicas.

Contiene las clases DTO utilizadas para transferir información sobre personas
académicas entre capas de la aplicación
"""

from dataclasses import dataclass


@dataclass
class MostrarInformacionUsuarioDto:
    """DTO que contiene la información básica del usuario.

    Attributes:
        nombre_completo (str): nombre completo del usuario.
        ruta_foto_perfil (str): ruta del archivo de foto de perfil del usuario.
        roles (list[str]): lista de roles o permisos asignados al usuario.
        es_administrador (bool): indicador de si el usuario tiene permisos
        administrativos.

    """

    nombre_completo: str
    ruta_foto_perfil: str
    roles: list[str]
    es_administrador: bool
