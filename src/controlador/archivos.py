"""Controlador de archivos locales para Flask.

Maneja las peticiones relacionadas con la entrega de archivos que Flask
requiere
"""

from flask import Response
from src.servicio.archivos import ArchivoServicio


class ArchivosControlador:
    """Controlador para el Blueprint de archivo."""

    def __init__(self, servicio: ArchivoServicio) -> None:
        """Inicializa el controlador con el servicio de archivos.

        Args:
            servicio (ArchivoServicio): instancia del servicio de archivos.

        """
        self.servicio = servicio

    def otorgar_documento(self, filename: str) -> Response:
        """Otorga un documento pdf.

        Args:
            filename (str): nombre del archivo.

        Returns:
            Response: objeto Response que contiene el archivo del documento pdf

        """
        return self.servicio.otorgar_documento(filename)
