"""Interfaces de servicio para la capa de servicio."""

from abc import ABC, abstractmethod

from src.enums import TipoWizard


class WizardServicioI(ABC):
    """Interfaz de servicio para atender las peticiones sobre wizards."""

    @abstractmethod
    def get_form(self, wizard: TipoWizard, paso_actual: int) -> str:
        """Obtiene el template del paso del wizard correspondiente.

        Args:
            wizard: (TipoWizard): El nombre del wizard
            paso_actual (int): Paso actual del wizard (Comienza en 1)

        Returns:
            str: El nombre del archivo que contiene la template del formulario
            correspondiente al paso indicado del wizard

        """

    @abstractmethod
    def get_pasos(self, wizard: TipoWizard) -> list[str]:
        """Obtiene la lista de todos los pasos del wizard.

        Args:
            wizard (TipoWizard): El nombre del wizard

        Returns:
            list[str]: La lista de los subtitulos de los pasos del wizard

        """

    @abstractmethod
    def get_total_pasos(self, wizard: TipoWizard) -> int:
        """Obtiene el numero total de pasos del wizard.

        Args:
            wizard (TipoWizard): El nombre del wizard

        Returns:
            int: El numero de pasos del wizard

        """
