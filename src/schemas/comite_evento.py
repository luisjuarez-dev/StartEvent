"""Modelo para representar comités asociados a eventos.

Note:
    Este modelo define la estructura de la tabla `comite_evento`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import AccesoOrganizador
from src.inicializacion.extenciones import db


class ComiteEvento(db.Model):
    """Modelo que representa un comité asociado a un evento académico.

    Cada evento académico puede tener múltiples comités, y cada comité
    puede estar asociado a un único evento académico.
    La relación es de muchos a uno (``EventoAcademico``→``ComiteEvento``)
    con borrado en cascada: al eliminar
    un evento académico, sus comités se eliminan automáticamente.

    Attributes:
        id_comite_evento (int): Clave primaria.
        id_plantel (str | None): Clave foránea que referencia al plantel
            al que pertenece.
        id_evento_academico (int): Clave foránea que referencia al
            evento académico al que pertenece.
        id_persona_academica (int): Clave foránea que referencia a
            la persona académica al que pertenece.
        acceso_organizador (AccesoOrganizador): Nivel de acceso del
            comité al organizador.
        plantel (Plantel): Relación con el plantel al que pertenece.
        evento_academico (EventoAcademico): Relación con el evento académico
            al que pertenece.
        persona_academica (PersonaAcademica): Relación con la persona académica
            al que pertenece.

    """

    __tablename__ = "comite_evento"

    id_comite_evento: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str | None] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE"), nullable=True
    )
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    acceso_organizador: Mapped[AccesoOrganizador]

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="comites_evento")  # pyright: ignore[reportUndefinedVariable]
    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="comites_evento"
    )
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="comites_evento"
    )
