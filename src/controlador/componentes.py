"""Controlador para peticiones sobre los componentes de jinja y tailwind."""

from flask import (
    Response,
    get_template_attribute,
    make_response,
    render_template,
    request,
    url_for,
)

from src.interfaces.servicio import WizardServicioI


class ComponentesControlador:
    """Controlador para el blueprint de componentes.

    Atiende peticiones relacionadas al funcionamiento dinámico de los
    componentes
    """

    def __init__(self, servicio_wizard: WizardServicioI) -> None:
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

    def renderizar_wizard_evento(self, paso: int) -> str:
        """Renderiza el wizard para crear evento en un paso concreto.

        Actualiza los botones para navegar entre pasos y el indicador del
        progreso total del wizard

        Args:
            paso (int): El paso del wizard que se va a renderizar

        Returns:
            str: El html de todos los componentes del wizard

        """
        wizard = "evento"
        n_pasos = self._servicio_wizard.get_total_pasos(wizard)
        form_template = self._servicio_wizard.get_form(wizard, paso)
        macro_progreso = get_template_attribute(
            "componentes/wizards.html", "progreso"
        )
        macro_navegacion = get_template_attribute(
            "componentes/wizards.html", "navegacion"
        )
        macro_form = get_template_attribute("componentes/wizards.html", "form")

        html_progreso = macro_progreso(
            num_pasos=n_pasos,
            paso_actual=paso,
            labels_pasos=self._servicio_wizard.get_pasos(wizard),
        )
        html_navegacion = macro_navegacion(
            num_pasos=n_pasos,
            paso_actual=paso,
            url_siguiente=url_for(
                "componentes.wizard_evento_siguiente",
                paso_actual=paso,
            ),
            url_anterior=url_for(
                "componentes.wizard_evento_anterior",
                paso_actual=paso,
            ),
        )
        html_form = macro_form(template=form_template)
        return html_progreso + html_form + html_navegacion

    def renderizar_wizard_evento_template(self) -> str:
        """Renderiza la template del wizard de evento."""
        return render_template(
            "wizard_evento.html",
            total_pasos=self._servicio_wizard.get_total_pasos(wizard="evento"),
            nombres_pasos=self._servicio_wizard.get_pasos(wizard="evento"),
            primer_formulario=self._servicio_wizard.get_form(
                wizard="evento", paso_actual=1
            ),
        )

    def renderizar_siguiente_formulario_evento(self, paso_actual: int) -> str:
        """Renderiza el siguiente formulario del wizard de evento."""
        return self.renderizar_wizard_evento(paso_actual + 1)

    def renderizar_anterior_formulario_evento(self, paso_actual: int) -> str:
        """Renderiza el anterior formulario del wizard de evento."""
        return self.renderizar_wizard_evento(paso_actual - 1)
