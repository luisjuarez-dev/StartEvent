"""Controlador de eventos para gestión de eventos académicos.

Maneja las peticiones relacionadas con eventos académicos y usuarios logeados.
"""

from flask import render_template
from flask_jwt_extended import current_user

from src.dto.evento import BuscarEventosUsuarioDto, MostrarEventoDto
from src.dto.persona_academica import MostrarInformacionUsuarioDto
from src.servicio.evento import EventosServicio


class EventosControlador:
    """Controlador para el blueprint de eventos.

    Atiende peticiones relacionadas a eventos académicos
    """

    def __init__(self, servicio: EventosServicio) -> None:
        """Inicializa el controlador con el servicio de eventos.

        Args:
            servicio (EventosServicio): instancia del servicio de eventos.

        """
        self._servicio = servicio

    def _buscar_todos_eventos(self) -> list[MostrarEventoDto]:
        """Busca todos los eventos en los que el usuario ha participado.

        Returns:
            list[MostrarEventoDto]: lista de DTOs con información básica de
            eventos.

        """
        dto = BuscarEventosUsuarioDto(
            id_usuario=current_user.id_persona_academica
        )
        return self._servicio.buscar_eventos(dto)

    def rederizar_eventos(self) -> str:
        """Renderiza la página de visualización de eventos del usuario.

        Returns:
            str: HTML de la página de eventos.

        """
        eventos = self._buscar_todos_eventos()
        usuario = MostrarInformacionUsuarioDto(
            nombre_completo=current_user.nombres,
            es_administrador=current_user.es_administrador,
            ruta_foto_perfil=current_user.ruta_foto_perfil,
            roles=[],
        )
        return render_template(
            "eventos.html", lista_eventos=eventos, usuario=usuario
        )

    def renderizar_modal_evento(self) -> str:
        """Renderiza un modal de evento con contenido de prueba.

        Returns:
            str: HTML del modal de evento.

        """
        modal = "Probando ventana modal"
        return render_template("modal.html", modal=modal)

    def renderizar_modal_vacia(self) -> str:
        """Renderiza un div vació donde iba la modal para cerrarla.

        Returns:
            str: HTML de un div vacío con estilos de modal.

        """
        return '<div id="div-modal" class="absolute left-0 top-0 z-20"></div>'
