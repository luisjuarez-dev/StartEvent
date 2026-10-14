"""Implementación del repositorio para el modelo de PersonaAcademica."""

from sqlalchemy import select

from src.inicializacion.extenciones import db
from src.interfaces.repositorio import PersonaAcademicaRepositorioI
from src.modelo.persona_academica import PersonaAcademica


class PersonaAcademicaRepositorio(PersonaAcademicaRepositorioI):
    """Consulta personas académicas almacenadas en la base de datos."""

    def select_by_correo(self, correo: str) -> PersonaAcademica | None:
        """Busca una persona académica a partir de su dirección de correo.

        Args:
            correo (str): El correo electrónico de la persona a buscar

        Returns:
            PersonaAcademica | None: La persona si fue encontrada, None si no.

        """
        stmt = select(PersonaAcademica).where(
            PersonaAcademica.correo_contacto == correo
        )
        return db.session.scalars(stmt).one_or_none()
