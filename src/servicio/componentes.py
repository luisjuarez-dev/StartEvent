"""Servicio para las peticiones relacionadas con componentes.

Muchos componentes requieren de comportamientos dinámicos mediante peticiones
HTMX, este módulo atiende estas peticiones e implementa dicho funcionamiento
"""
class ComponentesServicio:
    """Implementación del servicio para el funcionamiento de componentes."""

    def cambiar_siguiente_formulario_evento(self, paso_actual: int) -> str:
        """T."""
        return str(paso_actual + 1)

    def cambiar_anterior_formulario_evento(self, paso_actual: int) -> str:
        """T."""
        return str(paso_actual - 1)
