"""Modelo para representar requisiciones de materiales o servicios.

Note:
    Este modelo define la estructura de la tabla `requisicion`
    en la base de datos, incluyendo sus columnas y relaciones con
    otros modelos.

"""

from datetime import date

from sqlalchemy import CHAR, Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoRequisicion
from src.inicializacion.extenciones import db


class Requisicion(db.Model):
    """Modelo que representa una requisición de materiales o servicios.

    Cada evento académico puede tener múltiples requisiciones, y
    cada requisición pertenece a un único evento académico. La
    relación es de uno a muchos (``EventoAcademico`` → ``Requisicion``)
    con borrado en cascada: al eliminar un evento académico,
    sus requisiciones se eliminan automáticamente.

    Attributes:
        id_requisicion (int): Clave primaria.
        id_evento_academico (int): FK al evento académico.
        id_plantel (str): FK al plantel.
        numero_requisicion (str): Número de requisición (máx. 10 caracteres).
        partida (str): Partida presupuestal (máx. 10 caracteres).
        tipo_requisicion (TipoRequisicion): Clasificación de la requisición.
        descripcion (str): Descripción detallada (máx. 1500 caracteres).
        fecha_compra (date): Fecha de compra.
        unidades_compradas (int): Cantidad de unidades compradas.
        importe_comprado (float): Importe total de la compra.
        ruta_requisicion (str): Ruta del archivo de la requisición
            (máx. 200 caracteres).
        ruta_factura (str): Ruta del archivo de la factura
            (máx. 200 caracteres).
        evento_academico (EventoAcademico): Evento académico asociado.
        plantel (Plantel): Plantel asociado.

    """

    __tablename__ = "requisicion"

    id_requisicion: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    id_plantel: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE")
    )
    numero_requisicion: Mapped[str] = mapped_column(CHAR(10))
    partida: Mapped[str] = mapped_column(String(10))
    tipo_requisicion: Mapped[TipoRequisicion]
    descripcion: Mapped[str] = mapped_column(String(1500))
    fecha_compra: Mapped[date] = mapped_column(Date)
    unidades_compradas: Mapped[int] = mapped_column(Integer)
    importe_comprado: Mapped[float] = mapped_column(Numeric(5, 2))
    ruta_requisicion: Mapped[str] = mapped_column(String(200))
    ruta_factura: Mapped[str] = mapped_column(String(200))

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(  # pyright: ignore[reportUndefinedVariable]
        back_populates="requisiciones"
    )
    plantel: Mapped["Plantel"] = relationship(back_populates="requisiciones")  # pyright: ignore[reportUndefinedVariable]
