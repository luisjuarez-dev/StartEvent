"""Modelo para representar participantes en actividades académicas.

Note:
    Este modelo define la estructura de la tabla `participante`
    en la base de datos, incluyendo sus columnas y relaciones con otros modelos

"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoParticipante
from src.inicializacion.extenciones import db


class Participante(db.Model):
    """Modelo que representa un participante en una actividad académica.

    Cada actividad académica puede tener múltiples participantes, y
    cada participante
    pertenece a una única actividad. La relación es de uno a muchos
    (``Actividad`` → ``Participante``) con borrado en cascada: al eliminar
    una actividad, sus participantes se eliminan automáticamente.

    Attributes:
        id_participante (int): Clave primaria.
        id_actividad (int): FK a la actividad académica.
        id_persona_academica (int): FK a la persona académica.
        tipo_participante (TipoParticipante): Tipo de participación
            del participante.
        actividad (Actividad): Actividad propietaria.
        persona_academica (PersonaAcademica): Persona académica asociada.

    """

    __tablename__ = "participante"

    id_participante: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE")
    )
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    tipo_participante: Mapped[TipoParticipante]

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="participantes"
    )
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="participantes"
    )
