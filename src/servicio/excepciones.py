"""Excepciones del sistema para la capa de Servicio."""


class IndiceWizardError(Exception):
    """Excepción para cuando un wizard quiere acceder a un paso inválido."""

    def __init__(self, wizard: str, paso: int, paso_maximo: int) -> None:
        """Crea un objeto de la clase IndiceWizardError."""
        super().__init__(
            f"Número de paso inválido. Se recibió: {paso}, para el wizard"
            f"{wizard} se esperaba un número en el intervalo [1, "
            f"{paso_maximo}]"
        )
