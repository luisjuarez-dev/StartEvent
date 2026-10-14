"""Definición del blueprint para peticiones sobre StartEvent.

Note:
    El blueprint se define dentro de una función para inyectar las dependencias
    del controlador.

"""

from flask import Blueprint, Response
from flask import current_app as app

from src.controlador.startevent import StarteventControlador


def crear_startevent_blueprint(
    controlador: StarteventControlador,
) -> Blueprint:
    """Crea y configura el blueprint de StartEvent.

    Mapea todos los endpoints hacia el controlador y comandos de flask

    Args:
        controlador (StarteventControlador): Instancia del controlador para
        atender las peticiones.

    Returns:
        Blueprint: el blueprint configurado con todos los endpoints

    """
    startevent_bp = Blueprint(
        "startevent",
        __name__,
        url_prefix="/startevent",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "startevent",
    )

    @startevent_bp.route("/")
    def login() -> str:
        """Muestra la página de Login para StartEvent.

        Returns:
            str: El HTML de la página de Login.

        """
        return controlador.renderizar_login()

    @startevent_bp.after_request
    def refresh(response: Response) -> Response:
        """Refresca las cookies de acceso de JWT si estan por expirar.

        Este método se ejecuta tras todos los endpoint del blueprint de
        StartEvent

        Args:
            response (Response): El objeto Response que iba a ser enviado al
            cliente.

        Returns:
            Response: La respuesta con las cookies refrescadas si es el caso,
            la misma respuesta sin modificar si no.

        """
        return controlador.refrescar_tokens_por_expirar(response)

    return startevent_bp
