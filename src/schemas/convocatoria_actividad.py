"""Modelo para representar convocatorias asociadas a actividades.

Note:
    Este modelo define la estructura de la tabla `convocatoria_actividad`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date, time

from sqlalchemy import Date, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class ConvocatoriaActividad(db.Model):
    """Modelo que representa una convocatoria asociada a una actividad.

    Cada actividad puede tener una única convocatoria, y cada convocatoria
    puede estar asociada a una única actividad.
    La relación es de uno a uno (``Actividad``→``ConvocatoriaActividad``)
    con borrado en cascada: al eliminar
    una actividad, su convocatoria se elimina automáticamente.

    Attributes:
        id_convocatoria_actividad (int): Clave primaria.
        id_actividad (int): Clave foránea que referencia a
            la actividad a la que pertenece.
        fecha_expiracion (date): Fecha de expiración de la convocatoria.
        hora_expiracion (time): Hora de expiración de la convocatoria.

    """

    __tablename__ = "convocatoria_actividad"

    id_convocatoria_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE"), unique=True
    )
    fecha_expiracion: Mapped[date] = mapped_column(Date)
    hora_expiracion: Mapped[time] = mapped_column(Time)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="convocatorias_actividad"
    )
