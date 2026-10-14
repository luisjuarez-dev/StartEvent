"""Modelo que representa la actividad compartida entre académicos.

Note:
    Este modelo define la estructura de la tabla `actividad_compartida`
    en la base de datos, incluyendo sus columnas y relaciones con
    otros modelos.

"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class ActividadCompartida(db.Model):
    """Modelo que representa la actividad compartida entre académicos.

    Cada actividad compartida está asociada a una actividad específica,
    y puede tener múltiples remitentes y destinatarios.
    La relación es de uno a muchos (``Actividad`` → ``ActividadCompartida``)
    con borrado en cascada: al eliminar una actividad, sus
    actividades compartidas se eliminan automáticamente.

    Attributes:
        id_actividad_compartida (int): Clave primaria.
        id_actividad (int): FK a la actividad.
        id_remitente (int): FK al académico remitente.
        id_destinatario (int): FK al académico destinatario.
        id_plantel_destinatario (str): FK al plantel del destinatario.
        actividad (Actividad): Actividad asociada a la actividad compartida.
        remitente (PersonaAcademica): Académico remitente de la
            actividad compartida.
        destinatario (PersonaAcademica): Académico destinatario
            de la actividad compartida.
        plantel_destinatario (Plantel): Plantel del destinatario
            de la actividad compartida.

    """

    __tablename__ = "actividad_compartida"

    id_actividad_compartida: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE")
    )
    id_remitente: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    id_destinatario: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    id_plantel_destinatario: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE")
    )

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividades_compartidas"
    )
    remitente: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        foreign_keys=[id_remitente],
        back_populates="actividades_compartidas_remitente",
    )
    destinatario: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        foreign_keys=[id_destinatario],
        back_populates="actividades_compartidas_destinatario",
    )
    plantel_destinatario: Mapped["Plantel"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividades_compartidas"
    )
