"""Modelo para representar temas de eventos académicos.

Note:
    Este modelo define la estructura de la tabla `tema_evento`
    en la base de datos,incluyendo sus columnas y relaciones con otros modelos.

"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class TemaEvento(db.Model):
    """Modelo que representa un tema asociado a un evento académico.

    Cada evento académico puede tener múltiples temas, y cada tema
    pertenece a un único evento. La relación es de uno a muchos
    (``EventoAcademico`` → ``TemaEvento``) con borrado en cascada:
    al eliminar un evento, sus temas se eliminan automáticamente.

    Attributes:
        id_tema_evento (int): Clave primaria.
        id_evento_academico (int): FK al evento académico.
        tema (str): Nombre del tema (máx. 50 caracteres).
        evento_academico (EventoAcademico): Evento propietario.

    """

    __tablename__ = "tema_evento"

    id_tema_evento: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    tema: Mapped[str] = mapped_column(String(50))

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="temas_evento"
    )
