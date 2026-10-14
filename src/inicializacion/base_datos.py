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
        from src.modelo.actividad import Actividad
        from src.modelo.actividad_compartida import ActividadCompartida
        from src.modelo.agenda import Agenda
        from src.modelo.asistencia import Asistencia
        from src.modelo.automovil import Automovil
        from src.modelo.autoridad import Autoridad
        from src.modelo.clasificacion_persona import ClasificacionPersona
        from src.modelo.codigo_contrasenia import CodigoContrasenia
        from src.modelo.color_evento import ColorEvento
        from src.modelo.comite_evento import ComiteEvento
        from src.modelo.convocatoria_actividad import ConvocatoriaActividad
        from src.modelo.documento_evento import DocumentoEvento
        from src.modelo.espacio import Espacio
        from src.modelo.evento_academico import EventoAcademico
        from src.modelo.fecha_espacio import FechaEspacio
        from src.modelo.fecha_plantel import FechaPlantel
        from src.modelo.fecha_preferencial import FechaPreferencial
        from src.modelo.horario_actividad import HorarioActividad
        from src.modelo.palabra_clave_actividad import PalabraClaveActividad
        from src.modelo.participante import Participante
        from src.modelo.persona_academica import PersonaAcademica
        from src.modelo.plantel import Plantel
        from src.modelo.propiedades_actividad import PropiedadesActividad
        from src.modelo.requisicion import Requisicion
        from src.modelo.telefono_persona import TelefonoPersona
        from src.modelo.tema_evento import TemaEvento
        from src.modelo.bibliografia_ponente import BiografiaPonente

        db.create_all()
