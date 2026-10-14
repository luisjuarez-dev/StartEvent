"""Modelo que representa la asistencia a una actividad académica.

Note:
    Este modelo define la estructura de la tabla `asistencia`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Asistencia(db.Model):
    """Modelo que representa la asistencia a una actividad.

    Cada actividad puede tener múltiples asistencias, y cada asistencia
    pertenece a una única persona académica. La relación es de uno a muchos
    (``PersonaAcademica`` → ``Asistencia``) con borrado en cascada: al eliminar
    una persona académica, sus asistencias se eliminan automáticamente.

    Attributes:
        id_asistencia (int): Clave primaria.
        id_actividad (int): FK a la actividad.
        id_persona_academica (int): FK a la persona académica.
        fecha (date): Fecha de la asistencia.
        actividad (Actividad): Actividad a la que se asistió.
        persona_academica (PersonaAcademica): Persona académica que asistió.

    """

    __tablename__ = "asistencia"

    id_asistencia: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE")
    )
    id_persona_academica: Mapped[int | None] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="SET NULL"
        ),
        nullable=True,
    )
    fecha: Mapped[date | None] = mapped_column(Date, nullable=True)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(back_populates="asistencias")
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="asistencias"
    )
