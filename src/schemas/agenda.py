"""Modelo que representa la agenda de actividades académicas.

Note:
    Este modelo define la estructura de la tabla `agenda`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Agenda(db.Model):
    """Modelo que representa la agenda de actividades académicas.

    Cada agenda está asociada a un plantel y a una actividad específica.
    La relación es de uno a muchos (``Plantel`` → ``Agenda`` y
    ``Actividad`` → ``Agenda``) con borrado en cascada: al
    eliminar un plantel o una actividad, sus agendas se
    eliminan automáticamente.

    Attributes:
        id_agenda (int): Clave primaria.
        id_plantel (str): FK al plantel.
        id_actividad (int): FK a la actividad.
        plantel (Plantel): Plantel propietario de la agenda.
        actividad (Actividad): Actividad asociada a la agenda.

    """

    __tablename__ = "agenda"

    id_agenda: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE")
    )
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE")
    )

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="agendas")  # pyright: ignore[reportUndefinedVariable]
    actividad: Mapped["Actividad"] = relationship(back_populates="agendas")  # pyright: ignore[reportUndefinedVariable]
