"""Interfaces de servicio para la capa de servicio."""

from abc import ABC, abstractmethod


class WizardServicioI(ABC):
    """Interfaz de servicio para atender las peticiones sobre wizards."""

    @abstractmethod
    def siguiente(self, wizard: str, paso_actual: int) -> str:
        """Determina cual es el siguiente paso del wizard.

        Args:
            wizard: (str): El nombre del wizard
            paso_actual (int): Paso actual del wizard (Comienza en 1)

        Returns:
            str: El nombre del archivo que contiene la template del formulario
            que sigue en el wizard

        """

    @abstractmethod
    def anterior(self, wizard: str, paso_actual: int) -> str:
        """Determina cual es el paso anterior del wizard.

        Args:
            wizard: (str): El nombre del wizard
            paso_actual (int): Paso actual del wizard (Comienza en 1)

        Returns:
            str: El nombre del archivo que contiene la template del formulario
            anterioir en el wizard

        """
