"""Definición del blueprint para componentes definidos con jinja y tailwind.

Note:
    El blueprint se define dentro de una función para inyectar las dependencias
    del controlador.

"""

from flask import Blueprint, Response
from flask import current_app as app

from src.controlador.componentes import ComponentesControlador


def crear_componentes_blueprint(
    controlador: ComponentesControlador,
) -> Blueprint:
    """Crea y configura el blueprint de archivo.

    Mapea todos los endpoints hacia el controlador

    Args:
        controlador (ComponentesControlador): Instancia del controlador para
        atender las peticiones.

    Returns:
        Blueprint: el blueprint configurado con todos los endpoints

    """
    componentes_bp = Blueprint(
        "componentes",
        __name__,
        url_prefix="/componentes",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "componentes",
    )

    @componentes_bp.route("/")
    def playground() -> str:
        """Muestra la página demo de todos los componentes."""
        return controlador.renderizar_playground()

    @componentes_bp.get("/input/color")
    def color_actualiza_texto() -> str | Response:
        """Hace dinámico el componente de input color.

        Sincroniza el <input type="color"> y el <input type="text"> del
        componente de input de color para formularios
        """
        return controlador.renderizar_input_color()

    @componentes_bp.get("/wizard/evento/siguiente/<int:paso_actual>")
    def wizard_evento_siguiente(paso_actual: int) -> str:
        """Hace dinámico el botón de siguiente del wizard de evento."""
        return controlador.renderizar_siguiente_formulario_evento(paso_actual)

    @componentes_bp.get("/wizard/evento/anterior/<int:paso_actual>")
    def wizard_evento_anterior(paso_actual: int) -> str:
        """Hace dinámico el botón de anterior del wizard de evento."""
        return controlador.renderizar_anterior_formulario_evento(paso_actual)

    @componentes_bp.route("/wizard/evento")
    def renderizar_wizard_evento() -> str:
        """Renderiza el wizard de crear evento."""
        return controlador.renderizar_wizard_evento_template()

    return componentes_bp
