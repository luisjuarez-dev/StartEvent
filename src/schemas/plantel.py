"""Modelo para representar el plantel de una institución académica.

Note:
    Este modelo define la estructura de la tabla `plantel` en la base de datos,
    incluyendo sus columnas y relaciones con otros modelos.

"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Plantel(db.Model):
    """Modelo que representa un plantel académico.

    Cada plantel puede tener múltiples documentos, comités,
    actividades compartidas, autoridades, espacios, agendas
    y fechas asociadas. Si se elimina un plantel, todos
    los registros relacionados se eliminan automáticamente
    debido a la configuración de borrado en cascada.

    Attributes:
        abreviatura (str): Abreviatura del plantel, clave primaria.
            nombre (str): Nombre completo del plantel.
        correo_contacto (str): Correo electrónico de contacto del plantel.
        direccion (str): Dirección física del plantel
        documentos_evento (list[DocumentoEvento]): Documentos asociados
            al plantel.
        comites_evento (list[ComiteEvento]): Comités asociados al plantel.
        actividades_compartidas (list[ActividadCompartida]):
            Actividades compartidas asociadas al plantel.
        autoridades (list[Autoridad]): Autoridades asociadas al plantel.
        espacios (list[Espacio]): Espacios asociados al plantel.
        agendas (list[Agenda]): Agendas asociadas al plantel.
        fechas_plantel (list[FechaPlantel]): Fechas asociadas al plantel.
        requisiciones (list[Requisicion]): Requisiciones asociadas al plantel.

    """

    __tablename__ = "plantel"

    abreviatura: Mapped[str] = mapped_column(String(5), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    correo_contacto: Mapped[str] = mapped_column(String(255))
    direccion: Mapped[str] = mapped_column(String(150))

    # Relaciones
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    comites_evento: Mapped[list["ComiteEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    actividades_compartidas: Mapped[list["ActividadCompartida"]] = (  # pyright: ignore[reportUndefinedVariable]
        relationship(
            back_populates="plantel_destinatario",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    autoridades: Mapped[list["Autoridad"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    espacios: Mapped[list["Espacio"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    agendas: Mapped[list["Agenda"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    fechas_plantel: Mapped[list["FechaPlantel"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    requisiciones: Mapped[list["Requisicion"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
