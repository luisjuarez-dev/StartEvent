"""Servicio para las peticiones relacionadas con componentes.

Muchos componentes requieren de comportamientos dinámicos mediante peticiones
HTMX, este módulo atiende estas peticiones e implementa dicho funcionamiento
"""

from src.enums import TipoWizard
from src.interfaces.servicio import WizardServicioI
from src.servicio.excepciones import IndiceWizardError


class WizardServicio(WizardServicioI):
    """Implementación del servicio para el funcionamiento de los wizards."""

    _WIZARDS = {
        TipoWizard.EVENTO: {
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
        },
    }

    def get_form(self, wizard: TipoWizard, paso_actual: int) -> str:  # noqa: D102
        total_pasos = self.get_total_pasos(wizard)
        if paso_actual < 1 or paso_actual > total_pasos:
            raise (
                IndiceWizardError(
                    wizard=wizard, paso=paso_actual, paso_maximo=total_pasos
                )
            )
        return self._WIZARDS[wizard]["formularios"][paso_actual - 1]

    def get_total_pasos(self, wizard: TipoWizard) -> int:  # noqa: D102
        return len(self._WIZARDS[wizard]["formularios"])

    def get_pasos(self, wizard: TipoWizard) -> list[str]:  # noqa: D102
        return self._WIZARDS[wizard]["pasos"]
