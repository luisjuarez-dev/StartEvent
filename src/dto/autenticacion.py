"""Data Transfer Objects para el bluprint de autenticación.

Contiene las clases DTO utilizadas para transferir información de autenticación
entre capas de la aplicación
"""

from dataclasses import dataclass


@dataclass
class IniciarSesionDto:
    """DTO para solicitud de inicio de sesión.

    Attributes:
        correo (str): correo electrónico del usuario.
        contrasenia (str): contraseña del usuario.
        pimienta (str): clave de encriptación adicional para hash de contraseña

    """

    correo: str
    contrasenia: str
    pimienta: str


@dataclass
class ValiadarCredencialesDto:
    """DTO para respuesta de validación de credenciales.

    Attributes:
        token_acceso (str | None): token JWT de acceso si las credenciales son
        válidas, None si no.
        token_refrescar (str | None): token JWT para refrescar si es válido,
        None si no.
        codigo (int): código de estado HTTP de la validación.
        mensaje (str): mensaje descriptivo del resultado de la validación.

    """

    token_acceso: str | None
    token_refrescar: str | None
    codigo: int
    mensaje: str


@dataclass
class RefrescarTokenDto:
    """DTO para solicitud de refrescar un token.

    Attributes:
        identidad (str): identidad del usuario con la cual refrescar el token.

    """

    identidad: str


@dataclass
class OtorgarNuevoTokenDto:
    """DTO para respuesta con nuevo token de acceso.

    Attributes:
        token (str): nuevo token JWT de acceso generado.

    """

    token: str
