"""Servicio para las peticiones relacionadas con componentes.

Muchos componentes requieren de comportamientos dinámicos mediante peticiones
HTMX, este módulo atiende estas peticiones e implementa dicho funcionamiento
"""

from src.interfaces.servicio import WizardServicioI


class WizardServicio(WizardServicioI):
    """Implementación del servicio para el funcionamiento de los wizards."""

    _WIZARDS = {
        "evento": {
            "formularios": [
                "organizacion_evento/eventos/form_calendario.html",
                "organizacion_evento/eventos/form_convocatorias.html",
                "organizacion_evento/eventos/form_promocionales.html",
                "organizacion_evento/eventos/form_comite.html",
            ],
            "pasos": [
                "Calendario",
                "Convocatorias",
                "Imagenes Promocionales",
                "Comité Organizador",
            ],
        }
    }

    def get_form(self, wizard: str, paso_actual: int) -> str:  # noqa: D102
        return self._WIZARDS[wizard]["formularios"][paso_actual - 1]

    def get_total_pasos(self, wizard: str) -> int:  # noqa: D102
        return len(self._WIZARDS[wizard]["formularios"])

    def get_pasos(self, wizard: str) -> list[str]:  # noqa: D102
        return self._WIZARDS[wizard]["pasos"]
