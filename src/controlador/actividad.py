"""Controlador de peticiones sobre actividades."""

from flask import render_template


class ActividadControlador:
    """Controlador para el blueprint de actividades."""

    def renderizar_buzon_ponencias(self) -> str:
        """Renderiza el buzón de ponencias de la convocatoria del plantel.

        Returns:
            str: HTML de la página del buzón de ponencias.

        """
        return render_template("buzon_ponencias.html")
