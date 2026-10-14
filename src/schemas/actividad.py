"""Modelo que representa una actividad académica dentro de un evento.

Note:
    Este modelo define la estructura de la tabla `actividad`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import CarrerasUACM, EstadoActividad
from src.inicializacion.extenciones import db


class Actividad(db.Model):
    """Modelo que representa una actividad académica dentro de un evento.

    Cada actividad está asociada a un evento académico y puede tener
    múltiples agendas, documentos, participantes y otros elementos
    relacionados. La relación es de uno a muchos
    (``EventoAcademico`` → ``Actividad``) con borrado en cascada:
    al eliminar un evento, sus actividades se eliminan automáticamente.

    Attributes:
        id_actividad (int): Clave primaria.
        id_evento_academico (int): FK al evento académico.
        titulo (str): Título de la actividad.
        descripcion (str): Descripción de la actividad.
        carrera_asociada (CarrerasUACM | None): Carrera asociada a
            la actividad.
        estado_actividad (EstadoActividad): Estado de la actividad.
        numero_dias (int): Número de días de la actividad.
        link_reunion (str | None): Link de la reunión de la actividad.
        token (str): Token de la actividad.
        evento_academico (EventoAcademico): Evento propietario de la actividad.
        agendas (list[Agenda]): Agendas asociadas a la actividad.
        actividades_compartidas (list[ActividadCompartida]):
            Actividades compartidas asociadas a la actividad.
        asistencias (list[Asistencia]): Asistencias asociadas a la actividad.
        horarios_actividad (list[HorarioActividad]): Horarios asociados
            a la actividad.
        documentos_evento (list[DocumentoEvento]): Documentos asociados
            a la actividad.
        participantes (list[Participante]): Participantes asociados a
            la actividad.
        convocatorias_actividad (list[ConvocatoriaActividad]):
            Convocatorias asociadas a la actividad.
        fechas_preferenciales (list[FechaPreferencial]): Fechas
            preferenciales asociadas a la actividad.
        palabras_clave_actividad (list[PalabraClaveActividad]): Palabras
            clave asociadas a la actividad.
        propiedades_actividad (PropiedadesActividad): Propiedades
            de la actividad.

    """

    __tablename__ = "actividad"

    id_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    titulo: Mapped[str] = mapped_column(String(200))
    descripcion: Mapped[str] = mapped_column(String(1500))
    carrera_asociada: Mapped[CarrerasUACM | None]
    estado_actividad: Mapped[EstadoActividad]
    numero_dias: Mapped[int] = mapped_column(SmallInteger)
    link_reunion: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )
    token: Mapped[str] = mapped_column(String(64), nullable=True)

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividades"
    )
    agendas: Mapped[list["Agenda"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    actividades_compartidas: Mapped[list["ActividadCompartida"]] = (  # pyright: ignore[reportUndefinedVariable]
        relationship(
            back_populates="actividad",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    asistencias: Mapped[list["Asistencia"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    horarios_actividad: Mapped[list["HorarioActividad"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    participantes: Mapped[list["Participante"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    convocatorias_actividad: Mapped[list["ConvocatoriaActividad"]] = (  # pyright: ignore[reportUndefinedVariable]
        relationship(
            back_populates="actividad",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    fechas_preferenciales: Mapped[list["FechaPreferencial"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    palabras_clave_actividad: Mapped[list["PalabraClaveActividad"]] = (  # pyright: ignore[reportUndefinedVariable]
        relationship(
            back_populates="actividad",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    propiedades_actividad: Mapped["PropiedadesActividad"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="actividad"
    )
