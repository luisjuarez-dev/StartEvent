"""Implementación del servicio de autenticación con JWT."""

import hashlib

from flask_jwt_extended import create_access_token, create_refresh_token

from src.dto.autenticacion import (
    IniciarSesionDto,
    ValiadarCredencialesDto,
)
from src.interfaces.repositorio import PersonaAcademicaRepositorioI


class AutenticadorServicio:
    """Implementación del servicio de autenticación con JWT."""

    def __init__(
        self, repositorio_persona_academica: PersonaAcademicaRepositorioI
    ) -> None:
        """Inicializa el servicio con su repositorio de personas académicas.

        Args:
            repositorio_persona_academica (PersonaAcademicaRepositorioI):
                Instancia del repositorio para PersonaAcademica

        """
        self._repositorio_persona_academica = repositorio_persona_academica

    def validar_credenciales(
        self, dto: IniciarSesionDto
    ) -> ValiadarCredencialesDto:
        """Verifica las credenciales y devuelve un JWT de ser válidas.

        Args:
            dto (IniciarSesionDto): DTO que contiene correo, contraseña y
                pimienta para validar credenciales.

        Returns:
            ValiadarCredencialesDto: DTO con los tokens de acceso y refrescar
            si las credenciales son válidas, un DTO vacío si no.

        """
        persona = self._repositorio_persona_academica.select_by_correo(
            dto.correo
        )

        if (
            persona
            and persona.sal
            and persona.contrasenia
            == hashlib.sha256(
                dto.contrasenia.encode()
                + bytes.fromhex(persona.sal)
                + bytes.fromhex(dto.pimienta)
            ).hexdigest()
        ):
            jwt = create_access_token(identity=persona)
            token_refrescar = create_refresh_token(identity=persona)
            return ValiadarCredencialesDto(
                token_acceso=jwt,
                token_refrescar=token_refrescar,
                codigo=200,
                mensaje="Credenciales válidas",
            )
        return ValiadarCredencialesDto(
            token_acceso=None,
            token_refrescar=None,
            codigo=401,
            mensaje="Correo o contraseña inválidos",
        )
