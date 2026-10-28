"""Módulo para pruebas sobre el blueprint de autenticación."""

from flask.testing import FlaskClient


def test_login_responde(client: FlaskClient) -> None:
    """Prueba que la ruta de login responde correctamente."""
    respuesta = client.post(
        "startevent/autenticacion/login",
        data={"correo": "a@b.com", "password": "123"},
    )
    assert respuesta.status_code == 200
