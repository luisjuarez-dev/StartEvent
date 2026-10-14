"""Interfaces para repositorio para la comunicación entre capas.

Este módulo define la API base para los repositorios y los contratos
específicos que cada entidad del sistema debe implementar.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy import select

from src.enums import SubtipoDocumento, TipoDocumento
from src.inicializacion.extenciones import db
from src.modelo.comite_evento import ComiteEvento
from src.modelo.documento_evento import DocumentoEvento
from src.modelo.persona_academica import PersonaAcademica

ModeloT = TypeVar("ModeloT")
IdT = TypeVar("IdT")


class RepositorioBase(ABC, Generic[ModeloT, IdT]):
    """Define las operaciones comunes para todos los demás repositorios."""

    def __init__(self, clase_modelo: type[ModeloT]) -> None:
        """Inicializa el repositorio con la clase de modelo que administrará.

        Args:
            clase_modelo (type[ModeloT]): La clase del modelo que este
            repositorio manejará.

        """
        self._clase_modelo = clase_modelo

    def insert(self, modelo: ModeloT) -> None:
        """Guarda una nueva instancia del modelo en la base de datos.

        Args:
            modelo (ModeloT): La instancia del modelo a guardar.

        """
        db.session.add(modelo)
        db.session.commit()

    def select_by_id(self, id_: IdT) -> ModeloT | None:
        """Obtiene un registro por su identificador único de la base de datos.

        Args:
            id_ (IdT): El identificador único del registro a buscar.

        Returns:
            ModeloT | None: La instancia del modelo correspondiente al
            identificador, None si no se encuentra.

        """
        return db.session.get(self._clase_modelo, id_)

    def select_all(self) -> list[ModeloT]:
        """Regresa todos los registros de la entidad desde la base de datos.

        Returns:
            list[ModeloT]: Una lista con todas las instancias del modelo en la
            base de datos.

        """
        stmt = select(self._clase_modelo)
        return list(db.session.scalars(stmt).all())

    def update(self, modelo: ModeloT) -> ModeloT:
        """Actualiza un modelo existente y devuelve la versión persistida.

        Args:
            modelo (ModeloT): La instancia del modelo con los cambios a
            actualizar.

        Returns:
            ModeloT: La instancia del modelo después de ser persistida en la
            base de datos.

        """
        modelo_bd = db.session.merge(modelo)
        db.session.commit(modelo_bd)
        return modelo_bd

    def delete(self, modelo: ModeloT) -> None:
        """Elimina un modelo existente de la base de datos.

        Args:
            modelo (ModeloT): La instancia del modelo a eliminar.

        """
        modelo_bd = db.session.merge(modelo)
        db.session.delete(modelo_bd)
        db.session.commit()


class ComiteEventoRepositorioI(RepositorioBase[ComiteEvento, int], ABC):
    """Interfaz de repositorio para el modelo de ComiteEvento."""

    def __init__(self) -> None:
        """Inicializa el repositorio con el modelo correspondiente."""
        super().__init__(ComiteEvento)

    @abstractmethod
    def select_by_id_persona(self, id_persona: int) -> list[ComiteEvento]:
        """Devuelve los comités donde participa una persona específica.

        Args:
            id_persona (int): Identificador de la persona académica.

        Returns:
            list[ComiteEvento]: La lista de todos los comités en los que ha
            participado la persona

        """


class DocumentoEventoRepositorioI(RepositorioBase[DocumentoEvento, int], ABC):
    """Interfaz de repositorio para el modelo de DocumentoEvento."""

    def __init__(self) -> None:
        """Inicializa el repositorio con el modelo correspondiente."""
        super().__init__(DocumentoEvento)

    @abstractmethod
    def select_by_edicion_y_subtipo(
        self,
        id_evento_academico: int,
        tipo: TipoDocumento,
        subtipo: SubtipoDocumento,
    ) -> list[DocumentoEvento]:
        """Busca documentos por evento, tipo y subtipo.

        Args:
            id_evento_academico (int): El identificador del evento académico
            tipo (TipoDocumento): El tipo del documento a buscar
            subtipo (SubtipoDocumento): El subtipo del documento a buscar

        Returns:
            list[DocumentoEvento]: Una lista de todos los documentos que
            cumplen las condiciones

        """


class PersonaAcademicaRepositorioI(
    RepositorioBase[PersonaAcademica, int], ABC
):
    """Interfaz de repositorio para el modelo de PersonaAcadémica."""

    def __init__(self) -> None:
        """Inicializa el repositorio del modelo correspondiente."""
        super().__init__(PersonaAcademica)

    @abstractmethod
    def select_by_correo(self, correo: str) -> PersonaAcademica | None:
        """Obtiene una persona académica a partir de su correo electrónico.

        Args:
            correo (str): Correo electrónico de la persona académica.

        Returns:
            PersonaAcademica | None: La persona académica correspondiente al
            correo, o None si no se encuentra.

        """
