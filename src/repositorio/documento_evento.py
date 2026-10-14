"""Implementación del repositorio para documentos de eventos académicos."""

from sqlalchemy import select

from src.enums import SubtipoDocumento, TipoDocumento
from src.inicializacion.extenciones import db
from src.interfaces.repositorio import DocumentoEventoRepositorioI
from src.modelo.documento_evento import DocumentoEvento


class DocumentoEventoRepositorio(DocumentoEventoRepositorioI):
    """Accede a la información de DocumentoEvento en la base de datos."""

    def select_by_edicion_y_subtipo(
        self,
        id_evento_academico: int,
        tipo: TipoDocumento,
        subtipo: SubtipoDocumento,
    ) -> list[DocumentoEvento]:
        """Busca documentos por evento, tipo y subtipo.

        Args:
            id_evento_academico (int): El identificador del evento académico
            tipo (TipoDocumento): El tipo del documento a buscar
            subtipo (SubtipoDocumento): El subtipo del documento a buscar

        Returns:
            list[DocumentoEvento]: Una lista de todos los documentos que
            cumplen las condiciones

        """
        stmt = select(DocumentoEvento).where(
            DocumentoEvento.id_evento_academico == id_evento_academico
            and DocumentoEvento.tipo_documento == tipo
            and DocumentoEvento.subtipo_documento == subtipo
        )
        return list(db.session.scalars(stmt).all())