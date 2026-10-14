"""Modelo para representar teléfonos de personas académicas.

Note:
    Este modelo define la estructura de la tabla `telefono_persona`
    en la base de datos, incluyendo sus columnas y relaciones con
    otros modelos.

"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoTelefono
from src.inicializacion.extenciones import db


class TelefonoPersona(db.Model):
    """Modelo que representa un teléfono asociado a una persona académica.

    Cada persona académica puede tener múltiples teléfonos, y cada teléfono
    pertenece a una única persona. La relación es de uno a muchos
    (``PersonaAcademica`` → ``TelefonoPersona``) con borrado en cascada:
    al eliminar una persona, sus teléfonos se eliminan automáticamente.

    Attributes:
        id_telefono_persona (int): Clave primaria.
        id_persona_academica (int): FK a la persona académica.
        tipo_telefono (TipoTelefono): Clasificación del teléfono.
        numero_telefono (str): Número telefónico (máx. 25 caracteres).
        extension (str | None): Extensión, si aplica (máx. 10 caracteres).
        persona_academica (PersonaAcademica): Persona propietaria.

    """

    __tablename__ = "telefono_persona"

    id_telefono_persona: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    tipo_telefono: Mapped[TipoTelefono]
    numero_telefono: Mapped[str] = mapped_column(String(25))
    extension: Mapped[str | None] = mapped_column(String(10), nullable=True)

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="telefonos_persona"
    )
