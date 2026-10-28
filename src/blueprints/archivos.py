"""Definición del blueprint para peticiones sobre archivos locales.

Note:
    El blueprint se define dentro de una función para inyectar las dependencias
    del controlador.

"""

from flask import Blueprint, Response
from flask import current_app as app

from src.controlador.archivos import ArchivosControlador


def crear_archivos_blueprint(controlador: ArchivosControlador) -> Blueprint:
    """Crea y configura el blueprint de archivo.

    Mapea todos los endpoints hacia el controlador

    Args:
        controlador (ArchivosControlador): Instancia del controlador para
        atender las peticiones.

    Returns:
        Blueprint: el blueprint configurado con todos los endpoints

    """
    archivos_bp = Blueprint(
        "archivo",
        __name__,
        url_prefix="/archivo",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "archivo",
    )

    @archivos_bp.route("/documento/<path:filename>")
    def documentos(filename: str) -> Response:
        """Regresa un documento del sistema de archivos local.

        Args:
            filename (str): Ubicación del archivo, incluyendo ya ruta desde la
            carpeta de Documentos

        Returns:
            Response: La respuesta HTTP de Flask conteniendo el archivo.

        """
        return controlador.otorgar_documento(filename)

    return archivos_bp
