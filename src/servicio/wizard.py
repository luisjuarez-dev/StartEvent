"""Servicio para las peticiones relacionadas con componentes.

Muchos componentes requieren de comportamientos dinámicos mediante peticiones
HTMX, este módulo atiende estas peticiones e implementa dicho funcionamiento
"""

from src.interfaces.servicio import WizardServicioI

WIZARDS = {
    "evento": {
        "formularios": [
            "organizacion_evento/eventos/form_calendario.hmtl",
            "organizacion_evento/eventos/form_convocatorias.hmtl",
            "organizacion_evento/eventos/form_promocionales.hmtl",
            "organizacion_evento/eventos/form_comite.hmtl",
        ],
        "pasos": [
            "Calendario",
            "Convocatorias",
            "Imagenes Promocionales",
            "Comité Organizador",
        ],
    }
}


class WizardServicio(WizardServicioI):
    """Implementación del servicio para el funcionamiento de componentes."""

    def siguiente(self, wizard: str, paso_actual: int) -> str:  # noqa: D102
        return WIZARDS[wizard]["formularios"][paso_actual]

    def anterior(self, wizard: str, paso_actual: int) -> str:  # noqa: D102
        return WIZARDS[wizard]["formularios"][paso_actual - 2]
