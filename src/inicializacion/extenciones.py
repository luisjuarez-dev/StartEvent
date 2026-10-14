"""Módulo de extensiones para Flask.

Define y configura las extensiones de Flask utilizadas en la aplicación.
SQLAlchemy para ORM y Flask-JWT-Extended para autenticación JWT.
"""

from flask import redirect, url_for
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from werkzeug import Response

db = SQLAlchemy()
jwt = JWTManager()


@jwt.user_identity_loader
def sustituir_usuario(usuario: "PersonaAcademica") -> str:  # pyright: ignore[reportUndefinedVariable]
    """Sobreescribe la manera de extraer la identidad del usuario para JWT.

    Args:
        usuario: objeto de usuario con atributo id_persona_academica.

    Returns:
        str: identificador único del usuario como cadena de texto.

    """
    return str(usuario.id_persona_academica)


@jwt.user_lookup_loader
def definir_current_user(_: dict, jwt_data: dict) -> "PersonaAcademica | None":  # pyright: ignore[reportUndefinedVariable]
    """Sobreescribe la manera de obtener el usuario actual a partir del JWT.

    Al ejecutarse, este método consulta la base de datos para obtener el objeto
    PeronaAcademica correspondiente de la base de datosy colocarlo en la
    variable current_user de Flask-JWT-Extended.

    Args:
        _ : argumento ignorado pero requerido por Flask-JWT-Extended.
        Representa el header del JWT.
        jwt_data: diccionario con el contenido del JWT

    Returns:
        PersonaAcademica: objeto de usuario correspondiente al JWT

    """
    identidad = int(jwt_data["sub"])
    return db.session.execute(
        text(
            "SELECT id_persona_academica, nombres, es_administrador, "
            "ruta_foto_perfil FROM persona_academica WHERE "
            "id_persona_academica = :id"
        ),
        {"id": identidad},
    ).fetchone()


@jwt.expired_token_loader
def redireccionar_login(_: dict, __: dict) -> Response:
    """Sobreescribe la función de manejo de tokens expirados.

    Args:
        _ : requerido por Flask-JWT-Extended, representa el header del JWT.
        __ : requerido por Flask-JWT-Extended, representa el contenido del JWT.

    Returns:
        str: El HTML de la página de login

    """
    return redirect(url_for("startevent.login"))
