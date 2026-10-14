"""Modelo para representar la clasificación de una persona académica.

Note:
    Este modelo define la estructura de la tabla `clasificacion_persona`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import SubtipoPersona, TipoPersona
from src.inicializacion.extenciones import db


class ClasificacionPersona(db.Model):
    """Modelo que representa la clasificación de una persona académica.

    Cada persona académica puede tener múltiples clasificaciones, y cada
    clasificación pertenece a una única persona académica. La relación
    es de uno a muchos (``PersonaAcademica`` → ``ClasificacionPersona``)
    con borrado en cascada: al eliminar una persona académica,
    sus clasificaciones se eliminan automáticamente.

    Attributes:
        id_clasificacion_persona (int): Clave primaria.
        id_persona_academica (int): FK a la persona académica.
        tipo_persona (TipoPersona): Tipo de la persona.
        subtipo_persona (SubtipoPersona): Subtipo de la persona.
        persona_academica (PersonaAcademica): Persona académica propietaria.

    """

    __tablename__ = "clasificacion_persona"

    id_clasificacion_persona: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    tipo_persona: Mapped[TipoPersona]
    subtipo_persona: Mapped[SubtipoPersona]

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="clasificaciones_persona"
    )
