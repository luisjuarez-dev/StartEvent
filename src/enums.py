"""Contiene todas las enumeraciones de las clases del modelo y dominio."""

import enum


class AccesoOrganizador(enum.Enum):
    """Niveles de acceso que puede tener un organizador."""

    ORGANIZACION_EVENTO = "Organizacion_Evento"
    ORGANIZACION_TORNEOS = "Organizacion_Torneos"
    GESTION_REQUISICIONES = "Gestion_Requisiciones"


class SubtipoDocumento(enum.Enum):
    """Representa todos los tipos de documentos diferentes que existen."""

    # TipoDocumento.DOCUMENTO_EVENTO
    PLANEACION_REQUISICIONES = "Planeacion_Requisiciones"
    REPORTE_FINAL = "Reporte_Final"
    # TipoDocumento.DOCUMENTO_PROMOCIONAL
    LOGOTIPO = "Logotipo"
    BANNER_VERTICAL = "Banner"
    BANNER_HORIZONTAL = "Banner_Horizontal"
    CARTEL_PROMOCIONAL = "Cartel_Promocional"
    PALETA_COLORES = "Paleta_Colores"
    # TipoDocumento.DOCUMENTO_CONVOCATORIA
    CONVOCATORIA_ACADEMICA = "Convocatoria_Academica"
    CONVOCATORIA_ESTUDIANTIL = "Convocatoria_Estudiantil"
    # TipoDocumento.DOCUMENTO_PLANTEL
    ACUSE_ESPACIOS = "Acuse_Espacios"
    FONDO_CONSTANCIA = "Fondo_Constancia"
    LISTA_ESTACIONAMIENTO = "Lista_Estacionamiento"
    AGENDA_ACTIVIDADES = "Agenda_Actividades"
    AGENDA_ACTIVIDADES_CULTURALES = "Agenda_Actividades_Culturales"
    AGENDA_POR_DIA = "Agenda_Por_Dia"
    LISTA_TALLERES = "Lista_Talleres"
    LISTA_TORNEOS = "Lista_Torneos"
    # TipoDocumento.DOCUMENTO_ORGANIZADOR
    CARTA_DISPENSA = "Carta_Dispensa"
    CONSTANCIA_ORGANIZADOR = "Constancia_Organizador"
    # TipoDocumento.DOCUMENTO_PONENTE
    CARTA_PRESENTACION = "Carta_Presentacion"
    # TipoDocumento.DOCUMENTO_ACTIVIDAD
    CONSTANCIA_EXPOSITOR = "Constancia_Expositor"
    CONSTANCIA_ASISTENTE = "Constancia_Asistente"
    ACUSE_RECIBIDO = "Acuse_Recibido"
    NOTIFICACION_ACEPTACION = "Notificacion_Aceptacion"
    NOTIFICACION_RECHAZO = "Notificacion_Rechazo"
    NOTIFICACION_CALENDARIZACION = "Notificacion_Calendarizacion"
    CONFIRMACION_CALENDARIZACION = "Confirmacion_Calendarizacion"


class TipoDocumento(enum.Enum):
    """Representa diferentes grupos de documentos que existen."""

    DOCUMENTO_EVENTO = "Documento_Evento"
    DOCUMENTO_PROMOCIONAL = "Documento_Promocional"
    DOCUMENTO_CONVOCATORIA = "Documento_Convocatoria"
    DOCUMENTO_PLANTEL = "Documento_Plantel"
    DOCUMENTO_ORGANIZADOR = "Documento_Organizador"
    DOCUMENTO_PONENTE = "Documento_Ponente"
    DOCUMENTO_ACTIVIDAD = "Documento_Actividad"


class TipoAgenda(enum.Enum):
    """Representa un tipo de agenda del evento."""

    PONENCIA = "Ponencia"
    TALLER = "Taller"
    COMPLEMENTARIA = "Complementaria"


class TipoColor(enum.Enum):
    """Colores representativos de un evento para la creación de documentos."""

    TEXTO_TITULOS = "Texto_Titulos"
    TEXTO_SUBTITULOS = "Texto_Subtitulos"


class TipoTelefono(enum.Enum):
    """Diferenciador entre teléfonos personales o institucionales."""

    EMPRESARIAL = "Empresarial"
    PERSONAL = "Personal"


class TipoPersona(enum.Enum):
    """Grupos de personas principales del sistema."""

    ORGANIZADOR = "Organizador"
    PARTICIPANTE = "Participante"


class SubtipoPersona(enum.Enum):
    """Tipos específicos de personas del sistema, incluye usuarios."""

    PROFESOR = "Profesor"
    ESTUDIANTE = "Estudiante"
    COLABORADOR = "Colaborador"
    PONENTE = "Ponente"
    REPRESENTANTE = "Representante"
    ARTISTA = "Artista"
    TALLERISTA = "Tallerista"
    ASISTENTE = "Asistente"


class NivelEstudios(enum.Enum):
    """Niveles de educación para las constancias."""

    LIC = "Lic."
    MTR = "Mtr."
    DR = "Dr."
    ING = "Ing."
    ESTUDIANTE = "Estudiante"


class EstadoActividad(enum.Enum):
    """Posibles estados del ciclo de vida de una actividad."""

    REVISION = "Revision"
    ACEPTADA = "Aceptada"
    RECHAZADA = "Rechazada"
    CANCELADA = "Cancelada"
    CONFIRMADA = "Confirmada"
    POR_VALIDAR = "Por_Validar"


class CarrerasUACM(enum.Enum):
    """Las carreras de la UACM participantes en el simposio."""

    SOFTWARE = "Software"
    TRANSPORTE = "Transporte"
    MATEMATICAS = "Matematicas"
    ENERGIA = "Energia"
    ELECTRONICA = "Electronica"
    TELECOMUNICACIONES = "Telecomunicaciones"


class TipoAutoridad(enum.Enum):
    """Representa diferentes tipos de autoridades."""

    COORDINADOR_PLANTEL = "Coordinador_Plantel"
    COORDINADOR_COLEGIO = "Coodinador_Colegio"
    RECTOR = "Rector"
    ENLACE = "Enlace"


# Se cambio la enum
class TipoRequisicion(enum.Enum):
    """Modalidades de una requisición."""

    LICITACION = "Licitacion"
    GASTOS_POR_COMPROBAR = "Gastos_Por_Comprobar"
    REEMBOLSO_GASTOS = "Reembolso_Gastos"


class TipoActividad(enum.Enum):
    """Tipos de actividades de un evento."""

    PONENCIA = "Ponencia"
    PANEL = "Panel"
    TALLER = "Taller"
    PRESENTACION = "Presentacion"
    EXHIBICION = "Exhibicion"
    TORNEO = "Torneo"
    GENERICA = "Generica"


class TipoDocumentoEvento(enum.Enum):
    """Tipos de documentos para un evento.

    Incluye documentos promocionales como logotipos y convocatorias lanzadas
    para ponentes
    """

    LOGOTIPO = "Logotipo"
    BANNER_VERTICAL = "Banner_Vertical"
    BANNER_HORIZONTAL = "Banner_Horizontal"
    CARTEL_PROMOCIONAL = "Cartel_Promocional"
    PALETA_DE_COLORES = "Paleta_De_Colores"
    CONVOCATORIA_PONENCIA_ACADEMICA = "Convocatoria_Ponencia_Academica"
    CONVOCATORIA_PONENCIA_ESTUDIANTIL = "Convocatoria_Ponencia_Estudiantil"
    PLANEACION_REQUISICIONES = "Planeacion_Requisiciones"
    ACUSE_DE_ESPACIOS = "Acuse_De_Espacios"


class TipoInstitucion(enum.Enum):
    """Diferentes tipos de instituciones de origen para un ponente."""

    SECTOR_PUBLICO = "Sector_Publico"
    SECTOR_PRIVADO = "Sector_Privado"
    SECTOR_ESTUDIANTIL = "Sector_Estudiantil"
    SECTOR_ACADEMICO = "Sector_Academico"


class TipoParticipante(enum.Enum):
    """Rol de las personas que participan en una actividad."""

    EXPOSITOR = "Expositor"
    RESPONSABLE = "Responsable"


class EstadoActivo(enum.Enum):
    """Estatus de un usuario."""

    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    PENDIENTE = "Pendiente"
