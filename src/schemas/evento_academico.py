"""Modelo para representar eventos académicos.

Note:
    Este modelo define la estructura de la tabla `evento_academico`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class EventoAcademico(db.Model):
    """Modelo que representa un evento académico.

    Cada evento académico puede tener múltiples temas,
    documentos, comités, actividades, requisiciones, colores
    y fechas de plantel asociados. La relacion es de uno a muchos
    (``EventoAcademico`` → ``TemaEvento``,
    ``DocumentoEvento``, ``ComiteEvento``, ``Actividad``, ``Requisicion``,
    ``ColorEvento``, ``FechaPlantel``) con borrado en cascada:
    al eliminar un evento, sus elementos asociados se eliminan automáticamente.

    Attributes:
        id_evento_academico (int): Clave primaria.
        nombre (str): Nombre del evento (máx. 200 caracteres).
        edicion (int): Número de edición del evento.
        tematica (str | None): Temática del evento
            (máx. 200 caracteres,opcional).
        presentacion (str | None): Presentación o descripción
            del evento (máx. 1000 caracteres, opcional).
        temas_evento (list[TemaEvento]): Lista de temas asociados al evento.
        documentos_evento (list[DocumentoEvento]): Lista de
            documentos asociados al evento.
        comites_evento (list[ComiteEvento]): Lista de comités
            asociados al evento.
        actividades (list[Actividad]): Lista de actividades asociadas
            al evento.
        requisiciones (list[Requisicion]): Lista de requisiciones
            asociadas al evento.
        colores_evento (list[ColorEvento]): Lista de colores
            asociados al evento.
        fechas_plantel (list[FechaPlantel]): Lista de fechas
            de plantel asociadas al evento.

    """

    __tablename__ = "evento_academico"

    id_evento_academico: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    edicion: Mapped[int] = mapped_column(SmallInteger)
    tematica: Mapped[str | None] = mapped_column(String(200), nullable=True)
    presentacion: Mapped[str | None] = mapped_column(
        String(1000), nullable=True
    )

    # Relaciones
    temas_evento: Mapped[list["TemaEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    comites_evento: Mapped[list["ComiteEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    actividades: Mapped[list["Actividad"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    requisiciones: Mapped[list["Requisicion"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    colores_evento: Mapped[list["ColorEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    fechas_plantel: Mapped[list["FechaPlantel"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    biografias_ponente:  Mapped[list["BiografiaPonente"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="evento_academico",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
