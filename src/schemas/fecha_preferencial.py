"""Modelo para representar fechas preferenciales.

Note:
    Este modelo define la estructura de la tabla `fecha_preferencial`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class FechaPreferencial(db.Model):
    """Modelo que representa una fecha preferencial asociada a una actividad.

    Cada actividad puede tener múltiples fechas preferenciales, y cada fecha
    preferencial pertenece a una única actividad. La relación es de uno a
    muchos(``Actividad`` → ``FechaPreferencial``) con borrado en cascada:
    al eliminar una actividad, sus fechas preferenciales se
    eliminan automáticamente.

    Attributes:
        id_fecha_preferencial (int): Clave primaria.
        id_actividad (int): FK a la actividad académica.
        fecha (date): Fecha preferencial.
        actividad (Actividad): Actividad propietaria.

    """

    __tablename__ = "fecha_preferencial"

    id_fecha_preferencial: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE")
    )
    fecha: Mapped[date] = mapped_column(Date)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="fechas_preferenciales"
    )
