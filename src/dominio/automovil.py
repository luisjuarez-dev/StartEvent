"""Clase que representa un automóvil en el dominio de la aplicación.

Nota: Esta clase incluye validaciones para los atributos del automóvil,
    como la placa, el modelo, el año y el color. Las validaciones aseguran
    que los valores asignados cumplan con ciertos criterios de
    formato y longitud.

"""


class Automovil:
    """Clase que representa un automóvil en el dominio de la aplicación.

    Esta clase incluye validaciones para los atributos del automóvil,
    como la placa, el modelo, el año y el color. Las validaciones aseguran
    que los valores asignados cumplan con ciertos criterios de
    formato y longitud.

    Attributes:
        id_automovil (int): Identificador único del automóvil.
        id_persona_academica (int): Identificador de la persona
            académica asociada al automóvil.
        placa (str): Placa del automóvil.
        modelo (str): Modelo del automóvil.
        anio (str): Año del automóvil.
        color (str): Color del automóvil.

    """

    id_automovil: int
    id_persona_academica: int
    placa: str
    modelo: str
    anio: str
    color: str

    def __init__(
        self,
        placa: str,
        modelo: str,
        anio: str,
        color: str,
        id_persona_academica: int,
    ) -> None:
        """Inicializa una instancia de la clase Automovil."""
        self.id_persona_academica = id_persona_academica
        self.placa = placa
        self.modelo = modelo
        self.anio = anio
        self.color = color
