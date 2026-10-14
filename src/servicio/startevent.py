"""Servicio para las peticiones relacionadas con StartEvent."""

from datetime import datetime, timezone

from flask import current_app as app
from flask_jwt_extended import create_access_token

from src.dto.autenticacion import OtorgarNuevoTokenDto, RefrescarTokenDto


class StarteventServicio:
    """Atiende las peticiones de StartEventControlador."""

    def refrescar_token(self, dto: RefrescarTokenDto) -> OtorgarNuevoTokenDto:
        """Genera un nuevo token de acceso JWT para el usuario.

        Crea un nuevo token JWT usando la identidad del usuario contenida en
        el DTO. El token se genera con la configuración de expiración
        establecida en la aplicación Flask.

        Args:
            dto (RefrescarTokenDto): DTO que contiene la identidad del usuario
                para la cual se generará el nuevo token.

        Returns:
            OtorgarNuevoTokenDto: DTO que contiene el nuevo token JWT de acceso
                generado.

        """
        token = create_access_token(identity=dto.identidad)
        return OtorgarNuevoTokenDto(token=token)

    def esta_por_expirar(self, timestamp_expiracion: float) -> bool:
        """Verifica si el token JWT está próximo a expirar.

        Compara la fecha actual más un margen de tiempo configurado
        (JWT_POR_EXPIRAR) con el timestamp de expiración del token. Si el
        margen de tiempo se aproxima
        a la fecha de expiración, considera el token como próximo a vencer.

        Args:
            timestamp_expiracion (float): timestamp Unix (segundos desde epoch)
                que indica cuándo expira el token JWT.

        Returns:
            bool: True si el token está próximo a expirar según el margen
                configurado en JWT_POR_EXPIRAR, False en caso contrario.

        """
        esta_por_expirar = False
        utc_time = datetime.now(timezone.utc)
        timestamp_objetivo = datetime.timestamp(
            utc_time + app.config["JWT_POR_EXPIRAR"]
        )
        if timestamp_objetivo > timestamp_expiracion:
            esta_por_expirar = True
        return esta_por_expirar
