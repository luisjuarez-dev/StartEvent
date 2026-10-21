import pytest
from src import crear_app


@pytest.fixture
def app():
    app = crear_app()          # crea tu app Flask
    return app


@pytest.fixture
def client(app):
    return app.test_client()    # el "navegador falso"