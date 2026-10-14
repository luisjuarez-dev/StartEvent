"""Modelo para representar códigos de contraseña.

Note:
    Este modelo define la estructura de la tabla `codigo_contrasenia`
    en la base de datos, incluyendo sus columnas y relaciones
    con otros modelos.

"""

from datetime import date, time

from sqlalchemy import Boolean, Date, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class CodigoContrasenia(db.Model):
    """Modelo que representa un código de contraseña de una persona académica.

    Cada persona académica puede tener múltiples códigos de contraseña,
    y cada código
    pertenece a una única persona académica. La relación es de uno a muchos
    (``PersonaAcademica`` → ``CodigoContrasenia``) con borrado en
    cascada: al eliminar una persona académica, sus códigos de contraseña
    se eliminan automáticamente.

    Attributes:
        id_codigo_contrasenia (int): Clave primaria.
        id_persona_academica (int): FK a la persona académica.
        codigo_hash (str): Código de contraseña en formato
            hash (máx. 64 caracteres).
        fecha_expiracion (date): Fecha de expiración del código.
        hora_expiracion (time): Hora de expiración del código.
        usado (bool): Indica si el código ha sido utilizado.
        persona_academica (PersonaAcademica): Persona académica propietaria.

    """

    __tablename__ = "codigo_contrasenia"

    id_codigo_contrasenia: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey(
            "persona_academica.id_persona_academica", ondelete="CASCADE"
        )
    )
    codigo_hash: Mapped[str] = mapped_column(String(64))  # Verificar longitud
    fecha_expiracion: Mapped[date] = mapped_column(Date)
    hora_expiracion: Mapped[time] = mapped_column(Time)
    usado: Mapped[bool] = mapped_column(Boolean)

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="codigos_contrasenia"
    )
