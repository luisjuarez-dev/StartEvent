"""Controlador de StartEvent para las peticiones de StartEvent.

Maneja las peticiones relacionadas con la autenticación de usuarios, incluyendo
la renderización de la página de login y la renovación automática de tokens JWT
cuando están próximos a expirar.
"""

from flask import Response, render_template
from flask_jwt_extended import current_user, get_jwt, set_access_cookies

from src.dto.autenticacion import RefrescarTokenDto
from src.servicio.startevent import StarteventServicio


class StarteventControlador:
    """Controlador para el blueprint de StartEvent.

    Proporciona funcionalidades para renderizar la página de login y refrescar
    tokens de acceso cuando están próximos a expirar.
    """

    def __init__(self, servicio: StarteventServicio) -> None:
        """Inicializa el controlador con el servicio de StartEvent.

        Args:
            servicio (StarteventServicio): instancia del servicio de
            autenticación.

        """
        self._servicio = servicio

    def _esta_por_expirar(self, jwt: dict) -> bool:
        """Verifica si el token JWT está próximo a expirar.

        Args:
            jwt (dict): diccionario del token JWT con información de
            expiración.

        Returns:
            bool: True si el token está próximo a expirar segun las reglas de
            configuración de Flask, False en caso contrario.

        """
        return self._servicio.esta_por_expirar(jwt["exp"])

    def renderizar_login(self) -> str:
        """Renderiza la página de login para StartEvent.

        Returns:
            str: HTML de la página de login.

        """
        return render_template("login.html")

    def refrescar_tokens_por_expirar(self, response: Response) -> Response:
        """Refresca los tokens JWT de acceso si están próximos a expirar.

        Verifica si el token de acceso actual está próximo a expirar y de ser
        así genera un nuevo token estableciendolo en las cookies de la
        respuesta.

        Args:
            response (Response): objeto Response de Flask a modificar.

        Returns:
            Response: objeto Response con las cookies actualizadas si fue el
            caso.

        """
        try:
            token_acceso = get_jwt()
            if token_acceso and self._esta_por_expirar(token_acceso):
                dto = RefrescarTokenDto(identidad=current_user)
                dto_salida = self._servicio.refrescar_token(dto)
                set_access_cookies(response, dto_salida.token)
        except RuntimeError:
            return response
        else:
            return response
