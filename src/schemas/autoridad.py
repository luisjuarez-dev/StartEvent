"""Modelo para representar la autoridad de una persona académica.

Note:
    Este modelo define la estructura de la tabla `autoridad`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoAutoridad
from src.inicializacion.extenciones import db


class Autoridad(db.Model):
    """Modelo que representa la autoridad de una persona académica.

    Cada persona académica puede tener múltiples autoridades, y cada
    autoridad pertenece a una única persona académica. La relación
    es de uno a muchos (``PersonaAcademica`` → ``Autoridad``)
    con borrado en cascada: al eliminar una persona académica,
    sus autoridades se eliminan automáticamente.

    Attributes:
        id_autoridad (int): Clave primaria.
        id_persona_academica (int): FK a la persona académica.
        id_plantel (str | None): FK al plantel.
        tipo_autoridad (TipoAutoridad): Tipo de la autoridad.
        fecha_ingreso (date): Fecha de ingreso a la autoridad.
        fecha_egreso (date | None): Fecha de egreso de la autoridad.
        persona_academica (PersonaAcademica): Persona académica propietaria.
        plantel (Plantel): Plantel donde ejerce la autoridad.

    """

    __tablename__ = "autoridad"

    id_autoridad: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    id_plantel: Mapped[str | None] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE"), nullable=True
    )
    tipo_autoridad: Mapped[TipoAutoridad]
    fecha_ingreso: Mapped[date] = mapped_column(Date)
    fecha_egreso: Mapped[date | None] = mapped_column(Date, nullable=True)

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="autoridades"
    )
    plantel: Mapped["Plantel"] = relationship(back_populates="autoridades")  # pyright: ignore[reportUndefinedVariable]
