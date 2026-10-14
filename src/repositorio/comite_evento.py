"""Implementación del repositorio para la entidad de ComiteEvento."""

from sqlalchemy import select

from src.inicializacion.extenciones import db
from src.interfaces.repositorio import ComiteEventoRepositorioI
from src.modelo.comite_evento import ComiteEvento


class ComiteEventoRepositorio(ComiteEventoRepositorioI):
    """Accede a la información de ComiteEvento en la base de datos."""

    def select_by_id_persona(self, id_persona: int) -> list[ComiteEvento]:
        """Devuelve los comités donde participa una persona específica.

        Args:
            id_persona (int): Identificador de la persona académica.

        Returns:
            list[ComiteEvento]: La lista de todos los comités en los que ha
            participado la persona

        """
        # .options() sirve para establercer una estrategia para traer los
        # objetos sin hacer un query mas
        stmt = select(ComiteEvento).where(
            ComiteEvento.id_persona_academica == id_persona
        )  # .options(joinedload(ComiteEvento.evento_academico))
        return list(db.session.scalars(stmt).all())
