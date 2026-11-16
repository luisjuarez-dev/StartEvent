"""Controlador para peticiones sobre los componentes de jinja y tailwind."""

from flask import (
    Response,
    get_template_attribute,
    make_response,
    render_template,
    request,
)

from src.servicio.wizard import WizardServicio


class ComponentesControlador:
    """Controlador para el blueprint de componentes.

    Atiende peticiones relacionadas al funcionamiento dinámico de los
    componentes
    """

    def __init__(self, servicio_wizard: WizardServicio) -> None:
        """Inicializa el controlador con el servicio de componentes.

        Args:
            servicio_wizard (ComponentesServicio): instancia del servicio de
            componentes.

        """
        self._servicio_wizard = servicio_wizard

    def renderizar_playground(self) -> str:
        """Regresa el HTML de la página demo para los componentes."""
        return render_template("playground.html")

    def renderizar_input_color(self) -> str | Response:
        """Renderiza un input tipo color.

        Returns:
            str: HTML de un input de color con el valor asignado.

        """
        nombre_input = request.headers.get("HX-Trigger-Name")
        if not nombre_input:
            # El código 204 hace que HTMX ignore la respuesta
            return make_response("", 204)
        input_color_macro = get_template_attribute(
            "componentes/form_inputs.html", "input_color"
        )
        valor = request.args.get(nombre_input)
        label = request.args.get("label")
        return input_color_macro(label=label, name=nombre_input, value=valor)

    def renderizar_siguiente_formulario_evento(self, paso_actual: int) -> str:
        """Renderiza el siguiente formulario del wizard de evento."""
        return self._servicio_wizard.siguiente("evento", paso_actual)

    def renderizar_anterior_formulario_evento(self, paso_actual: int) -> str:
        """Renderiza el anterior formulario del wizard de evento."""
        return self._servicio_wizard.anterior("evento", paso_actual)
