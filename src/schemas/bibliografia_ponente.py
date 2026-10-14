"""Modelo para representar la biografía de un ponente.

Note:
    Este modelo define la estructura de la tabla `biografia_ponente` en la
    base de datos, incluyendo sus columnas y relaciones con otros modelos.

"""

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoInstitucion
from src.inicializacion.extenciones import db


class BiografiaPonente(db.Model):
    """Modelo que representa la biografía de un ponente.

    Cada biografía está asociada a una persona académica y a un evento
    de ponente. Almacena información como la semblanza, intereses,
    institución de procedencia, tipo de institución y la ruta de la
    fotografía del ponente.

    Attributes:
        id_biografia_ponente (int): Identificador único de la biografía,
            clave primaria.
        id_persona_academica (int): Clave foránea que referencia a la
            persona académica asociada.
        id_evento_ponente (int): Clave foránea que referencia al evento
            de ponente asociado.
        semblanza (str): Texto con la semblanza del ponente.
        intereses (str): Intereses del ponente.
        institucion_procedencia (str): Institución de procedencia del
            ponente.
        tipo_institucion (str): Tipo de institución de procedencia.
        ruta_foto (str): Ruta del archivo de la fotografía del ponente.
        persona_academica (PersonaAcademica): Persona académica asociada
            a la biografía.
        evento_ponente (EventoPonente): Evento de ponente asociado a la
            biografía.

    """

    __tablename__ = "biografia_ponente"

    id_biografia_ponente: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica",ondelete="CASCADE")
    )
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    semblanza: Mapped[str | None] = mapped_column(String(1700), nullable=True)
    intereses: Mapped[str | None] = mapped_column(String(250), nullable=True)
    institucion_procedencia: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )
    tipo_institucion: Mapped[TipoInstitucion | None]
    ruta_foto: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="biografias_ponente",
    )
    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="biografias_ponente",
    )
