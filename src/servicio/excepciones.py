"""Excepciones del sistema para la capa de Servicio."""

from src.enums import TipoWizard


class IndiceWizardError(Exception):
    """Excepción para cuando un wizard quiere acceder a un paso inválido."""

    def __init__(
        self, wizard: TipoWizard, paso: int, paso_maximo: int
    ) -> None:
        """Crea un objeto de la clase IndiceWizardError."""
        super().__init__(
            f"Número de paso inválido. Se recibió: {paso}, para el wizard"
            f"{wizard.value} se esperaba un número en el intervalo [1, "
            f"{paso_maximo}]"
        )
