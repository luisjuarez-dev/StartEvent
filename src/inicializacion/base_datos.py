"""Módulo para la creación de la base de datos con SQLAlchemy."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def crear_base(app: Flask, db: SQLAlchemy) -> None:
    """Crea todas las tablas de base de datos.

    Ejecuta db.create_all() dentro del contexto de la aplicación para
    crear todas las tablas definidas en los modelos SQLAlchemy.

    Args:
        app (Flask): instancia de la aplicación Flask.
        db (SQLAlchemy): instancia de SQLAlchemy.

    """
    with app.app_context():
        from src.schemas.actividad import Actividad
        from src.schemas.actividad_compartida import ActividadCompartida
        from src.schemas.agenda import Agenda
        from src.schemas.asistencia import Asistencia
        from src.schemas.automovil import Automovil
        from src.schemas.autoridad import Autoridad
        from src.schemas.clasificacion_persona import ClasificacionPersona
        from src.schemas.codigo_contrasenia import CodigoContrasenia
        from src.schemas.color_evento import ColorEvento
        from src.schemas.comite_evento import ComiteEvento
        from src.schemas.convocatoria_actividad import ConvocatoriaActividad
        from src.schemas.documento_evento import DocumentoEvento
        from src.schemas.espacio import Espacio
        from src.schemas.evento_academico import EventoAcademico
        from src.schemas.fecha_espacio import FechaEspacio
        from src.schemas.fecha_plantel import FechaPlantel
        from src.schemas.fecha_preferencial import FechaPreferencial
        from src.schemas.horario_actividad import HorarioActividad
        from src.schemas.palabra_clave_actividad import PalabraClaveActividad
        from src.schemas.participante import Participante
        from src.schemas.persona_academica import PersonaAcademica
        from src.schemas.plantel import Plantel
        from src.schemas.propiedades_actividad import PropiedadesActividad
        from src.schemas.requisicion import Requisicion
        from src.schemas.telefono_persona import TelefonoPersona
        from src.schemas.tema_evento import TemaEvento
        from src.schemas.bibliografia_ponente import BiografiaPonente

        db.create_all()
