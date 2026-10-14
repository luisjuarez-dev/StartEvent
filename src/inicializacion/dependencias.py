"""Módulo para la inyección de dependencias.

Maneja la composición de la aplicación, la inyección de dependencias entre
capas (repositorio, servicio, controlador), y el registro de blueprints en la
aplicación Flask.
"""

from flask import Flask

from src.blueprints.archivos import crear_archivos_blueprint
from src.blueprints.autenticacion import crear_autenticacion_blueprint
from src.blueprints.componentes import crear_componentes_blueprint
from src.blueprints.evento import crear_evento_blueprint
from src.blueprints.startevent import crear_startevent_blueprint
from src.controlador.archivos import ArchivosControlador
from src.controlador.autenticacion import AutenticacionControlador
from src.controlador.componentes import ComponentesControlador
from src.controlador.evento import EventosControlador
from src.controlador.startevent import StarteventControlador
from src.repositorio.comite_evento import ComiteEventoRepositorio
from src.repositorio.documento_evento import DocumentoEventoRepositorio
from src.repositorio.persona_academica import PersonaAcademicaRepositorio
from src.servicio.archivos import ArchivoServicio
from src.servicio.autenticacion import AutenticadorServicio
from src.servicio.evento import EventosServicio
from src.servicio.startevent import StarteventServicio


def componer_de_raiz(app: Flask) -> None:
    """Registra blueprints en la aplicación inyectando dependencias.

    Realiza la composición de raíz de la aplicación creando instancias de
    repositorios, servicios y controladores e inyectando las dependencias
    apropiadamente.
    Tambien registra todos los blueprints en la aplicación Flask.

    Args:
        app: instancia de la aplicación Flask.

    """
    persona_academica_repositorio = PersonaAcademicaRepositorio()
    comite_evento_repositorio = ComiteEventoRepositorio()
    documento_evento_repositorio= DocumentoEventoRepositorio()
    startevent_servicio = StarteventServicio()
    autenticacion_servicio = AutenticadorServicio(
        persona_academica_repositorio
    )

    eventos_servicio = EventosServicio(comite_evento_repositorio,
                                       documento_evento_repositorio)
    archivos_servicio = ArchivoServicio()
    archivos_controlador = ArchivosControlador(archivos_servicio)
    startevent_controlador = StarteventControlador(startevent_servicio)
    componentes_controlador = ComponentesControlador()
    autenticacion_controlador = AutenticacionControlador(
        autenticacion_servicio
    )
    evento_academico_controlador = EventosControlador(eventos_servicio)

    with app.app_context():
        archivos_bp = crear_archivos_blueprint(archivos_controlador)
        startevent_bp = crear_startevent_blueprint(startevent_controlador)
        autenticacion_bp = crear_autenticacion_blueprint(
            autenticacion_controlador
        )
        componentes_bp = crear_componentes_blueprint(componentes_controlador)
        evento_academico_bp = crear_evento_blueprint(
            evento_academico_controlador
        )

        startevent_bp.register_blueprint(autenticacion_bp)
        startevent_bp.register_blueprint(evento_academico_bp)
        app.register_blueprint(archivos_bp)
        app.register_blueprint(startevent_bp)
        app.register_blueprint(componentes_bp)
