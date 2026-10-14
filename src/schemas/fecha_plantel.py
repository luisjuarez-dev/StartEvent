"""Modelo para representar fechas asociadas a un plantel.

Note:
    Este modelo define la estructura de la tabla `fecha_plantel`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class FechaPlantel(db.Model):
    """Modelo que representa una fecha asociada a un plantel.

    Cada plantel puede tener múltiples fechas asociadas, y cada fecha
    asociada pertenece a un único plantel. La relación es de uno a
    muchos(``Plantel`` → ``FechaPlantel``) con borrado en cascada:
    al eliminar un plantel, sus fechas asociadas se
    eliminan automáticamente.

    Attributes:
        id_fecha_plantel (int): Clave primaria.
        id_plantel (str): FK al plantel.
        id_evento_academico (int): FK al evento académico.
        fecha (date): Fecha asociada.
        plantel (Plantel): Plantel propietario.
        evento_academico (EventoAcademico): Evento académico propietario.

    """

    __tablename__ = "fecha_plantel"

    id_fecha_plantel: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE")
    )
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    fecha: Mapped[date] = mapped_column(Date)

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="fechas_plantel")  # pyright: ignore[reportUndefinedVariable]

    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="fechas_plantel"
    )
