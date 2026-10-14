"""Modelo para representar un automóvil perteneciente a una persona académica.

Note:
    Este modelo define la estructura de la tabla `automovil`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Automovil(db.Model):
    """Modelo que representa un automóvil asociado a una persona académica.

    Cada persona académica puede tener un único automóvil, y cada automóvil
    pertenece a una única persona académica. La relación es de uno a muchos
    (``PersonaAcademica`` → ``Automovil``) con borrado en cascada: al eliminar
    una persona académica, su automóvil se elimina automáticamente.

    Attributes:
        id_automovil (int): Clave primaria.
        id_persona_academica (int): FK a la persona académica.
        placa (str): Placa del automóvil.
        modelo (str): Modelo del automóvil.
        anio (str): Año del automóvil.
        color (str): Color del automóvil.
        persona_academica (PersonaAcademica): Persona académica propietaria.

    """

    __tablename__ = "automovil"

    id_automovil: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        ),
        unique=True,
    )
    placa: Mapped[str] = mapped_column(String(10))
    modelo: Mapped[str] = mapped_column(String(50))
    anio: Mapped[str] = mapped_column(String(4))
    color: Mapped[str] = mapped_column(String(20))

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="automovil"
    )
