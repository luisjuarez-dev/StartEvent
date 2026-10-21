def test_login_responde(client):
    respuesta = client.post(
        "startevent/autenticacion/login",
        data={"correo": "a@b.com", "password": "123"},
    )
    assert respuesta.status_code == 200