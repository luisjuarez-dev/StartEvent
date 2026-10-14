"""Definición del blueprint para peticiones sobre eventos.

Note:
    El blueprint se define dentro de una función para inyectar las dependencias
    del controlador.

"""

from flask import Blueprint
from flask import current_app as app
from flask_jwt_extended import jwt_required

from src.controlador.evento import EventosControlador


def crear_evento_blueprint(controlador: EventosControlador) -> Blueprint:
    """Crea y configura el blueprint de eventos.

    Mapea todos los endpoints hacia el controlador

    Args:
        controlador (EventosControlador): Instancia del controlador para
        atender las peticiones.

    Returns:
        Blueprint: el blueprint configurado con todos los endpoints

    """
    evento_academico_bp = Blueprint(
        "eventos",
        __name__,
        url_prefix="/eventos",
        template_folder=app.config["DIRECTORIO_TEMPLATES"]
        / "startevent"
        / "organizacion_evento"
        / "eventos",
    )

    @evento_academico_bp.route("/")
    @jwt_required()
    def mostrar_eventos_asociados() -> str:
        """Muestra los eventos asociados al usuario.

        Returns:
            str: La vista HTML de la lista de eventos

        """
        return controlador.rederizar_eventos()

    @evento_academico_bp.route("/modal")
    def mostrar_modal_evento() -> str:
        """Muestra una ventana modal de prueba.

        Returns:
            str: El HTML de la ventana modal.

        """
        return controlador.renderizar_modal_evento()

    @evento_academico_bp.route("/quitar_modal")
    def esconder_modal_evento() -> str:
        """Esconde la ventana modal de prueba.

        Returns:
            str: El HTML de la ventana modal escondida.

        """
        return controlador.renderizar_modal_vacia()

    return evento_academico_bp
