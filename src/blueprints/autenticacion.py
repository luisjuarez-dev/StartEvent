"""Definición del blueprint para peticiones sobre autenticación.

Note:
    El blueprint se define dentro de una función para inyectar las dependencias
    del controlador.

"""

from flask import Blueprint, request
from flask import current_app as app

from src.controlador.autenticacion import AutenticacionControlador


def crear_autenticacion_blueprint(
    controlador: AutenticacionControlador,
) -> Blueprint:
    """Crea y configura el blueprint de autenticación.

    Mapea todos los endpoints hacia el controlador

    Args:
        controlador (AutenticacionControlador): Instancia del controlador para
        atender las peticiones.

    Returns:
        Blueprint: el blueprint configurado con todos los endpoints

    """
    autenticacion_bp = Blueprint(
        "autenticacion",
        __name__,
        url_prefix="/autenticacion",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "startevent",
    )

    @autenticacion_bp.post("/login")
    def iniciar_sesion() -> str:
        """Autentica a un usuario validando las credenciales en un login.

        Returns:
            Response: La respuesta HTTP que valida las credenciales y redirige
            a otro endpoint o una notificación de error.

        """
        correo: str = request.form["correo"]
        password: str = request.form["password"]
        return controlador.iniciar_sesion(correo, password)

    return autenticacion_bp
