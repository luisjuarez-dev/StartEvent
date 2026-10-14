"""Controlador de autenticación para login y gestión de tokens JWT.

Maneja las peticiones de autenticación de usuarios, validando credenciales
y estableciendo cookies de sesión (tokens JWT) en la respuesta.
"""

from flask import current_app as app
from flask import make_response, render_template, url_for
from flask_jwt_extended import set_access_cookies, set_refresh_cookies

from src.dto.autenticacion import IniciarSesionDto
from src.dto.notificacion import NotificacionDto
from src.servicio.autenticacion import AutenticadorServicio


class AutenticacionControlador:
    """Controlador para el blueprint de autenticación.

    Proporciona funcionalidad para validar credenciales de inicio de sesión
    y establecer tokens JWT en las cookies de respuesta.
    """

    def __init__(self, servicio: AutenticadorServicio) -> None:
        """Inicializa el controlador con el servicio de autenticación.

        Args:
            servicio (AutenticadorServicio): instancia del servicio de
            autenticación.

        """
        self._servicio = servicio

    def iniciar_sesion(self, correo: str, contrasenia: str) -> str:
        """Inicia sesión con las credenciales proporcionadas.

        Valida el correo electrónico y contraseña del usuario, comparando la
        contraseña hasehada ingresada por el usuario con la almacenada en la
        base de datos. Si las credenciales son válidas, genera tokens JWT
        (acceso y refrescar) y los establece en las cookies de respuesta,
        redirigiendo al usuario a la página de inicio de StartEvent

        Si las credenciales son inválidas, retorna una notificación de error.

        Args:
            correo (str): correo electrónico del usuario.
            contrasenia (str): contraseña del usuario.

        Returns:
            Response: objeto Response con redirección y cookies de sesión si es
            exitoso, o página de notificación de error si falla.

        """
        dto = IniciarSesionDto(
            correo=correo,
            contrasenia=contrasenia,
            pimienta=app.config["PIMIENTA"],
        )
        dto_salida = self._servicio.validar_credenciales(dto)
        if dto_salida.token_acceso is not None:
            response = make_response()
            response.headers["Hx-Redirect"] = url_for(
                "startevent.eventos.mostrar_eventos_asociados"
            )
            set_access_cookies(response, dto_salida.token_acceso)
            set_refresh_cookies(response, dto_salida.token_refrescar)
            return response

        dto = NotificacionDto("Error", "Correo o contraseña inválidos")
        return render_template("notificacion.html", notificacion=dto)
