"""Definición del blueprint para peticiones sobre actividades.

Note:
    El blueprint se define dentro de una función para inyectar las dependencias
    del controlador.

"""

from flask import Blueprint
from flask import current_app as app

from src.controlador.actividad import ActividadControlador


def crear_actividad_blueprint(controlador: ActividadControlador) -> Blueprint:
    """Crea y configura el blueprint de actividades.

    Mapea todos los endpoints hacia el controlador

    Args:
        controlador (ActividadesControlador): Instancia del controlador para
        atender las peticiones.

    Returns:
        Blueprint: el blueprint configurado con todos los endpoints

    """
    actividad_bp = Blueprint(
        "actividades",
        __name__,
        url_prefix="/actividades",
        template_folder=app.config["DIRECTORIO_TEMPLATES"]
        / "startevent"
        / "organizacion_evento"
        / "actividades",
    )

    @actividad_bp.route("/")
    def renderizar_buzon_ponencias() -> str:
        """Muestra el buzón de ponencias de la convocatoria del plantel.

        Returns:
            str: La vista HTML del buzón de ponencias

        """
        return controlador.renderizar_buzon_ponencias()

    return actividad_bp
