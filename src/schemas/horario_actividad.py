"""Modelo para representar horarios asociados a actividades académicas.

Note:
    Este modelo define la estructura de la tabla `horario_actividad`
    en la base de datos, incluyendo sus columnas y relaciones con
    otros modelos.

"""

from datetime import date, time

from sqlalchemy import Date, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


# -----------------------NOTA-----------------------
# Se movieron las ids al borrar tablas, verificar comportamiento
class HorarioActividad(db.Model):
    """Modelo que representa un horario asociado a una actividad académica.

    Cada actividad académica puede tener múltiples horarios, y cada horario
    pertenece a una única actividad. La relación es de uno a muchos
    (``Actividad`` → ``HorarioActividad``) con borrado en cascada: al eliminar
    una actividad, sus horarios se eliminan automáticamente.

    Attributes:
        id_horario_actividad (int): Clave primaria.
        id_actividad (int | None): FK a la actividad académica.
        id_espacio (int): FK al espacio donde se lleva a cabo el horario.
        fecha (date): Fecha del horario.
        hora_inicio (time): Hora de inicio del horario.
        hora_fin (time | None): Hora de fin del horario.
        actividad (Actividad): Actividad propietaria.
        espacio (Espacio): Espacio asociado al horario.

    """

    __tablename__ = "horario_actividad"

    id_horario_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int | None] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE"), nullable=True
    )
    id_espacio: Mapped[int] = mapped_column(
        ForeignKey("espacio.id_espacio", ondelete="CASCADE")
    )
    fecha: Mapped[date] = mapped_column(Date)
    hora_inicio: Mapped[time] = mapped_column(Time)
    hora_fin: Mapped[time | None] = mapped_column(Time, nullable=True)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="horarios_actividad"
    )
    espacio: Mapped["Espacio"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="horarios_actividad"
    )
