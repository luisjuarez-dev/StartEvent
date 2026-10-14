"""Modelo de datos para la tabla persona_academica.

Note:
    Este modelo define la estructura de la tabla `persona_academica`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import EstadoActivo, NivelEstudios, TipoInstitucion
from src.inicializacion.extenciones import db


class PersonaAcademica(db.Model):
    """Modelo que representa a una persona académica.

    Cada persona académica puede tener múltiples relaciones con otros modelos,
    como teléfonos, autoridades, comités de eventos, documentos de eventos,
    actividades compartidas, asistencias, automóviles, clasificaciones
    de persona, códigos de contraseña y participantes. La relación es
    de uno a muchos con borrado en cascada: al eliminar una persona
    académica, sus relaciones se eliminan automáticamente.

    Attributes:
        id_persona_academica (int): Clave primaria.
        nombres (str): Nombres de la persona (máx. 50 caracteres).
        apellido_paterno (str): Apellido paterno (máx. 50 caracteres).
        apellido_materno (str | None): Apellido materno
            (máx. 50 caracteres, opcional).
        correo_contacto (str | None): Correo de contacto
            (máx. 255 caracteres, opcional).
        estado_activo (EstadoActivo | None): Estado de actividad
            de la persona académica (opcional).
        contrasenia (str | None): Contraseña de la persona
            académica (máx. 64 caracteres, opcional).
        sal (str | None): Sal para la contraseña
            (máx. 64 caracteres, opcional).
        es_administrador (bool | None): Indica si la persona académica
        es administrador (opcional).
        cubiculo (str | None): Cubículo de la persona académica (máx.
            10 caracteres, opcional).
        ruta_foto_perfil (str): Ruta de la foto de perfil (máx.
            200 caracteres, opcional).
        semblanza (str | None): Semblanza de la persona académica (máx
            1700 caracteres, opcional).
        intereses (str | None): Intereses de la persona académica (máx.
            250 caracteres, opcional).
        institucion_procedencia (str | None): Institución de
            procedencia de la persona académica
            (máx. 200 caracteres, opcional).
        tipo_institucion (TipoInstitucion | None): Tipo de institución
            de la persona académica (opcional).
        nivel_estudios (NivelEstudios | None): Nivel de estudios de
            la persona académica (opcional).
        discapacidad (str | None): Discapacidad de la persona académica
            (máx. 200 caracteres, opcional).
        ruta_foto_ponente (str | None): Ruta de la foto del ponente
            (máx. 200 caracteres, opcional).
        telefonos_persona (list[TelefonoPersona]): Lista de teléfonos
            asociados a la persona académica.
        autoridades (list[Autoridad]): Lista de autoridades asociadas
            a la persona académica.
        comites_evento (list[ComiteEvento]): Lista de comités de
            eventos asociados a la persona académica.
        documentos_evento (list[DocumentoEvento]): Lista de documentos
            de eventos asociados a la persona académica.
        actividades_compartidas_remitente (list[ActividadCompartida]):
            Lista de actividades compartidas donde la persona académica
            es remitente.
        actividades_compartidas_destinatario (list[ActividadCompartida]):
            Lista de actividades compartidas donde la persona académica
            es destinatario.
        asistencias (list[Asistencia]): Lista de asistencias asociadas
            a la persona académica.
        automovil (Automovil): Automóvil asociado a la persona académica.
        clasificaciones_persona (list[ClasificacionPersona]): Lista
            de clasificaciones de persona asociadas a la persona académica.
        codigos_contrasenia (list[CodigoContrasenia]): Lista de códigos
            de contraseña asociados a la persona académica.
        participantes (list[Participante]): Lista de participantes
            asociados a la persona académica.

    """

    __tablename__ = "persona_academica"

    id_persona_academica: Mapped[int] = mapped_column(primary_key=True)
    nombres: Mapped[str] = mapped_column(String(50))
    apellido_paterno: Mapped[str] = mapped_column(String(50))
    apellido_materno: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )
    correo_contacto: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )
    estado_activo: Mapped[EstadoActivo | None]
    contrasenia: Mapped[str | None] = mapped_column(
        String(64), nullable=True
    )  # Verificar longitud
    sal: Mapped[str | None] = mapped_column(
        String(64), nullable=True
    )  # Verificar longitud
    es_administrador: Mapped[bool | None] = mapped_column(
        Boolean, nullable=True
    )
    cubiculo: Mapped[str | None] = mapped_column(String(10), nullable=True)
    ruta_foto_perfil: Mapped[str] = mapped_column(String(200), nullable=True)


    nivel_estudios: Mapped[NivelEstudios | None]
    discapacidad: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )


    # Relaciones
    telefonos_persona: Mapped[list["TelefonoPersona"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    autoridades: Mapped[list["Autoridad"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    comites_evento: Mapped[list["ComiteEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    actividades_compartidas_remitente: Mapped[list["ActividadCompartida"]] = (  # pyright: ignore[reportUndefinedVariable]
        relationship(
            foreign_keys="ActividadCompartida.id_remitente",
            back_populates="remitente",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    actividades_compartidas_destinatario: Mapped[
        list["ActividadCompartida"]  # pyright: ignore[reportUndefinedVariable]
    ] = relationship(
        foreign_keys="ActividadCompartida.id_destinatario",
        back_populates="destinatario",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    asistencias: Mapped[list["Asistencia"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    automovil: Mapped["Automovil"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica"
    )
    clasificaciones_persona: Mapped[list["ClasificacionPersona"]] = (  # pyright: ignore[reportUndefinedVariable]
        relationship(
            back_populates="persona_academica",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    codigos_contrasenia: Mapped[list["CodigoContrasenia"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    participantes: Mapped[list["Participante"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    biografias_ponente:  Mapped[list["BiografiaPonente"]] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="persona_academica",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
