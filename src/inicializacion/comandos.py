"""Módulo para la gestión de respaldos de base de datos.

Proporciona funcionalidad para crear respaldos automáticos de la base de datos
usando el comando 'flask backup'
"""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

import click
from flask import Flask
from sqlalchemy import text

from src.inicializacion.base_datos import crear_base
from src.inicializacion.extenciones import db


def registrar_comandos(app: Flask) -> None:
    """Registra comandos de utilidad en CLI en Flask.

    Registra los siguientes comandos para su uso en la terminal:
        - 'flask backup'
        - 'flask format'
        - 'flask crear_base_prueba'

    Args:
        app (Flask): instancia de la aplicación Flask.

    """

    @app.cli.command("backup")
    def backup_command() -> str | None:
        """Crea un respaldo de la base de datos desde Flask.

        Crea un respaldo SQL de la base de datos. El archivo de backup se
        guarda en el directorio Backups con un nombre que incluye la fecha y
        hora actual.

        Returns:
            str | None: La ruta del archivo de backup creado,
            o None si hubo un error.

        """
        db_uri = app.config["SQLALCHEMY_DATABASE_URI"]
        match = re.match(
            r"postgresql\+psycopg2://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)",
            db_uri,
        )
        if not match:
            print("Error: No se pudo leer la URI de la base de datos")  # noqa: T201 para saber que es un print de error
            return None
        usuario, contrasenia, host, puerto, base_datos = match.groups()
        directorio_backup = app.config["DIRECTORIO_BACKUP"]
        directorio_backup.mkdir(exist_ok=True)
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        archivo = directorio_backup / f"backup_{fecha}.sql"
        comando = (
            f"pg_dump -h {host} -p {puerto} -U {usuario} "
            f"-d {base_datos} -f {archivo}"
        )
        env = os.environ.copy()
        env["PGPASSWORD"] = contrasenia

        try:
            resultado = subprocess.run(
                comando, shell=True, env=env, capture_output=True, text=True
            )
        except OSError:
            return None

        if resultado.returncode == 0:
            tamaño = Path(archivo).stat().st_size / 1024
            print(f"Backup creado: {archivo} ({tamaño:.2f} KB)")  # noqa: T201
            return str(archivo)
        return None

    @app.cli.command("format")
    @click.option("--corregir/--no-corregir", default=True)
    def autoformatear(*, corregir: bool) -> None:
        """Formatea automáticamente el código de todo el proyecto.

        Utiliza las herramientas de Ruff y Djlint para indicar los errores
        según la configuración de pyproject.toml, corrige los que sea posible
        y muestra el resto de los errores.

        Note:
            Equivalente a ejecutar
            ruff format
            ruff check --fix
            djlint . --reformat
            djlint . --check

        Examples:
            flask startevent format

        """
        if corregir:
            resultado1 = subprocess.run(
                ["ruff", "format"],
                capture_output=True,
                text=True,
                check=False,
                encoding="UTF8",
            )
        else:
            resultado1 = subprocess.run(
                ["ruff", "format", "--check"],
                capture_output=True,
                text=True,
                check=False,
                encoding="UTF8",
            )
        print(
            f"{'-' * 45}\n\tFormateando archivos python...\n{'-' * 45}\n{resultado1.stdout}",
            flush=True,
        )  # noqa: T201

        if corregir:
            resultado2 = subprocess.run(
                ["ruff", "check", "--fix"],
                capture_output=True,
                text=True,
                check=False,
                encoding="UTF8",
            )
        else:
            resultado2 = subprocess.run(
                ["ruff", "check"],
                capture_output=True,
                text=True,
                check=False,
                encoding="UTF8",
            )
        print(
            f"{'-' * 45}\n\tAnalizando archivos python...\n{'-' * 45}\n{resultado2.stdout}",
            flush=True,
        )  # noqa: T201

        if corregir:
            resultado3 = subprocess.run(
                ["djlint", ".", "--reformat"],
                capture_output=True,
                text=True,
                check=False,
                encoding="UTF8",
            )
        else:
            resultado3 = subprocess.run(
                ["djlint", ".", "--check"],
                capture_output=True,
                text=True,
                check=False,
                encoding="UTF8",
            )
        print(
            f"{'-' * 45}\n\tAnalizando archivos HTML...\n{'-' * 45}{resultado3.stdout}{resultado3.stderr}",
            end="",
            flush=True,
        )  # noqa: T201

        if (
            resultado1.returncode != 0
            or resultado2.returncode != 0
            or resultado3.returncode != 0
        ):
            raise SystemExit(1)

    @app.cli.command("crear_base_prueba")
    def crear_base_prueba() -> None:
        """Pobla la base de datos con los datos de prueba de un script."""
        crear_base(app, db)
        archivo = Path.open(
            app.config["DIRECTORIO_BACKUP"] / "backup_prueba.sql",
            "r",
            encoding="utf-8",
        )
        sql = archivo.read()
        db.session.execute(text(sql))
        db.session.commit()


"""
import subprocess

resultado = subprocess.run(
    ["ruff", "format"],
    capture_output=True,
    text=True,  # devuelve str en lugar de bytes
    check=False,  # no lanza excepción si falla
)

# ruff format escribe casi todo por stderr
if resultado.stdout:
    print("── stdout ──")
    print(resultado.stdout)

if resultado.stderr:
    print("── stderr ──")
    print(resultado.stderr)

print(f"Código de salida: {resultado.returncode}")
"""
