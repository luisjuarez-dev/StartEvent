"""Modelo para representar espacios físicos.

Note:
    Este modelo define la estructura de la tabla `espacio`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Espacio(db.Model):
    """Modelo que representa un espacio físico dentro de un plantel.

    Cada espacio pertenece a un único plantel y puede estar asociado
    a múltiples fechas y horarios de actividad. La  relacion es de
    uno a muchos (``Espacio`` → ``FechaEspacio`` y
    ``Espacio`` → ``HorarioActividad``) con borrado en cascada:
    al eliminar un espacio, sus fechas y horarios asociados
    se eliminan automáticamente.

    Attributes:
        id_espacio (int): Clave primaria.
        id_plantel (str): Clave foránea que referencia al
            plantel al que pertenece.
        ubicacion (str): Ubicación del espacio (máx. 50 caracteres).
        es_principal (bool): Indica si el espacio es principal.

    """

    __tablename__ = "espacio"

    id_espacio: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE")
    )
    ubicacion: Mapped[str] = mapped_column(String(50))
    es_principal: Mapped[bool] = mapped_column(Boolean)

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="espacios")  # pyright: ignore[reportUndefinedVariable]

    fechas_espacio: Mapped[list["FechaEspacio"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="espacio",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    horarios_actividad: Mapped[list["HorarioActividad"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="espacio",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
