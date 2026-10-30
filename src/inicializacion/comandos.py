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


def registrar_comandos(app: Flask) -> None:  # noqa: C901
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
    @click.option("--local/--no-local", default=True)
    def autoformatear(*, corregir: bool, local: bool) -> None:
        """Formatea y revisa el código fuente de la aplicación.

        Args:
            corregir (bool): Si es True, corrige los errores de formato y
            estilo.
            local (bool): Si es True, muestra los resultados en la terminal
            local.

        Returns:
            None: No retorna ningún valor, pero puede terminar la ejecución con
            un código de error si ocurre algún fallo durante la revisión.

        """
        comandos_revision_y_correccion = [
            ["ruff", "format"],  # Corrige con el formeador de Python
            ["ruff", "check", "--fix"],  # Corrige con el linter de Python
            [
                "djlint",
                ".",
                "--reformat",
            ],  # Corrige con el formateador de HTML
        ]
        comandos_revision = [
            ["ruff", "format", "--check"],  # Revisa con el formeador de Python
            ["ruff", "check"],  # Revisa con el linter de Python
            ["djlint", ".", "--check"],  # Revisa con el formateador de HTML
        ]
        comandos_ejecucion = []
        capturar_output = (False, False)
        resultados = []
        separadores_local = [
            f"{'-' * 45}\n\tFormateando archivos python...\n{'-' * 45}\n",
            f"{'-' * 45}\n\tAnalizando archivos python...\n{'-' * 45}\n",
            f"{'-' * 45}\n\tFormateando archivos HTML...\n{'-' * 45}\n",
            f"{'-' * 45}\n\tAnalizando archivos HTML...\n{'-' * 45}\n",
        ]

        if corregir:
            comandos_ejecucion = comandos_revision_y_correccion
        else:
            comandos_ejecucion = comandos_revision
        comandos_ejecucion.append(
            ["djlint", ".", "--lint"]
        )  # Revisa con el linter de HTML
        if not local:
            capturar_output = (True, True)

        for i in range(len(comandos_ejecucion)):
            if local:
                print(separadores_local[i])  # noqa: T201
            resultados.append(
                subprocess.run(
                    comandos_ejecucion[i],
                    capture_output=capturar_output[0],
                    text=capturar_output[1],
                    encoding="UTF8",
                )
            )

        if not local:
            error = mostrar_resultados(resultados)
            if error == 1:
                raise SystemExit(1)

    def mostrar_resultados(resultados) -> int:
        """Imprime un resumen de los resultados del comando flask format.

        Args:
            resultados (list): Lista de resultados de los comandos ejecutados.

        Returns:
            int: 1 si hubo errores, 0 si todo salió bien.

        """
        error = 0
        if resultados[0].returncode != 0:
            print("1.- ❌ Algo falló con el formateador de python Ruff\n")  # noqa: T201
            error = 1
        else:
            print(  # noqa: T201
                "1.- ✅ El formateador de python Ruff finalizo correctamente\n"
            )

        if resultados[1].returncode != 0:
            print("2.- ❌ Algo falló con el linter de python Ruff\n")  # noqa: T201
            error = 1
        else:
            print("2.- ✅ El linter de python Ruff finalizo correctamente\n")  # noqa: T201

        if resultados[2].returncode != 0:
            print("3.- ❌ Algo falló con el formateador de HTML Djlint")  # noqa: T201
            error = 1
        else:
            print(  # noqa: T201
                "3.- ✅ El formateador de HTML Djlint finalizo correctamente\n"
            )

        if resultados[3].returncode != 0:
            print("4.- ❌ Algo falló con el linter de HTML Djlint\n")  # noqa: T201
            error = 1
        else:
            print("4.- ✅ El linter de Djlint finalizo correctamente\n")  # noqa: T201

        return error

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
