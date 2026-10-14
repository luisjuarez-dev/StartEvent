"""Modelo para representar palabras clave asociadas a actividades académicas.

Note:
    Este modelo define la estructura de la tabla `palabra_clave_actividad`
    en la base de datos, incluyendo sus columnas y relaciones con
    otros modelos.

"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class PalabraClaveActividad(db.Model):
    """Modelo que representa una palabra clave asociada a una actividad.

    Cada actividad académica puede tener múltiples palabras clave,
    y cada palabra clave pertenece a una única actividad. La
    relación es de uno a muchos (``Actividad`` → ``PalabraClaveActividad``)
    con borrado en cascada: al eliminar una actividad, sus palabras clave
    se eliminan automáticamente.

    Attributes:
        id_palabra_clave_actividad (int): Clave primaria.
        id_actividad (int): FK a la actividad académica.
        palabra_clave (str): Palabra clave asociada a la
        actividad (máx. 30 caracteres).
        actividad (Actividad): Actividad académica propietaria de
            la palabra clave.

    """

    __tablename__ = "palabra_clave_actividad"

    id_palabra_clave_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE")
    )
    palabra_clave: Mapped[str] = mapped_column(String(30))

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="palabras_clave_actividad"
    )
