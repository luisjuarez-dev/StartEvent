"""Fixture para crear la aplicación Flask de prueba."""

import pytest
from flask import Flask
from flask.testing import FlaskClient

from src import crear_app


@pytest.fixture
def app() -> Flask:
    """Crea una instancia de la aplicación Flask para pruebas."""
    return crear_app()  # crea tu app Flask


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Crea un cliente de prueba para la aplicación Flask."""
    return app.test_client()  # el "navegador falso"
