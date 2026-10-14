"""Modelo para representar colores asociados a eventos.

Note:
    Este modelo define la estructura de la tabla `color_evento`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoColor
from src.inicializacion.extenciones import db


class ColorEvento(db.Model):
    """Modelo que representa un color asociado a un evento académico.

    Cada evento académico puede tener múltiples colores, y cada color
    puede estar asociado a un único evento académico.
    La relación es de muchos a uno (``EventoAcademico``→``ColorEvento``)
    con borrado en cascada: al eliminar
    un evento académico, sus colores se eliminan automáticamente.

    Attributes:
        id_color_evento (int): Clave primaria.
        id_evento_academico (int): Clave foránea que referencia al
            evento académico al que pertenece.
        tipo_color (TipoColor): Tipo de color.
        codigo_hexadecimal (str): Código hexadecimal del color.
        evento_academico(EventoAcademico): Relación con el evento académico
            al que pertenece.

    """

    __tablename__ = "color_evento"

    id_color_evento: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    tipo_color: Mapped[TipoColor]
    codigo_hexadecimal: Mapped[str] = mapped_column(CHAR(8))

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="colores_evento"
    )
