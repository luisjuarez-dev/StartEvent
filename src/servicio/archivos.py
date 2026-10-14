"""Proporciona acceso a archivos locales del sistema de archivos."""

from flask import Response, send_from_directory
from flask import current_app as app


class ArchivoServicio:
    """Implementación del servicio para la entrega de archivos locales."""

    def otorgar_documento(self, filename: str) -> Response:
        """Envía un documento guardado en el directorio de Documentos."""
        return send_from_directory(
            app.config["DIRECTORIO_DOCUMENTOS"], filename
        )