"""Modelo para representar propiedades de actividades académicas.

Note:
    Este modelo define la estructura de la tabla `propiedades_actividad`
    en la base de datos, incluyendo sus columnas y relaciones con
    otros modelos.

"""

from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoActividad
from src.inicializacion.extenciones import db


class PropiedadesActividad(db.Model):
    """Modelo que representa las propiedades de una actividad académica.

    Cada actividad académica puede tener un conjunto de propiedades, y
    cada conjunto de propiedades pertenece a una única actividad. La relación
    es de uno a uno (``Actividad`` → ``PropiedadesActividad``) con borrado
    en cascada: al eliminar una actividad, sus propiedades se
    eliminan automáticamente.

    Attributes:
        id_propiedades_actividad (int): Clave primaria.
        id_actividad (int): FK a la actividad académica.
        tipo_actividad (TipoActividad): Clasificación de la actividad.
        documentacion (str | None): Ruta del archivo de documentación
            (máx. 200 caracteres).
        cartel_promocional (str | None): Ruta del archivo del cartel
            promocional (máx. 200 caracteres).
        cupo_maximo (int | None): Número máximo de participantes.
        referencias (str | None): Referencias adicionales
            (máx. 5000 caracteres).
        actividad (Actividad): Actividad académica asociada.

    """

    __tablename__ = "propiedades_actividad"

    id_propiedades_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE"), unique=True
    )
    tipo_actividad: Mapped[TipoActividad]
    documentacion: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )
    cartel_promocional: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )
    cupo_maximo: Mapped[int | None] = mapped_column(
        SmallInteger, nullable=True
    )
    referencias: Mapped[str | None] = mapped_column(
        String(5000), nullable=True
    )

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="propiedades_actividad"
    )
