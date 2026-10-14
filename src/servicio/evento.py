"""Servicio para la gestión de eventos académicos."""
from src.dto.evento import BuscarEventosUsuarioDto, MostrarEventoDto
from src.enums import SubtipoDocumento, TipoDocumento
from src.interfaces.repositorio import (
    ComiteEventoRepositorioI,
    DocumentoEventoRepositorioI,
)


class EventosServicio:
    """Implementación del servicio para atender el controlador de eventos."""

    def __init__(
        self,
        repositorio_comite_evento: ComiteEventoRepositorioI,
        repositorio_documento_evento: DocumentoEventoRepositorioI,
    ) -> None:
        """Inicializa el servicio con los repositorios necesarios.

        Args:
            repositorio_comite_evento (ComiteEventoRepositorioI): Instancia del
                repositorio para ComiteEvento
            repositorio_documento_evento (DocumentoEventoREpositorioI):
                Instancia del repositorio para DocumentoEvento

        """
        self._repositorio_comite_evento = repositorio_comite_evento
        self._repositorio_documento_evento = repositorio_documento_evento

    def buscar_eventos(
        self, dto: BuscarEventosUsuarioDto
    ) -> list[MostrarEventoDto]:
        """Busca los eventos en los que participa un usuario.

        Args:
            dto (BuscarEventosUsuarioDto): DTO que contiene el id del usuario.

        Returns:
            list[MostrarEventoDto]: Lista de DTOs con la información básica de
            los eventos del usuario

        """
        lista_comites = self._repositorio_comite_evento.select_by_id_persona(
            dto.id_usuario
        )
        dtos = []
        for comite in lista_comites:
            documento_evento = (
                self._repositorio_documento_evento.select_by_edicion_y_subtipo(
                    comite.id_evento_academico,
                    TipoDocumento.DOCUMENTO_PROMOCIONAL,
                    SubtipoDocumento.LOGOTIPO,
                )
            )
            dto_salida = MostrarEventoDto(
                nombre=comite.evento_academico.nombre,
                edicion=comite.evento_academico.edicion,
                ruta_logotipo=documento_evento[0].ruta_archivo,
            )
            dtos.append(dto_salida)
        return dtos
