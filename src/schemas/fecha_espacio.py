"""Modelo para representar fechas asociadas a un espacio.

Note:
    Este modelo define la estructura de la tabla `fecha_espacio`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class FechaEspacio(db.Model):
    """Modelo que representa una fecha asociada a un espacio.

    Cada espacio puede tener múltiples fechas asociadas, y cada fecha
    asociada pertenece a un único espacio. La relación es de uno a
    muchos(``Espacio`` → ``FechaEspacio``) con borrado en cascada:
    al eliminar un espacio, sus fechas asociadas se
    eliminan automáticamente.

    Attributes:
        id_fecha_espacio (int): Clave primaria.
        id_espacio (int): FK al espacio.
        fecha (date): Fecha asociada.
        espacio (Espacio): Espacio propietario.

    """

    __tablename__ = "fecha_espacio"

    id_fecha_espacio: Mapped[int] = mapped_column(primary_key=True)
    id_espacio: Mapped[int] = mapped_column(
        ForeignKey("espacio.id_espacio", ondelete="CASCADE")
    )
    fecha: Mapped[date] = mapped_column(Date)

    # Relaciones
    espacio: Mapped["Espacio"] = relationship(back_populates="fechas_espacio")  # pyright: ignore[reportUndefinedVariable]
