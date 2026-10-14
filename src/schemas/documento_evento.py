"""Modelo para representar documentos asociados.

Note:
    Este modelo define la estructura de la tabla `documento_evento`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date, time

from sqlalchemy import Date, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import SubtipoDocumento, TipoDocumento
from src.inicializacion.extenciones import db


class DocumentoEvento(db.Model):
    """Modelo que representa un documento asociado a un evento académico.

    Cada evento académico puede tener múltiples documentos asociados,
    y cada documento puede estar asociado a un único evento académico.
    La relación es de uno a muchos (``EventoAcademico``→
    ``DocumentoEvento``) con borrado en cascada: al eliminar
    un evento, sus documentos se eliminan automáticamente.

    Attributes:
        id_documento_evento (int): Clave primaria.
        id_evento_academico (int): Clave foránea que referencia
            al evento académico al que pertenece.
        id_plantel (str | None): Clave foránea que referencia al
            plantel al que pertenece.
        id_persona_academica (int | None): Clave foránea que referencia
            a la persona académica al que pertenece.
        id_actividad (int | None): Clave foránea que referencia a
            la actividad a la que pertenece.
        fecha_expiracion (date | None): Fecha de expiración del documento.
        hora_expiracion (time | None): Hora de expiración del documento.
        tipo_documento (TipoDocumento): Tipo de documento.
        subtipo_documento (SubtipoDocumento): Subtipo de documento.
        ruta_archivo (str): Ruta del archivo del documento.

    """

    __tablename__ = "documento_evento"

    id_documento_evento: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    id_plantel: Mapped[str | None] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE"), nullable=True
    )
    id_persona_academica: Mapped[int | None] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        ),
        nullable=True,
    )
    id_actividad: Mapped[int | None] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE"), nullable=True
    )
    fecha_expiracion: Mapped[date | None] = mapped_column(Date, nullable=True)
    hora_expiracion: Mapped[time | None] = mapped_column(Time, nullable=True)
    tipo_documento: Mapped[TipoDocumento]
    subtipo_documento: Mapped[SubtipoDocumento]
    ruta_archivo: Mapped[str] = mapped_column(String(200))

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="documentos_evento"
    )
    plantel: Mapped["Plantel"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="documentos_evento"
    )
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="documentos_evento"
    )
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="documentos_evento"
    )
